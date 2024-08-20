from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


class IrisModel:
    """
    A model class for classifying iris species using XGBoost.

    Attributes:
    - model: The XGBoost classifier with specified hyperparameters.
    """

    def __init__(
        self,
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
    ):
        """
        Initializes the IrisModel with specified hyperparameters for the XGBoost classifier.

        Parameters:
        - n_estimators (int): Number of boosting rounds.
        - max_depth (int): Maximum depth of a tree.
        - learning_rate (float): Boosting learning rate.
        - subsample (float): Subsample ratio of the training instances.
        - colsample_bytree (float): Subsample ratio of columns when constructing each tree.
        - random_state (int): Random number seed.
        """
        self.model = XGBClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            learning_rate=learning_rate,
            subsample=subsample,
            colsample_bytree=colsample_bytree,
            random_state=random_state,
            n_jobs=-1,  # Utilize all available CPU cores for parallel processing
            eval_metric="logloss",  # Use log loss as the evaluation metric
        )

    def train(self, x_train, y_train):
        """
        Train the XGBoost model on the provided training data.

        Parameters:
        - x_train: Features for training.
        - y_train: Target labels for training.
        """
        self.model.fit(x_train, y_train)

    def evaluate(self, x_test, y_test):
        """
        Evaluate the model on the test data and return the accuracy score.

        Parameters:
        - x_test: Features for testing.
        - y_test: True labels for testing.

        Returns:
        - accuracy (float): The accuracy of the model on the test data.
        """
        predictions = self.model.predict(x_test)
        return accuracy_score(y_test, predictions)

    def predict(self, x):
        """
        Make predictions on new data using the trained model.

        Parameters:
        - x: New data for which predictions are to be made.

        Returns:
        - predictions: Predicted labels for the input data.
        """
        return self.model.predict(x)
