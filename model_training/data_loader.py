from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def load_data(test_size=0.2, random_state=42):
    """
    Load the Iris dataset and split it into training and testing sets.

    Parameters:
    - test_size (float): The proportion of the dataset to include in the test split.
    - random_state (int): Controls the shuffling applied to the data before applying the split.

    Returns:
    - X_train, X_test, y_train, y_test: The training and testing data and labels.
    """
    # Load the Iris dataset from sklearn
    iris = load_iris()
    X = iris.data  # Features: Sepal length, sepal width, petal length, petal width
    y = iris.target  # Target: Species of the iris flower

    # Split the dataset into training and testing sets
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
