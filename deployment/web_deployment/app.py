import streamlit as st
import pickle
import numpy as np

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

# Input Fields
st.sidebar.header("Input Parameters")
st.sidebar.markdown("Provide the following details for prediction:")

def get_user_input():
    input_data = {}
    for i in range(2):  # Adjust for the number of data rows you expect
        st.sidebar.subheader(f"Sample {i}")
        input_data.update({
            f"{i}_pre-RR": st.sidebar.number_input(f"{i} Pre-RR", value=206.0),
            f"{i}_post-RR": st.sidebar.number_input(f"{i} Post-RR", value=243.0),
            f"{i}_pPeak": st.sidebar.number_input(f"{i} P Peak", value=0.047969956),
            f"{i}_tPeak": st.sidebar.number_input(f"{i} T Peak", value=1.541606797),
            f"{i}_rPeak": st.sidebar.number_input(f"{i} R Peak", value=1.509806577),
            f"{i}_sPeak": st.sidebar.number_input(f"{i} S Peak", value=1.509806577),
            f"{i}_qPeak": st.sidebar.number_input(f"{i} Q Peak", value=0.011090966),
            f"{i}_qrs_interval": st.sidebar.number_input(f"{i} QRS Interval", value=9),
            f"{i}_pq_interval": st.sidebar.number_input(f"{i} PQ Interval", value=3),
            f"{i}_qt_interval": st.sidebar.number_input(f"{i} QT Interval", value=13),
            f"{i}_st_interval": st.sidebar.number_input(f"{i} ST Interval", value=1),
            f"{i}_qrs_morph0": st.sidebar.number_input(f"{i} QRS Morph 0", value=0.011090966),
            f"{i}_qrs_morph1": st.sidebar.number_input(f"{i} QRS Morph 1", value=0.013109427),
            f"{i}_qrs_morph2": st.sidebar.number_input(f"{i} QRS Morph 2", value=0.167740782),
            f"{i}_qrs_morph3": st.sidebar.number_input(f"{i} QRS Morph 3", value=0.583400545),
            f"{i}_qrs_morph4": st.sidebar.number_input(f"{i} QRS Morph 4", value=1.119587456)
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
