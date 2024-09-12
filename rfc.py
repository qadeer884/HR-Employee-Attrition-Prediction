from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the saved model
model = joblib.load('content\Rf_classifier.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    satisfaction_level = float(request.form['satisfaction_level'])
    last_performance_rating = float(request.form['last_performance_rating'])
    number_of_projects = float(request.form['number_of_projects'])
    avg_monthly_hours = float(request.form['avg_monthly_hours'])
    years_at_company = int(request.form['years_at_company'])
    had_work_accident = int(request.form['had_work_accident'])
    promoted_in_last_5_years = int(request.form['promoted_in_last_5_years'])
    salary_level = int(request.form['salary_level'])

    # Create an array for prediction
    features = np.array([[satisfaction_level, last_performance_rating, number_of_projects, avg_monthly_hours, years_at_company, had_work_accident, promoted_in_last_5_years, salary_level]])

    # Make prediction
    prediction = model.predict(features)

    if prediction == 1:
        result = "The employee will leave the company."
    else:
        result = "The employee will not leave the company."

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
