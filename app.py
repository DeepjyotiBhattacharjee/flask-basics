## Create a simple flask application

from flask import Flask, render_template

# create the flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Hello, World !</p>"

@app.route('/welcome')
def welcome_page():
    return "This is the welcome page"

@app.route("/index")
def index_page():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the score is "+str(score)

@app.route('/calculate')
def calculate():
    return render_template("calculate.html")

@app.route('/calculatemarks')
def calculate_marks():...

if __name__ == "__main__":
    app.run(debug=True)