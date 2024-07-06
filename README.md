# Healthcare-Diagnosis-Assistant
The Healthcare Diagnosis Assistant is a Flask-based web application designed to assist doctors in predicting diagnoses based on patient symptoms using MindsDB. This application provides a user-friendly interface for entering patient data and obtaining predictions, aiding healthcare professionals in making informed decisions.

Features
Prediction of Diagnoses: Utilizes a machine learning model trained with MindsDB to predict diagnoses based on patient age, gender, and symptoms.
Interactive Web Interface: Allows doctors to input patient information through a web form and receive immediate predictions.
Data Persistence: Connects to a SQLite database (health_data.db) to store and retrieve patient information for predictions.
How It Helps Doctors
The Healthcare Diagnosis Assistant enhances healthcare practices by:

Providing quick and accurate predictions based on patient symptoms.
Allowing doctors to make informed decisions promptly, potentially improving patient care outcomes.
Integrating machine learning capabilities into healthcare diagnostics without requiring deep technical knowledge.
Installation and Setup
To clone and run the Healthcare Diagnosis Assistant locally, follow these steps:

Prerequisites
Python 3.7 or higher
MindsDB installed (pip install mindsdb-sdk)
Flask (pip install flask)
Clone the Repository
bash
Copy code
git clone https://github.com/your-username/healthcare-diagnosis-assistant.git
cd healthcare-diagnosis-assistant
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Start the Flask Application
bash
Copy code
python final_icu_management_and_diagonostic.py
The application will start on http://127.0.0.1:5000/.

Usage
Open your web browser and go to http://127.0.0.1:5000/.
Enter patient information: age, gender, and select symptoms from the dropdown menus.
Click on the "Predict" button to see the predicted diagnosis and an explanation.
Repeat steps for additional predictions or patients.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your improvements. For major changes, please open an issue first to discuss the proposed changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
