from flask import Flask, request, jsonify
import os
import io
# import base64
from bson.objectid import ObjectId
import numpy as np
from PIL import Image
import pymongo
from pymongo import MongoClient
import tensorflow as tf
from tensorflow.keras.models import load_model
from dotenv import load_dotenv

import time

# load model
load_dotenv()
MODEL_PATH = "plantrecog.keras"
model = load_model(MODEL_PATH)

# Configuration constants
BATCH_SIZE = 32
IMG_HEIGHT = 180
IMG_WIDTH = 180
CLASS_NAMES = ['aloevera', 'banana', 'bilimbi', 'cantaloupe', 'cassava', 'coconut', 'corn', 'cucumber', 'curcuma', 'eggplant', 'galangal', 'ginger', 'guava', 'kale', 'longbeans', 'mango', 'melon', 'orange', 'paddy', 'papaya', 'peperchili', 'pineapple', 'pomelo', 'shallot', 'soybeans', 'spinach', 'sweetpotatoes', 'tobacco', 'waterapple', 'watermelon']

#Connecting to the DB 
cxn = pymongo.MongoClient("mongodb://admin:secret@mongodb:27017")
db = cxn["PlantDB"]
collection=db["plants"]

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_request():
    """ Endpoint to trigger processing of unknown plants. """
    poll_and_process()
    return jsonify({'status': 'Processing started'}), 202

def poll_and_process():
    """ Continuously polls the database for 'Unknown Plant' entries and processes them. """
    unknown_plants = collection.find({"plant_name": "Unknown Plant"})
    for plant in unknown_plants:
        image_data = plant['image_data']
        image = Image.open(io.BytesIO(image_data))
        processed_name = process_plant_image(image)
        collection.update_one({'_id': plant['_id']}, {'$set': {'plant_name': processed_name}})
    print("Processing completed.")


def process_plant_image(image):

    if image.mode != 'RGB':
        image = image.convert('RGB')  # Convert RGBA to RGB if necessary
  
    image = image.resize((IMG_WIDTH, IMG_HEIGHT))
    
    # Convert PIL image to numpy array and scale pixels to 0-1 if your model expects this scaling
    image = tf.keras.utils.img_to_array(image)
    
    # Add batch dimension
    image = tf.expand_dims(image, axis=0)

    # Predict using the loaded model
    predictions = model.predict(image)
    score = tf.nn.softmax(predictions[0])
    predicted_class = CLASS_NAMES[np.argmax(score)]
    return predicted_class


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
