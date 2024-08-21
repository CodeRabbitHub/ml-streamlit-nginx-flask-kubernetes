# ML Streamlit Nginx Flask Kubernetes

A comprehensive machine learning application deployed using Kubernetes, featuring a Flask API, Streamlit UI, and Nginx server. The project leverages Docker, Kubernetes, and Minikube to deploy a scalable and modular machine learning pipeline.

## 🧩 Architecture

![Kubernetes Architecture](./architecture/k8s-arch.drawio.png)

### Architectural Overview and Rationale

The architecture is thoughtfully designed to ensure a robust, scalable, and modular system that meets the demands of modern web applications, particularly in the context of serving machine learning models.

#### Key Components

1. **Flask API with Gunicorn:**
   - **Why Flask with Gunicorn?** Flask is a lightweight and flexible web framework, making it ideal for serving machine learning models. Gunicorn, a Python WSGI HTTP server, complements Flask by efficiently handling multiple incoming requests, ensuring that the API remains responsive under load.
   - **Advantages:**
     - **Scalability:** Gunicorn's ability to spawn multiple worker processes allows the API to scale horizontally, handling more requests without compromising performance.
     - **Reliability:** Flask's simplicity and Gunicorn's robustness ensure that the application remains stable and easy to maintain.

2. **Streamlit UI for Interactive Visualizations:**
   - **Why Streamlit?** Streamlit provides an easy-to-use interface for creating interactive data applications. It allows users to visualize and interact with the data and predictions generated by the machine learning model.
   - **Advantages:**
     - **User Engagement:** Streamlit's real-time interaction capabilities enhance user engagement, making data insights more accessible.
     - **Ease of Development:** The framework is designed for simplicity, allowing for rapid development and iteration of visualization components.

3. **Nginx as a Reverse Proxy:**
   - **Why Nginx?** Nginx is employed as a reverse proxy to route incoming traffic to the appropriate services (Flask API or Streamlit UI) and handle SSL termination, ensuring secure communication between the client and server.
   - **Advantages:**
     - **Security:** By managing SSL certificates and enforcing HTTPS, Nginx secures all client-server communications, protecting sensitive data.
     - **Load Balancing:** Nginx can also distribute traffic among multiple instances of the backend services, ensuring even load distribution and improving overall system performance.

4. **Containerization with Docker:**
   - **Why Docker?** Docker containerizes the Flask API, Streamlit UI, and Nginx server, ensuring consistency across development, testing, and production environments.
   - **Advantages:**
     - **Portability:** Docker containers encapsulate all dependencies, ensuring that the application runs identically across different environments.
     - **Isolation:** Each service runs in its own container, preventing conflicts and making it easier to manage and scale individual components.

5. **Orchestration with Kubernetes:**
   - **Why Kubernetes?** Kubernetes orchestrates the deployment and management of Docker containers, providing scalability, self-healing, and automated rollouts.
   - **Advantages:**
     - **Scalability:** Kubernetes allows the system to automatically scale up or down based on demand, ensuring optimal resource utilization.
     - **Resilience:** Kubernetes' self-healing capabilities automatically replace failed containers, maintaining system availability and reducing downtime.

### Strategic Benefits of This Architecture

- **Modularity:** By separating the application into distinct components (API, UI, proxy), each can be developed, tested, and deployed independently, increasing flexibility and reducing the complexity of managing the system.
- **Scalability:** Both the Flask API and Streamlit UI can be scaled independently based on demand, ensuring that the system remains responsive even under heavy load.
- **Security:** The use of Nginx for SSL termination and routing enhances security, ensuring that all communication is encrypted and that the system can handle high volumes of traffic securely.
- **Ease of Deployment:** Docker and Kubernetes together simplify the deployment process, allowing for continuous integration and delivery pipelines, ensuring that updates can be rolled out quickly and with minimal risk.

This architecture is designed to meet the needs of a production-grade machine learning application, balancing performance, security, and ease of maintenance, while providing a scalable and modular foundation for future growth.

