from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

MENUDB = 'chickens.db'

#chickens = [
#['Red Shavers','Heavy Breed','All Year Round', 'Friendly', 'Not Fussy', 'Small'],
#]

questionss = [
 ['Question 1:', 'How often do you want your chickens to lay?'],
 #['Question 2:', 'How big do you want your chickens to be (in mass)?'],
 #[['Question 3:', 'How friendly do you want your chickens to be?'],
 #['Question 4:', 'How big is your current backyard?'],
 #['Question 5:', 'Do you get wild weather/strange climate where you live?'],
]

answers = [
[['Rarely', 'Summer & Spring', 'All Year Round']],
#[['Light Breed', 'Medium Breed', 'Heavy Breed']],
#[['Friendly', 'Child Friendly']],
#[['Small', 'Medium', 'Large']],
#[['It's very dry/hot, 'It gets rain/cold often', 'Neither']],
]

@app.route('/index')
def index():
    return render_template('index.html',
                            disclaimer='This website is for folks living in Aotearoa, New Zealand | Designed and Coded by Maggie McMillan-Perry',
                            answers=answers)

@app.route('/questions')
def questions():    
    return render_template('questions.html',
                            disclaimer='This website is for folks living in Aotearoa, New Zealand | Designed and Coded by Maggie McMillan-Perry',
                            questionss=questionss,
                            answers=answers)    

@app.route('/results')
def results():  
    db = sqlite3.connect(MENUDB)
    print(db)

    chickens = []
    cur = db.execute('SELECT chicken,mass,egg,friendly,climate,backyard FROM chickens')
    for row in cur:
        chickens.append(list(row))
    db.close()

    return render_template('results.html',
                            disclaimer='This website is for folks living in Aotearoa, New Zealand | Designed and Coded by Maggie McMillan-Perry',
                            chickens=chickens
                            )    