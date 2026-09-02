import joblib
import numpy as np
from preprocessor import process_review
from flask import Flask, request, jsonify

app = Flask(__name__)

model = joblib.load("model.joblib") #loading the saved Model
vectorizer = joblib.load("tf_idf.joblib") #loading the saved TF-IDf Vectorizer

@app.route("/predict", methods = ["POST"]) # Whenever user POSTs data to /predict, call this function
def predict():
    data = request.get_json() # Reading the incoming JSON Data
    
    reviews = data["reviews"] # Extract the features values from the message
    
    processed_review = process_review(reviews) # Preprocess the review podted
    
    processed_reviews = vectorizer.transform([processed_review])# Extract the features values from the review
    
    prediction = model.predict(processed_reviews)# Predict the sentiment
    
    return jsonify({"prediction": prediction[0]}) # Output the sentiment. jsonify is used to convert python dict to JSON object

@app.route("/health", methods = ['GET']) # Used to Check if the server is running . it"ll output {"status": "ok"} if server is running
def health():
    return jonsify ({"status": "ok"})

if __name__ == "__main__":
    app.run(debug= True, host="0.0.0.0", port=5000) # host: 0.0.0.0 means any computer can connect to this host