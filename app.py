from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("./handwriting-prediction-ann-model.h5")

@app.route("/")
def home():
    return "Flask ANN Model API is running!"

@app.route("/predict", methods=["GET"])
def predict():
    try:
        # Get JSON data from request
        # data = request.get_json()
        # features = np.array(data["features"]).reshape(1, -1)  # Ensure proper shape

        # Make prediction
        prediction = 2

        return jsonify({"prediction": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
