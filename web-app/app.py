from flask import Flask, render_template, session, flash, redirect, request, jsonify
import base64
import datetime
from bson import binary
from pymongo import MongoClient
import os


app = Flask(__name__)

#Connecting to the DB 
client = MongoClient("");
db = client[''] # Database Name 
collection = db[''] #Collection name

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
    image_data = request.form["image"]
    plant_name = request.form["plant_name"]

    if image_data:
        _, encoded = image_data.split(",", 1)
        data = base64.b64decode(encoded)

        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_plant = {
            "plant_name": plant_name,
            "image_data": binary.Binary(data),
            "date_uploaded": current_date
        }

        # inserting the plant into the collection
        result = collection.insert_one(new_plant)
        return jsonify({"msg": "Image saved successfully!", "id": str(result.inserted_id)}), 200
    
    return jsonify({"msg": "No image data provided."}), 400



if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "8000")
    app.run(port=FLASK_PORT)