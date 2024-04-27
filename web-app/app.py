from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route('/')
def home():
    """
    Route for the main page
    """
    return render_template("home.html")


if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "8000")
    app.run(port=FLASK_PORT)