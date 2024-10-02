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
                        "error": (
                            'Invalid input. Expected JSON with keys: "sepal_length", "sepal_width", '
                            '"petal_length", "petal_width". Example: {"sepal_length": 5.1, "sepal_width": 3.5, '
                            '"petal_length": 1.4, "petal_width": 0.2}'
                        )
                    }
                ),
                400,
            )

        # Extract features from the validated data
        features = np.array(
            [
                data["sepal_length"],
                data["sepal_width"],
                data["petal_length"],
                data["petal_width"],
            ]
        ).reshape(1, -1)

        # Predict the class
        prediction = model.predict(features)
        class_idx = int(prediction[0])

        # Prepare response
        response = {"prediction": class_idx, "class_name": get_class_name(class_idx)}

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)})


def validate_input(data):
    """
    Validate the input JSON data.

    Args:
        data (dict): The JSON data to validate.

    Returns:
        bool: True if the input is valid, otherwise False.
    """
    # Required keys and their types
    required_keys = {
        "sepal_length": (int, float),
        "sepal_width": (int, float),
        "petal_length": (int, float),
        "petal_width": (int, float),
    }

    # Check if data is a dictionary and contains all required keys
    if not isinstance(data, dict):
        return False
    if not all(key in data for key in required_keys):
        return False

    # Validate that all the values are of the correct type
    return all(isinstance(data[key], required_keys[key]) for key in required_keys)


def get_class_name(class_idx):
    """
    Map class index to class name.

    Args:
        class_idx (int): The index of the class.

    Returns:
        str: The name of the class corresponding to the index.
    """
    # Map class index to class name
    class_names = {0: "setosa", 1: "versicolor", 2: "virginica"}
    return class_names.get(class_idx, "unknown")
