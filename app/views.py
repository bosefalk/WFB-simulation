from flask import render_template, flash, redirect, request
from app import app
from .forms import UnitForm
from unit_class import Unit
from wfb_simulation import wfb_simulation
from read_csv import win_percent

def testfun(name1, S1, name2, S2):
    return name1 * S1 + ", " + name2 * S2


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UnitForm()
    output = ""
    if form.validate_on_submit():
        unit_one = Unit(request.form['name1'], int(request.form['models1']),
                        int(request.form['WS1']), int(request.form['S1']),
                        int(request.form['T1']), int(request.form['I1']),
                        int(request.form['Sv1']), int(request.form['Ld1']))
        unit_two = Unit(request.form['name2'], int(request.form['models2']),
                        int(request.form['WS2']), int(request.form['S2']),
                        int(request.form['T2']), int(request.form['I2']),
                        int(request.form['Sv2']), int(request.form['Ld2']))

        wfb_simulation(unit_one, unit_two, int(request.form['runs']))
        output = win_percent()


    return render_template('index.html',
                           form = form, output = output)



