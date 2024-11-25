# ECG Arrhythmia Classifier

## 🚀 Run Your App Locally with Docker

Follow these steps to get your app running locally in a Docker container:

### 1️⃣ Navigate to the Deployment Directory

```bash
cd deployment/web_deployment
```

### 2️⃣ Build the Docker Image

Run the following command to build the Docker image:

```bash
docker build -t streamlit-app:latest .
```

### 3️⃣ Run the Docker Container

Once the image is built, start the Streamlit app with:

```bash
docker run -p 8501:8501 streamlit-app:latest
```

### 4️⃣ Access the App

Open your browser and go to:

```
http://localhost:8501
```

---

## 🌍 Deploy the App for Free on Streamlit Community Cloud

### 1️⃣ Prepare Your Repository

Ensure your repository contains the following:

- `app.py`: Your Streamlit app code.
- `requirements.txt`: A file listing the required Python dependencies.
  - Example:
    ```txt
    streamlit==1.25.0
    numpy
    pandas
    scikit-learn
    ```

### 2️⃣ Push Your Code to GitHub

Commit and push your code to a GitHub repository.

### 3️⃣ Deploy on Streamlit

1. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
2. Log in with your GitHub account.
3. Click on **"New app"** and select the repository containing your app.
4. Configure the deployment:
   - **Main file path**: `app.py`
   - Streamlit will automatically install the dependencies from `requirements.txt`.

### 4️⃣ Share Your App

Once deployed, you’ll receive a unique URL for your app that you can share with others.

---

## 🎉 Enjoy Your App!

Whether locally or online, this app is now ready to predict ECG arrhythmia types interactively. 🚀
