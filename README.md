# HR-Employee-Attrition-Prediction
A machine learning project to predict employee attrition using Random Forest Classifier with 97% accuracy, including EDA and Flask-based deployment

This project predicts employee attrition using machine learning models applied to HR datasets. The main objective is to determine whether an employee is likely to leave the company based on various factors such as satisfaction level, evaluation scores, and work hours.

## Overview

### Files Overview

- **`datasets/HR_dataset.csv`**:
  - This file contains the HR dataset used for training and testing the machine learning models. It includes features such as satisfaction level, evaluation scores, and work hours.

- **`notebooks/binary_Classifier_Hr.ipynb`**:
  - The Jupyter notebook (`binary_Classifier_Hr.ipynb`) provides a comprehensive overview of the project. It covers:
    - Data cleaning and preprocessing steps.
    - Exploratory Data Analysis (EDA) visualizations to understand the dataset.
    - Model selection process, where different algorithms are evaluated for predicting employee attrition.
    - Model training and evaluation metrics, including accuracy, precision, recall, and F1-score.

- **`flask_app/`**:
  - This directory contains files related to the deployment of the predictive model using Flask:
    - **`rfc.py`**: Python script that initializes the Flask web application and loads the trained model (`rfc_classifier.pkl`).
    - **`index.html`**: HTML file that defines the user interface for interacting with the model predictions. It allows users to input employee data and receive predictions regarding attrition.

### Setup and Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/HR-Employee-Attrition-Prediction.git