## 📁 Project Structure

```bash
ml-streamlit-nginx-flask-kubernetes/
├── 📁 architecture
│   └── k8s-arch.drawio.png
├── 📁 flask_app
│   ├── app.py
│   ├── iris_model.pkl
│   └── requirements.txt
├── 📁 k8s
│   ├── flask-api-deployment.yaml
│   ├── flask-api-service.yaml
│   ├── nginx-server-deployment.yaml
│   ├── nginx-server-service.yaml
│   ├── streamlit-ui-deployment.yaml
│   └── streamlit-ui-service.yaml
├── 📁 model_training
│   ├── data_loader.py
│   ├── model.py
│   ├── train.py
│   └── utils.py
├── 📁 nginx
│   ├── 📁 certs
│   │   ├── nginx-selfsigned.crt
│   │   └── nginx-selfsigned.key
│   └── nginx.conf
├── 📁 streamlit_app
│   ├── requirements.txt
│   └── streamlit_app.py
├── .gitignore
├── docker-compose.yaml
├── Dockerfile.flask-api
├── Dockerfile.nginx-server
├── Dockerfile.streamlit-ui
├── LICENSE
├── minikube-deployment.bat
└── README.md
```

## 🚀 Features

- **Model Training**: Python scripts for data loading, model training, and utility functions.
- **Flask API**: REST API serving machine learning predictions.
- **Gunicorn**: WSGI server for Flask API.
- **Streamlit UI**: Interactive user interface to visualize model predictions.
- **Nginx Server**: Reverse proxy and SSL termination.
- **Kubernetes**: Deployment and service configurations for scalable and modular architecture.

## 🛠️ Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/CodeRabbitHub/ml-streamlit-nginx-flask-kubernetes.git
    cd ml-streamlit-nginx-flask-kubernetes
    ```

2. **Install Dependencies:**

   - Flask Application:
     ```bash
     cd flask_app
     pip install -r requirements.txt
     ```
   - Streamlit Application:
     ```bash
     cd streamlit_app
     pip install -r requirements.txt
     ```

3. **Set up Docker:**
    ```bash
    docker-compose up --build
    ```

4. **Deploy on Kubernetes:**
    - Start Minikube:
      ```bash
      minikube start
      ```
    - Deploy using the batch script:
      ```bash
      ./minikube-deployment.bat
      ```

## 🎯 Usage

- **Access the Flask API:**
  - URL: `http://localhost:5000/`
- **Access the Streamlit UI:**
  - URL: `http://localhost:8501/`
- **Nginx Server:**
  - URL: `https://localhost/`


## Detailed Overview

This section provides a comprehensive breakdown of the key components of the project, including model training, Flask application, Nginx configuration, and SSL certificate generation. Each part has been meticulously designed to ensure robustness, scalability, and security.

---

## 🧠 Model Training and Artifact Management

The Iris classification model leverages the XGBoost algorithm, known for its efficiency and accuracy in handling structured data. The model is encapsulated within the `IrisModel` class, which manages training, evaluation, and prediction tasks. Post-training, the model is serialized into an artifact, facilitating seamless integration into the Flask application.

### Model Training

The `IrisModel` class is tailored for classifying Iris species using an XGBoost classifier. The class is equipped with customizable hyperparameters, enabling fine-tuning of the model’s performance to suit various use cases.

#### Key Components

- **Initialization:**
    ```python
    def __init__(self, n_estimators=100, max_depth=4, learning_rate=0.1, subsample=0.8, colsample_bytree=0.8, random_state=42):
    ```
    The model initialization involves setting essential hyperparameters, such as the number of boosting rounds, maximum tree depth, learning rate, and sampling ratios. A random seed is also provided to ensure reproducibility, which is critical for consistent model performance across different runs.

- **Training:**
    ```python
    def train(self, x_train, y_train):
    ```
    The `train` method employs the XGBoost model to learn patterns from the provided training data (`x_train`, `y_train`). It utilizes parallel processing capabilities to expedite the training process, ensuring efficient use of computational resources.

