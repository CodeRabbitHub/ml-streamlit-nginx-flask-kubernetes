from data_loader import load_data
from model import IrisModel
from utils import save_model


def main():
    """
    Main function to load data, train the IrisModel, evaluate its performance, and save the trained model.
    """
    # Load the Iris dataset and split it into training and testing sets
    x_train, x_test, y_train, y_test = load_data()

    # Initialize the IrisModel with default hyperparameters and train it on the training data
    iris_model = IrisModel()
    iris_model.train(x_train, y_train)

    # Evaluate the trained model on the test data and print the accuracy
    accuracy = iris_model.evaluate(x_test, y_test)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    # Save the trained model to disk for future use
    save_model(iris_model.model)


if __name__ == "__main__":
    # Entry point for the script
    main()
