import mindsdb_sdk

MINDSDB_HOST = 'http://127.0.0.1'
MINDSDB_PORT = 47334

def check_model_error():
    try:
        server = mindsdb_sdk.connect(f"{MINDSDB_HOST}:{MINDSDB_PORT}")
        result = server.query("SELECT error FROM information_schema.models WHERE name = 'diagnosis_predictor';")
        error_message = result.fetch()[0]['error']
        return error_message
    except Exception as e:
        print(f"Error checking model error: {e}")
        return None

def main():
    # Check model error initially
    error_message = check_model_error()
    print(f"Initial model 'diagnosis_predictor' error: {error_message}")

    # Attempt to connect to MindsDB and make predictions
    server = mindsdb_sdk.connect(f"{MINDSDB_HOST}:{MINDSDB_PORT}")
    if server is None:
        print("Failed to connect to MindsDB. Exiting.")
        return

    try:
        # Your prediction logic here
        # Ensure the model 'diagnosis_predictor' is in a usable state before making predictions
        prediction_result = predict_diagnosis(server, age, gender, symptom1, symptom2, symptom3)
        print(f"Prediction result: {prediction_result}")

    except Exception as e:
        print(f"Error during prediction: {e}")

if __name__ == "__main__":
    main()


from flask import Flask, render_template, request
import mindsdb_sdk
import time

app = Flask(__name__)

MINDSDB_HOST = 'http://127.0.0.1'
MINDSDB_PORT = 47334

def connect_to_mindsdb():
    for attempt in range(3):
        try:
            print(f"Attempting to connect to MindsDB locally (attempt {attempt + 1})...")
            server = mindsdb_sdk.connect(f"{MINDSDB_HOST}:{MINDSDB_PORT}")
            print("Connected successfully to MindsDB!")
            return server
        except Exception as error:
            print(f"Failed to connect to MindsDB. Error: {error}")
            if attempt < 2:
                print("Retrying in 5 seconds...")
                time.sleep(5)
    return None

def predict_diagnosis(server, age, gender, symptom1, symptom2, symptom3):
    try:
        query = f"""
        SELECT diagnosis, diagnosis_explain
        FROM health_diagnosis.diagnosis_predictor
        WHERE age = {age}
        AND gender = '{gender}'
        AND symptom1 = '{symptom1}'
        AND symptom2 = '{symptom2}'
        AND symptom3 = '{symptom3}'
        """
        result = server.query(query)
        result_list = result.fetch()
        if result_list:
            return result_list[0]['diagnosis'], result_list[0].get('diagnosis_explain', 'No explanation provided')
        else:
            return "Unable to predict", "No results returned from the model"
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Unable to predict", "An error occurred during prediction"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        symptom1 = request.form['symptom1']
        symptom2 = request.form['symptom2']
        symptom3 = request.form['symptom3']

        server = connect_to_mindsdb()
        if server is None:
            return "Failed to connect to MindsDB. Please try again later."

        diagnosis, explanation = predict_diagnosis(server, age, gender, symptom1, symptom2, symptom3)

        return render_template('result.html', diagnosis=diagnosis, explanation=explanation)

    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        symptom1 = request.form['symptom1']
        symptom2 = request.form['symptom2']
        symptom3 = request.form['symptom3']

        server = connect_to_mindsdb()
        if server is None:
            return "Failed to connect to MindsDB. Please try again later."

        diagnosis, explanation = predict_diagnosis(server, age, gender, symptom1, symptom2, symptom3)

        return render_template('result.html', diagnosis=diagnosis, explanation=explanation)

if __name__ == '__main__':
    app.run(debug=True)