- **Evaluation:**
    ```python
    def evaluate(self, x_test, y_test):
    ```
    The `evaluate` method measures the model's accuracy on a test dataset, offering insights into its ability to generalize to new, unseen data. This step is crucial for validating the model's effectiveness before deployment.

- **Prediction:**
    ```python
    def predict(self, x):
    ```
    The `predict` method generates predictions based on new input data, enabling real-time classification tasks within the Flask application.

### Saving the Model Artifact

Upon successful training and evaluation, the model is serialized into a file using Python’s `pickle` module. This serialized artifact (`iris_model.pkl`) ensures that the model can be easily loaded and deployed without retraining, promoting efficiency and resource conservation.

#### Saving the Model
```python
import pickle

# Train the model
iris_model = IrisModel()
iris_model.train(x_train, y_train)

# Save the trained model to a file
with open("iris_model.pkl", "wb") as file:
    pickle.dump(iris_model, file)
```

- **`pickle.dump(iris_model, file)`**: This command serializes the `IrisModel` instance and stores it in the `iris_model.pkl` file. By doing so, the model can be transported and reused across different environments, streamlining the deployment process.

### Loading the Model in Flask

In the Flask application, the saved model artifact is loaded using `pickle`, making it available for prediction tasks. This approach guarantees consistency, as the exact model used during training is deployed in production.

```python
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)
```

### Benefits of Model Serialization

- **Portability:** Serialized models can be easily shared and deployed across different platforms, enhancing the flexibility of your ML pipeline.
- **Consistency:** Ensuring that the deployed model is identical to the trained one mitigates risks of discrepancies in predictions.
- **Reusability:** Reusing the trained model eliminates the need for retraining, saving time and computational resources.

By adopting this model artifact management strategy, the project ensures that the trained model integrates seamlessly into the broader application infrastructure, offering accurate and efficient predictions.

---

## 🚀 Flask Application

The Flask application (`app.py`) acts as the backend API for predicting Iris species based on user-provided features. It loads a pre-trained machine learning model and exposes an endpoint to handle prediction requests.

### Key Components

- **Loading the Model:**
    ```python
    with open("iris_model.pkl", "rb") as file:
        model = pickle.load(file)
    ```
    The application loads the pre-trained model from `iris_model.pkl`, which serves as the engine for generating predictions based on input features.

- **Prediction Endpoint:**
    ```python
    @app.route("/predict", methods=["POST"])
    def predict():
    ```
    The `/predict` endpoint handles POST requests containing a JSON payload with the Iris flower’s features. It processes the input data and returns the predicted class.

- **Input Validation:**
    ```python
    def validate_input(data):
    ```
    The `validate_input` function ensures the incoming data is structured correctly and contains valid numerical values, preventing errors during prediction.

- **Class Name Mapping:**
    ```python
    def get_class_name(class_idx):
    ```
    This function maps the model’s predicted class index to a human-readable class name, making the API response more understandable.

### How It Works

1. **Receive Request:** The API accepts a POST request at the `/predict` endpoint with a JSON payload containing the Iris flower’s features.
2. **Validate Input:** The input data is validated to ensure it meets the expected format and contains valid numerical values.
3. **Make Prediction:** The model processes the validated features and predicts the class of the flower.
4. **Return Response:** The API returns a JSON response that includes the predicted class index and its corresponding name.

### Hosting with Gunicorn

Gunicorn is used to deploy the Flask application in a production environment, handling multiple requests efficiently and ensuring scalability.

#### Command to Run the Application with Gunicorn

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

- **`--bind 0.0.0.0:5000`**: This binds Gunicorn to all available IP addresses on port 5000, making the API accessible across the network.
- **`app:app`**: This specifies the Flask application to be served, with `app` being the instance of the Flask class.

By hosting the Flask application with Gunicorn, the project ensures that it can handle multiple client requests concurrently, providing reliable and fast predictions in a production environment.

