# ECG-Arrhythmia-Classifier

### Classifying Arrhythmias from ECG Signals ❤️📈

Hey there! 👋 Welcome to my machine learning project, where I'm working on classifying arrhythmias using ECG signals. This project explores how artificial intelligence can assist in detecting and classifying cardiac conditions with precision.

The entire pipeline is designed to be reproducible and scalable, so you can easily follow along and replicate the results on your machine or in the cloud.✨

I’ve used ECG signal data and built an end-to-end machine learning solution using tools like MLflow, Flask, Docker etc

The goal? Help healthcare professionals detect and classify arrhythmias more accurately, improving patient care with the power of AI.

📝 **Problem Description**

---

Arrhythmias are irregular heartbeats that can be harmless or life-threatening, depending on their type. Early detection is critical for effective patient management and better health outcomes.

**Objective**  
This project aims to develop a machine learning model that classifies arrhythmias based on ECG signal features. By doing so, healthcare providers can detect these conditions with greater precision and speed.

### 📊 **Dataset**

This project uses an ECG dataset from Kaggle, which is based on the **MIT-BIH Arrhythmia Dataset** from PhysioNet. The dataset contains essential features derived from two-lead ECG signals, which are used to train the arrhythmia classification model.

- **Number of records**: 109,446 heartbeats
- **Number of features**: 19

For the model-building process, the dataset is preprocessed and stored in CSV files, ready for training and testing.

For more detailed information about the dataset, including explanations of the columns, please refer to the [data/README.md](./data/README.md).

Ready to see how AI can help detect arrhythmias and save lives? Let’s get started! ✨

### 🔧 Tools & Techniques

To bring this project to life, I used:

- **MLflow** for experiment tracking
- **Flask** for building a lightweight API
- **Docker** for containerizing the pipeline
- **Evidently AI** for monitoring model performance and detecting data drift

This ensures the project is scalable, transparent, and easy to maintain.

---.
