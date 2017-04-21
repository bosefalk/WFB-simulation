from flask import render_template, flash, redirect, request
from app import app
from .forms import UnitForm

def testfun(name1, S1, name2, S2):
    return name1 * S1 + ", " + name2 * S2


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UnitForm()
    output = ""
    if form.validate_on_submit():
        output = testfun(request.form['name1'], int(request.form['S1']),
                         request.form['name2'], int(request.form['S2']))
    return render_template('index.html',
                           form = form, output = output)



