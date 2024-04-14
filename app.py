from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return "<h1>Garrett Boyd's Resume</h1>"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9449, debug=True) # This will need to be changed from debug=True