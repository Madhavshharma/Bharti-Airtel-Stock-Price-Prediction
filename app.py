from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Collect features from form
            features = [
                float(request.form['Open']),
                float(request.form['High']),
                float(request.form['Low']),
                float(request.form['Volume']),
                float(request.form['Close_1']),
                float(request.form['High_Low_Spread']),
                float(request.form['Return']),
                float(request.form['SMA_5']),
                float(request.form['SMA_10']),
            ]

            final_input = np.array([features])
            prediction = model.predict(final_input)
            output = round(prediction[0], 2)

            return render_template('predict.html', prediction_text=f"Predict Closing Stock Price: ₹{output}")

        except Exception as e:
            return render_template('predict.html', prediction_text=f"Error: {str(e)}")

    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
