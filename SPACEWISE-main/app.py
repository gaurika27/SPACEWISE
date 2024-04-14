from flask import Flask, render_template
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import pickle

from flask import Flask, render_template, request
import maintrajectory as mlmodel

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("trajectory.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get user input from the form
        user_input = request.form.get("user_input")

        # Preprocess data (convert to numerical format if necessary)
        processed_data = preprocess_data(user_input)  # Modify this based on your features

        # Load the model
        model = mlmodel.load_model()

        # Make prediction
        prediction = model.predict([processed_data])[0]

        return render_template("trajectory.html", prediction=prediction)

    return "Something went wrong!"

if __name__ == "__main__":
    app.run(debug=True)

def preprocess_data(data):
    # Implement data preprocessing steps here (e.g., convert string to float)
    # ... (modify this based on your feature type)
    return processed_data

