from flask import Flask, request


# load model

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_image():
    # This could be just a signal to check the database for pending images
    ml_model.process_pending_images()
    return 'Processing started', 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
