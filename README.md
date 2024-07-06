# Healthcare-Diagnosis-Assistant
The Healthcare Diagnosis Assistant is a Flask-based web application designed to assist doctors in predicting diagnoses based on patient symptoms using MindsDB. This application provides a user-friendly interface for entering patient data and obtaining predictions, aiding healthcare professionals in making informed decisions.

YOUTUBE VIDEO LINK

https://youtu.be/r-_L3WW7JAg?feature=shared

FEATURES

1. Prediction of Diagnoses:
 Utilizes a machine learning model trained with MindsDB to predict diagnoses based on patient age, gender, and symptoms.
2. Interactive Web Interface:
 Allows doctors to input patient information through a web form and receive immediate predictions.
3. Data Persistence:
 Connects to a SQLite database (health_data.db) to store and retrieve patient information for predictions.
HOW IT HELP DOCTORS

The Healthcare Diagnosis Assistant enhances healthcare practices by:

1. Providing quick and accurate predictions based on patient symptoms.
2. Allowing doctors to make informed decisions promptly, potentially improving patient care outcomes.
3. Integrating machine learning capabilities into healthcare diagnostics without requiring deep technical knowledge.

INSTALLATION AND SETUP

To clone and run the Healthcare Diagnosis Assistant locally, follow these steps:

PREREQUISTIES

1. Python 3.7 or higher
2. MindsDB installed (pip install mindsdb-sdk)
3. Flask (pip install flask)
CLONE THE REPOSITORY

bash
Copy code


git clone https://github.com/your-username/healthcare-diagnosis-assistant.git
cd healthcare-diagnosis-assistant


INSTALL DEPENDENCIES

bash
Copy code


pip install -r requirements.txt
START THE FLASK APPLICATION

bash
Copy code


python final_icu_management_and_diagonostic.py

The application will start on http://127.0.0.1:5000/.

USAGE
1.Open your web browser and go to http://127.0.0.1:5000/.
2. Enter patient information: age, gender, and select symptoms from the dropdown menus.
3. Click on the "Predict" button    to see the predicted diagnosis and an explanation.
4. Repeat steps for additional predictions or patients.

CONTRIBUTING
Contributions are welcome! Please fork the repository and create a pull request with your improvements. For major changes, please open an issue first to discuss the proposed changes.

LICENSE
This project is licensed under the MIT License - see the LICENSE file for details.
