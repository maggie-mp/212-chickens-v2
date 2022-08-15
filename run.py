from flask import Flask, render_template, g, session, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'CHICKENS'

MENUDB = 'chickens.db'

#chickens = [
#['Red Shavers','Heavy Breed','All Year Round', 'Friendly', 'Not Fussy', 'Small'],
#]

@app.route('/index')
@app.route('/')
def index():
    session['question'] = 0
    session['questions_list'] = []
    session['answers_list'] = []
    db = sqlite3.connect(MENUDB)
    cur = db.execute('SELECT * FROM questions')
    for row in cur:
        session['questions_list'].append(list(row))
    cur = db.execute('SELECT * FROM answers')
    for row in cur:
        session['answers_list'].append(list(row))
    db.close()
    
    return render_template('index.html')
    

    # return redirect(url_for('questions'))

@app.route('/questions')
def questions():
    if not 'question' in session:
        return redirect(url_for('index'))
    return render_template('questions.html',
                            disclaimer='This website is for folks living in Aotearoa, New Zealand | Designed and Coded by Maggie McMillan-Perry',
                            questionss=session['questions_list'],
                            answers=session['answers_list'],
                            current_question=session['question'])    

@app.route('/egg', methods=['GET', 'POST'])
def egg():
    session['question'] += 1
    if session['question'] >= 5:
        return redirect(url_for('results'))
    else:
        return redirect(url_for('questions'))

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