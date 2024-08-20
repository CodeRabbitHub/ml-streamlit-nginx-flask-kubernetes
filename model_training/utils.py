import pickle


def save_model(model, filename="iris_model.pkl"):
    """
    Save a trained model to disk using pickle.

    Parameters:
    - model: The trained model object to be saved.
    - filename (str): The name of the file where the model will be saved. Defaults to 'iris_model.pkl'.
    """
    with open(filename, "wb") as file:
        # Serialize the model object and save it to the specified file
        pickle.dump(model, file)


def load_model(filename="iris_model.pkl"):
    """
    Load a trained model from disk using pickle.

    Parameters:
    - filename (str): The name of the file from which the model will be loaded. Defaults to 'iris_model.pkl'.

    Returns:
    - model: The deserialized model object.
    """
    with open(filename, "rb") as file:
        # Load the model object from the specified file and return it
        return pickle.load(file)
