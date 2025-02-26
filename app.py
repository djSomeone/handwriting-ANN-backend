from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Load the trained model
model = tf.keras.models.load_model("./handwriting-prediction-ann-model.h5")

@app.route("/")
def home():
    return "Flask ANN Model API is running!"


    
@app.route("/predict", methods=["POST"])
def upload_image():
    try:
        # Get the uploaded image
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400
        
        file = request.files["image"]
        image = Image.open(file)
        # grey scale
        image = image.convert("L")

        # Convert image to NumPy array
        image_array = np.array(image)  # Values will be in range 0-255
        print(image_array.shape)
        
        # Convert NumPy array to list (JSON serializable)
        
        pred=model.predict(np.array([image_array]))
        output=str(pred.argmax())
        print(type(output))
        return jsonify({"pred":int(float(output))})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
