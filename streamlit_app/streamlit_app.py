import streamlit as st
import requests
import os

# URL of the Flask backend API, fetched from environment variables
FLASK_API_URL = os.environ["FLASK_API_URL"]


def main():
    """
    Main function to create a Streamlit web application for predicting Iris species.
    Users can adjust features using sliders, and the prediction is made by sending the data to a Flask API.
    """
    st.title("Iris Species Prediction")

    st.write(
        "Use the sliders to adjust the features and click 'Predict' to see the predicted Iris species."
    )

    # Sliders for input features
    sepal_length = st.slider(
        "Sepal Length (cm)", min_value=4.0, max_value=8.0, value=5.1, step=0.1
    )
    sepal_width = st.slider(
        "Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.5, step=0.1
    )
    petal_length = st.slider(
        "Petal Length (cm)", min_value=1.0, max_value=7.0, value=1.4, step=0.1
    )
    petal_width = st.slider(
        "Petal Width (cm)", min_value=0.1, max_value=2.5, value=0.2, step=0.1
    )

    # When the "Predict" button is clicked
    if st.button("Predict"):
        # Prepare the input data as a dictionary to send to the Flask API
        data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        }

        try:
            # Send a POST request to the Flask API with the input data
            response = requests.post(FLASK_API_URL, json=data)

            # Check if the response is successful
            if response.status_code == 200:
                prediction = response.json()
                st.success(
                    f"Predicted Species: {prediction['class_name'].capitalize()}"
                )
            else:
                st.error("There was an error with the prediction. Please try again.")

        except requests.exceptions.RequestException as e:
            # Handle any errors that occur during the API request
            st.error(f"Request failed: {e}")


if __name__ == "__main__":
    # Entry point for the Streamlit app
    main()
