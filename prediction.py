import os
import json
import urllib.request
import pandas as pd
import numpy as np
from dotenv import load_dotenv
load_dotenv()
import joblib
from sklearn.preprocessing import OneHotEncoder



def predict(satisfaction, evaluation, project, hours, time, accident, promotion, department, sal):

    data = pd.DataFrame({
        'dept': ['IT', 'HR', 'Sales'],
        'salary': ['low', 'medium', 'high']
    })

    # Initialize the encoders
    department_encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    salary_encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')

    # Fit and transform the encoders
    department_encoded = department_encoder.fit_transform(data[['dept']])
    salary_encoded = salary_encoder.fit_transform(data[['salary']])

    # Save the encoders to files
    joblib.dump(department_encoder, 'department_encoder.pkl')
    joblib.dump(salary_encoder, 'salary_encoder.pkl')

    satisfaction = float(satisfaction) / 100
    evaluation = float(evaluation) / 100
    project = int(project)
    hours = int(hours)
    time = int(time)
    accident = int(accident)
    promotion = int(promotion)

    # Load the pre-fitted encoders for 'dept' and 'salary'
    department_encoder = joblib.load('department_encoder.pkl')
    salary_encoder = joblib.load('salary_encoder.pkl')

    # Encode the 'dept' and 'salary' values
    department_encoded = department_encoder.transform(np.array([[department]]).reshape(1, -1))
    salary_encoded = salary_encoder.transform(np.array([[sal]]).reshape(1, -1))

    # Create a data array for prediction
    data = np.array([[
        satisfaction,
        evaluation,
        project,
        hours,
        time,
        accident,
        promotion,
    ]])

    # Concatenate the one-hot encoded features
    data = np.concatenate((data, department_encoded, salary_encoded), axis=1)

    model_filename = 'model_linear.pkl'

    svm_best_model = joblib.load(model_filename)
    predictions = svm_best_model.predict(data)

    print("Loading success")