---

## 🛠️ Nginx Configuration File

The Nginx configuration file (`nginx.conf`) plays a pivotal role in routing HTTP and HTTPS traffic, proxying requests to the appropriate services, and supporting WebSocket connections within the Kubernetes deployment.

### Configuration Overview

The Nginx configuration is split into key server blocks:

1. **HTTP to HTTPS Redirection:**
    ```nginx
    server {
        listen 80;
        server_name localhost;

        return 301 https://$host$request_uri;
    }
    ```
    - **Port 80 Listening:** Nginx listens for HTTP traffic on port 80.
    - **Redirection:** Automatically redirects all HTTP traffic to HTTPS, ensuring all communications are encrypted and secure.

2. **Main HTTPS Server Block:**
    ```nginx
    server {
        listen 443 ssl;
        server_name localhost;

        ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
        ssl_certificate_key /etc/ssl/certs/nginx-selfsigned.key;
    ```
    - **Port 443 Listening:** Listens for HTTPS traffic, ensuring secure communication.
    - **SSL Configuration:** Uses a self-signed SSL certificate and key to encrypt traffic, safeguarding data transmitted between clients and the server.

3. **Proxying Requests to Streamlit:**
    ```nginx
    location / {
        proxy_pass http://streamlit-ui:8501;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    ```
    - **Proxy Pass:** Routes requests to the Streamlit service, allowing the UI to be served alongside the Flask API.
    - **Header Management:** Preserves critical request headers, maintaining the integrity and traceability of requests.

4. **WebSocket Support:**
    ```nginx
    location /stream {
        proxy_pass http://streamlit-ui:8501/stream;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 86400;
        proxy_send_timeout 86400;
    }
    ```
    - **WebSocket Handling:** Ensures that real-time connections, such as those required for WebSockets, are properly supported, enabling dynamic interactions.

5. **Logging:**
    ```nginx
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
    ```
    - **Access Log:** Records details of incoming requests for monitoring and analysis.
    - **Error Log:** Captures errors encountered during request processing, aiding in debugging.

### Purpose

This Nginx configuration ensures secure communication via HTTPS, efficient routing of requests to the Streamlit service, and proper handling of WebSocket connections. The logging capabilities allow for ongoing monitoring and troubleshooting, ensuring a reliable and secure deployment.

---

## 🔐 Generating SSL Certificates

Securing the Nginx server involves generating SSL certificates, which encrypt data and protect it from unauthorized access.

### Generate SSL Certificates with OpenSSL

Use OpenSSL to generate the SSL certificate (`nginx-selfsigned.crt`) and private key (`nginx-selfsigned.key`):

```bash
openssl req -x509 -nodes -days 365 -newkey rsa

:2048 -keyout nginx-selfsigned.key -out nginx-selfsigned.crt
```

- **`-x509`**: Creates a self-signed certificate.
- **`-nodes`**: Specifies that no passphrase is required for the key.
- **`-days 365`**: The certificate is valid for 365 days.
- **`-newkey rsa:2048`**: Generates a new RSA key with a 2048-bit length.

### SSL Certificates Directory

The generated SSL certificate and key are stored in the `/etc/ssl/certs/` directory, and Nginx is configured to use these files for encrypting communications:

```nginx
ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
ssl_certificate_key /etc/ssl/certs/nginx-selfsigned.key;
```

By following this process, the project ensures that all client-server communications are encrypted, enhancing security and protecting sensitive data.

---

### Streamlining Kubernetes Deployment with Minikube

Minikube is leveraged to create a local Kubernetes cluster, enabling the testing and development of the application in an environment that closely mimics production. The Kubernetes manifests define the deployment of the Flask API, Streamlit UI, and Nginx server, ensuring a seamless and scalable deployment process.

---

This documentation provides a detailed breakdown of the project’s components, highlighting how each part contributes to a robust, scalable, and secure deployment. This structured approach ensures that the application can be effectively maintained and scaled, meeting both current and future requirements.


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

