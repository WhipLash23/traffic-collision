import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Load the model
with open('traffic_collision/test_model.pkl', 'rb') as file:
    model = pickle.load(file)

user_name = None

@app.route('/')
def greet_user():
    user_agent = request.headers.get('User-Agent')
    # return f'I hope...'
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    global user_name
    user_name = name
    return redirect(url_for('predict', name=name))

@app.route('/predict')
def predict():
    return render_template('predict.html', name=user_name)

@app.route('/make_prediction', methods=['POST'])
def make_prediction():
    print("beautiful bitchesss")
    data = request.get_json(force=True)
    print(data)
    # Assuming the data comes in the form of a list of features
    # prediction = model.predict(np.array(data).reshape(1, -1))
    return jsonify({'prediction': 98})
    # return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)