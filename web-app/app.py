from flask import Flask, render_template, session, flash, redirect, request, jsonify
import requests
import base64
import datetime
from bson import binary, ObjectId
import pymongo
#from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

#Connecting to the DB 
MONGO_URI=os.getenv('MONGO_URI')
print(f"Connecting to MongoDB at URI: {MONGO_URI}")
cxn = pymongo.MongoClient(MONGO_URI)
db = cxn["PlantDB"]
collection=db["plants"]

@app.route('/')
def home():
    """
    Route for the main page
    """
    return render_template("home.html")



@app.route("/save_picture", methods=["POST"])
def save_picture():
    """
    Route to save image and plant name.
    """
    print("Received request to save picture.")
    image_data = request.form["image"]
    plant_name = "Unknown Plant"
    conf = "0"

    if image_data:
        _, encoded = image_data.split(",", 1)
        data = base64.b64decode(encoded)

        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_plant = {
            "plant_name": plant_name,
            "image_data": binary.Binary(data),
            "confidence": conf,
            "date_uploaded": current_date
        }
        print(f"Saving new plant entry: {new_plant}")

        # Inserting the plant into the collection
        result = collection.insert_one(new_plant)
        plant_id = result.inserted_id

        # Send a POST request to mlclient
        try:
            response = requests.post('http://mlclient:8000/process')
            response.raise_for_status()  # Will raise an exception for HTTP error codes
            print("POST request to mlclient successful.")
        except requests.RequestException as e:
            print(f"Failed to send POST request to mlclient: {str(e)}")
            return jsonify({"msg": "Failed to ping mlclient", "error": str(e)}), 500

        # Fetching the saved image and plant name to display
        saved_plant = collection.find_one({"_id": ObjectId(plant_id)})
        image = base64.b64encode(saved_plant['image_data']).decode('utf-8')
        return render_template("display_plant.html", image=image, plant_name=saved_plant['plant_name'], confidence=saved_plant['confidence'])
    
    return jsonify({"msg": "No image data provided."}), 400



if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "8000")
    app.run(port=FLASK_PORT)