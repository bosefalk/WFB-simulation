from flask import render_template, flash, redirect, request
from app import app
from .forms import UnitForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UnitForm()
    if form.validate_on_submit():
        flash('Unit Name = "%s", Strength = "%S"' %
              (form.name, str(form.S)))
        return redirect('/result')
    return render_template('index.html',
                           form = form)

@app.route('/result', methods=['GET', 'POST'])
def result():
    print(request.form['name'])
    print(request.form['S'])