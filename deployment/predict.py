import pickle
from flask import Flask
from flask import request
from flask import jsonify

with open('model.pkl', 'rb') as f_in:
    model = pickle.load(f_in)
    
app = Flask('predict')

@app.route('/predict', methods=['POST'])
def predict(sample):
    sample = request.get_json()
    y_pred = model.predict(sample)
    
    result = {
        "type" : object(y_pred)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
    