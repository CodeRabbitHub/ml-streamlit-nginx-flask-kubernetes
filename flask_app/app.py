# app.py
from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract and validate JSON data from the POST request
        data = request.get_json(force=True)
        if not validate_input(data):
            return (
                jsonify(
                    {
                        "error": 'Invalid input. Expected a JSON object with 4 numerical values for the keys: "sepal_length", "sepal_width", "petal_length", "petal_width".'
                    }
                ),
                400,
            )

        # Extract features from the validated data
        features = [
            data["sepal_length"],
            data["sepal_width"],
            data["petal_length"],
            data["petal_width"],
        ]

        # Convert features to numpy array and reshape for prediction
        features = np.array(features).reshape(1, -1)

        # Predict the class
        prediction = model.predict(features)
        class_idx = int(prediction[0])

        # Prepare response
        response = {"prediction": class_idx, "class_name": get_class_name(class_idx)}

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)})


def validate_input(data):
    # Check if data is a dictionary and contains all required keys
    required_keys = {"sepal_length", "sepal_width", "petal_length", "petal_width"}
    if not isinstance(data, dict) or not required_keys.issubset(data.keys()):
        return False

    # Validate that all the values are numbers
    for key in required_keys:
        if not isinstance(data[key], (int, float)):
            return False

    return True


def get_class_name(class_idx):
    # Map class index to class name
    class_names = {0: "setosa", 1: "versicolor", 2: "virginica"}
    return class_names.get(class_idx, "unknown")
