import streamlit as st
import pickle
import numpy as np

# Path to the trained model
#model_path = 'model.pkl'
model_path = 'deployment/web_deployment/model.pkl'

# Load the trained model
with open(model_path, 'rb') as f_in:
    model = pickle.load(f_in)

# Define the mapping for decoding labels
label_to_category = {
    1: 'Normal beats',
    2: 'Supraventricular ectopic beats',
    3: 'Ventricular ectopic beats',
    4: 'Fusion beats',
    5: 'Unknown beats'
}

# Streamlit App
st.set_page_config(
    page_title="ECG Arrhythmia Classifier",
    page_icon="💓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main App Design
st.title("💓 ECG Arrhythmia Classifier")
st.markdown("""
This app predicts the type of heartbeats based on provided ECG data. 
Simply enter the required parameters below and get insights into the heartbeat category.
""")

# Dataset Overview
st.markdown("### 📊 Dataset Overview")
st.markdown("""
#### About the Dataset  
This dataset classifies heartbeats using **two-lead ECG signals**: **Lead II** and **Lead V5**

#### 🎯 Target Classes  
The dataset includes the following heartbeat categories:  
- **N**: Normal beats  
- **S**: Supraventricular ectopic beats  
- **V**: Ventricular ectopic beats  
- **F**: Fusion beats  
- **Q**: Unknown beats  

#### 🧬 Feature Descriptions  
For each lead:  
- **RR Interval**: Preceding and following R-to-R intervals (ms)  
- **Peaks (P, Q, R, S, T)**: Amplitudes of respective waves  
- **QRS Interval**: Duration of QRS complex (ms)  
- **PQ Interval**: Time from atrial to ventricular depolarization (ms)  
- **QT Interval**: Start of ventricular depolarization to end of repolarization (ms)  
- **Morphology (QRS Morph Features 0–4)**: Morphological attributes of QRS complexes  

This dataset provides a robust foundation for cardiac arrhythmia classification.
""")

# Input Fields
st.sidebar.header("Input Parameters")
st.sidebar.markdown("Provide the following details for prediction:")

def get_user_input():
    input_data = {}
    for i in range(2):  # Adjust for the number of data rows you expect
        lead = "Lead II" if i == 0 else "Lead V5"
        st.sidebar.subheader(f"{lead} Parameters")
        input_data.update({
            f"{i}_pre-RR": st.sidebar.number_input(f"{lead}: Pre-RR Interval (ms)", value=206.0),
            f"{i}_post-RR": st.sidebar.number_input(f"{lead}: Post-RR Interval (ms)", value=243.0),
            f"{i}_pPeak": st.sidebar.number_input(f"{lead}: P Peak Amplitude", value=0.047969956),
            f"{i}_tPeak": st.sidebar.number_input(f"{lead}: T Peak Amplitude", value=1.541606797),
            f"{i}_rPeak": st.sidebar.number_input(f"{lead}: R Peak Amplitude", value=1.509806577),
            f"{i}_sPeak": st.sidebar.number_input(f"{lead}: S Peak Amplitude", value=1.509806577),
            f"{i}_qPeak": st.sidebar.number_input(f"{lead}: Q Peak Amplitude", value=0.011090966),
            f"{i}_qrs_interval": st.sidebar.number_input(f"{lead}: QRS Interval (ms)", value=9),
            f"{i}_pq_interval": st.sidebar.number_input(f"{lead}: PQ Interval (ms)", value=3),
            f"{i}_qt_interval": st.sidebar.number_input(f"{lead}: QT Interval (ms)", value=13),
            f"{i}_st_interval": st.sidebar.number_input(f"{lead}: ST Interval (ms)", value=1),
            f"{i}_qrs_morph0": st.sidebar.number_input(f"{lead}: QRS Morph 0", value=0.011090966),
            f"{i}_qrs_morph1": st.sidebar.number_input(f"{lead}: QRS Morph 1", value=0.013109427),
            f"{i}_qrs_morph2": st.sidebar.number_input(f"{lead}: QRS Morph 2", value=0.167740782),
            f"{i}_qrs_morph3": st.sidebar.number_input(f"{lead}: QRS Morph 3", value=0.583400545),
            f"{i}_qrs_morph4": st.sidebar.number_input(f"{lead}: QRS Morph 4", value=1.119587456)
        })
    return input_data

user_input = get_user_input()

# Predict Button
if st.sidebar.button("Predict"):
    # Convert input to array format
    sample_array = np.array([list(user_input.values())])
    
    # Make prediction
    y_pred = model.predict(sample_array)
    
    # Decode the predicted label
    decoded_label = label_to_category.get(y_pred[0], "Unknown")
    
    # Display Results
    st.success(f"The predicted heartbeat type is: **{decoded_label}**")
    st.balloons()
else:
    st.markdown("Enter parameters in the sidebar and click 'Predict' to see results.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit. @Tobi2024")
