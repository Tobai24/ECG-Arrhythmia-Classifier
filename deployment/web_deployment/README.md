## Run Your App Locally with Docker ✨

Follow these steps to get your app running locally in a Docker container:

### 1️⃣ Navigate to the Deployment Directory

```bash
cd deployment/web_deployment
```

**Please before you do this change the model path in the app.py to this `model.pkl` it might have been changed when deploying the app on streamlit cloud**

### 2️⃣ Build the Docker Image

Run the following command to build the Docker image:

```bash
docker build -t streamlit-app:latest .
```

**Pls make sure your bash is in this folder containing the dockerfile**

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

**Please before you do this change the model path in the app.py to this `deployment/web_deployment/model.pkl` streamlit does not regonize the model without giving this path**

### 1️⃣ Prepare Your Repository

Ensure your repository contains the following:

- `app.py`: Your Streamlit app code.
- `requirements.txt`: A file listing the required Python dependencies.

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

the url for this app is : https://heart-class.streamlit.app/

## 🎉 Enjoy Your App!

Whether locally or online, this app is now ready to predict ECG arrhythmia types interactively. 🚀
