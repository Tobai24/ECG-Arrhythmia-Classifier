import pickle
import numpy as np
from flask import Flask, request, jsonify

# Load the trained model
with open('model.pkl', 'rb') as f_in:
    model = pickle.load(f_in)

# Define the mapping for decoding labels
label_to_category = {
    1: 'Normal beats', 
    2: 'Supraventricular ectopic beats', 
    3: 'Ventricular ectopic beats', 
    4: 'Fusion beats', 
    5: 'Unknown beats'}

app = Flask('predict')

@app.route('/predict', methods=['POST'])
def predict():
    sample = request.get_json()

    # Ensure input is in the correct format for the model
    sample_array = np.array([list(sample.values())])

    # Make prediction
    y_pred = model.predict(sample_array)

    # Decode the predicted label
    decoded_label = label_to_category.get(y_pred[0], "Unknown")

    # Create response
    result = {"type": decoded_label}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

    