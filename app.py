from flask import Flask, render_template, request, flash, redirect, url_for
from flask.ext.wtf import Form
from wtforms import TextField, validators

app = Flask(__name__)
app.config.from_object('config')


class SetParametersForm(Form):
    OmegaM = TextField('OmegaM', [validators.Required()])
    OmegaL = TextField('OmegaL', [validators.Required()])




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/parameters', methods=['GET', 'POST'])
def parameters():
    form = SetParametersForm()
    if form.validate_on_submit():
        return render_template('show_parameters.html',
                               OmegaM=form.OmegaM.data,
                               OmegaL=form.OmegaL.data)
    return render_template('parameters.html', form=form)


@app.route('/distances')
def distances():
    return render_template('distances.html')


@app.route('/show_parameters/OmegaM=<float:OmegaM>/OmegaL=<float:OmegaL>')
def show_parameters(OmegaM, OmegaL):
    return render_template('show_parameters.html', OmegaM=OmegaM, OmegaL=OmegaL)


if __name__ == '__main__':
#    with app.test_request_context():
#        print url_for('index')
#        print url_for('parameters')
#        print url_for('distances')
#        print url_for('show_parameters', OmegaM=0.3, OmegaL=0.7)


    app.run(debug=True, host='0.0.0.0')
