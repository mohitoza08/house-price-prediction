from flask import Flask, render_template, request
import numpy as np
import pickle
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


model = pickle.load(open('house_price_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    prediction = None  
    
    try:
        
        data = [
            float(request.form['bedrooms']),
            float(request.form['bathrooms']),
            float(request.form['sqft_living']),
            float(request.form['sqft_lot']),
            float(request.form['floors']),
            float(request.form['waterfront']),
            float(request.form['view']),
            float(request.form['condition']),
            float(request.form['grade']),
            float(request.form['sqft_above']),
            float(request.form['sqft_basement']),
            float(request.form['yr_built']),
            float(request.form['yr_renovated']),
            float(request.form['zipcode']),
            float(request.form['lat']),
            float(request.form['long']),
            float(request.form['sqft_living15']),
            float(request.form['sqft_lot15'])
        ]

        input_data = np.array([data])
        prediction = model.predict(input_data)[0]

        print("Received data:", data)
        print("Predicted:", prediction)

        result = f"🏠 Estimated House Price: ${round(prediction, 2):,}"

    except Exception as e:
        print("Error:", e)
        result = "Error in prediction. Please check your inputs."

    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
