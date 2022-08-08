from flask import Flask, render_template
app = Flask(__name__)


questions = [
 ['Hello Question'],
]

answers = [
 ['Hello Person'],
]

@app.route('/')
def index():
    return render_template('index.html',
                            disclaimer='This website is for folks living in Aotearoa, New Zealand | Designed and Coded by Maggie McMillan-Perry',
                            answers=answers)

@app.route('/questions')
def questions():    
    return render_template('questions.html',
                            disclaimer='This website is for folks living in Aotearoa, New Zealand | Designed and Coded by Maggie McMillan-Perry',
                            questions=questions,
                            answers=answers)    