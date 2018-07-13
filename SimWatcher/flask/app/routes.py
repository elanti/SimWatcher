from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/my_simulations')
def my_simulations():
    return render_template('my_simulations.html')
