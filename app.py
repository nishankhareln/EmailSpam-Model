from flask import Flask, request, jsonify
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

app = Flask(__name__)

# Load the trained model
model_path = './models/logistic_regression_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Load the vectorizer used during training
vectorizer_path = './models/tfidf_vectorizer.pkl'
with open(vectorizer_path, 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


@app.route("/")
def home():
    response = "hello texas..."
    return jsonify({'response':response})

# API endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        user_input = data['email_text']

        # Convert user input to feature vector using the loaded vectorizer
        user_input_features = vectorizer.transform([user_input])

        # Make a prediction
        prediction = model.predict(user_input_features)

        result = "Ham Mail" if prediction[0] == 1 else "Spam Mail"
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
