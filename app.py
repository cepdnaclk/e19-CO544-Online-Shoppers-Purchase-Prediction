import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

model_path = 'Saving Trained Models/model_random_forest_classifier'

# Load the trained model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Define mappings for month and visitorType
month_mapping = {
    "Jan": 0, "Feb": 0.2, "Mar": 0.4, "Apr": 0.6, "May": 0.8, "Jun": 1,
    "Jul": 1.2, "Aug": 1.4, "Sep": 1.6, "Oct": 1.8, "Nov": 2, "Dec": 2.2
}

visitor_type_mapping = {
    "New_Visitor": 1,
    "Returning_Visitor": 0
}

# Default values for the missing features
default_values = {
    'OperatingSystems': 1,
    'Weekend': 1,
    'TrafficType': 2,
    'Region': 1,
    'Informational': 0,
    'Informational_Duration': 0.0,
    'Browser': 1,
    'SpecialDay': 0.0
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Convert categorical features to numeric values
    month = month_mapping.get(data['month'], 0)  # Default to 0 if month not found
    visitor_type = visitor_type_mapping.get(data['visitorType'], 0)  # Default to 0 if visitorType not found
    
    # Create the feature list with default values for missing features
    features = [
        
        data['administrative'],
        data['administrativeduration'],
        default_values['Informational'],
        default_values['Informational_Duration'],
        data['productRelated'],
        data['productRelatedDuration'],
        data['bounceRate'],
        data['exitRate'],
        data['pageValue'],
        default_values['SpecialDay'],
        month,
        default_values['OperatingSystems'],
        default_values['Browser'],
        default_values['Region'],
        default_values['TrafficType'],
        visitor_type,
        default_values['Weekend']
        
    ]
    
    # Predict using the loaded model
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
