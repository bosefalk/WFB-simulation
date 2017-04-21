from flask import render_template, flash, redirect, request
from app import app
from .forms import UnitForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UnitForm()
    return render_template('index.html',
                           form = form)

@app.route('/result', methods=['GET', 'POST'])
def result():
    print_name = request.form['name']
    print_S = str(request.form['S'])
    string = print_name + ", " + print_S
    return string