# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template
import pandas as pd
import os
print(os.getcwd())
model = pd.read_pickle(r'/home/Harshitajain16/mysite/HousePricePredictor')
cols = ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Area Population']

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Hello from Flask!'

@app.route('/house_price', methods = ['GET','POST'])
def house_price_preidction():
    result = 0
    if request.method == 'POST':
        income = request.form['income']
        house_age = request.form['house_age']
        rooms = request.form['rooms']
        population = request.form['population']
        query = pd.DataFrame({'Avg. Area Income':[income],
                      'Avg. Area House Age':[house_age],
                      'Avg. Area Number of Rooms': [rooms],
                      'Area Population':[population]
                     })
        result = round(model.predict(query)[0],1)
    return render_template('house_price.html', result = result)

@app.route('/about')
def about_page():
    return "This is my Machine Learning Presentation Website"
