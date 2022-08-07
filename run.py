from flask import Flask, render_template
app = Flask(__name__)

burgers = [
 ['Classic Burger', '$4.99'],
 ['Cheese Burger', '$5.99'],
 ['Chicken Burger', '$5.99'],
 ['Double Burger', '$6.99']
]

@app.route('/')
def index():
    return render_template('index.html',
                            disclaimer='This website is for folks living in Aotearoa, New Zealand.',
                            burgers=burgers)

@app.route('/questions')
def questions():    
    return render_template('questions.html')    