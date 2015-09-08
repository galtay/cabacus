from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parameters')
def parameters():
    return render_template('parameters.html')

@app.route('/distances')
def distances():
    return render_template('distances.html')

if __name__ == '__main__':
    app.run(debug=True)
