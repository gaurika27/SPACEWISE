#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pickle

# Load your satellite trajectory dataset (replace 'your_dataset.csv' with the actual file name)
# Make sure your dataset includes columns like 'initial_velocity', 'launch_angle', etc.
df = pd.read_csv('satellite_trajectory_dataset.csv')

# Define features (X) and target variable (y)
features = df[['initial_velocity', 'launch_angle', 'atmospheric_conditions']]
target = df['trajectory_optimization']  # Replace 'trajectory_optimization' with the actual target column name

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Visualize results (for simplicity, you can modify this based on your actual data)
plt.scatter(X_test['initial_velocity'], y_test, color='black', label='Actual')
plt.scatter(X_test['initial_velocity'], predictions, color='blue', label='Predicted')
plt.xlabel('Initial Velocity')
plt.ylabel('Optimized Trajectory')
plt.legend()
plt.show()

with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

