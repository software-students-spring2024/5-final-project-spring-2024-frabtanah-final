import os
import io
# import base64
import numpy as np
from PIL import Image
import pymongo
import tensorflow as tf
from tensorflow.keras.models import load_model
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()
MODEL_PATH = "plantrecog.keras"
model = load_model(MODEL_PATH)

BATCH_SIZE = 32
IMG_HEIGHT = 180
IMG_WIDTH = 180
CLASS_NAMES = ['aloevera', 'banana', 'bilimbi', 'cantaloupe', 'cassava', 'coconut', 'corn', 'cucumber', 'curcuma', 'eggplant', 'galangal', 'ginger', 'guava', 'kale', 'longbeans', 'mango', 'melon', 'orange', 'paddy', 'papaya', 'peperchili', 'pineapple', 'pomelo', 'shallot', 'soybeans', 'spinach', 'sweetpotatoes', 'tobacco', 'waterapple', 'watermelon']
test_path = "test/spinach801.jpg"

img = tf.keras.utils.load_img(
    test_path, target_size=(IMG_HEIGHT, IMG_HEIGHT)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(CLASS_NAMES[np.argmax(score)], 100 * np.max(score))
)
