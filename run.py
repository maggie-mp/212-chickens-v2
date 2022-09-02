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
    session['response_list'] = []
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

@app.route('/questions', methods=['GET','POST'])
def questions():
    if not 'question' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        response = request.form["response"]
        session ["response_list"].append(int(response))
        session['question'] += 1
        if session['question'] >= 5:
            return redirect(url_for('results'))
        else:
            return redirect(url_for('questions'))
    return render_template('questions.html',
                            disclaimer='This website is for folks living in Aotearoa, New Zealand | Designed and Coded by Maggie McMillan-Perry',
                            questionss=session['questions_list'],
                            answers=session['answers_list'],
                            current_question=session['question'])
#
#@app.route('/egg', methods=['GET','POST'])
#def egg():
#    session['question'] += 1
#    if session['question'] >= 4:
#        return redirect(url_for('results'))
#    else:
#        return redirect(url_for('questions'))

@app.route('/results')
def results():
    db = sqlite3.connect(MENUDB)
    print(db)

    translated_responses = translate_responses()
    chickens = []
    cur = db.execute('SELECT chicken,mass,egg,friendly,climate,backyard, image FROM chickens')
    for row in cur:
        chickens.append(list(row))
    db.close()

    best_chickens = scored_chickens(chickens, translated_responses)

    return render_template('results.html',
                            disclaimer='This website is for folks living in Aotearoa, New Zealand | Designed and Coded by Maggie McMillan-Perry',
                            best_chickens=best_chickens,
                            chickens=chickens
                            )


def translate_responses():
    answers_list = session["answers_list"]
    response_list = session["response_list"]
    translated_responses = []
    for i in range(len(response_list)):
        translated_responses.append(answers_list[i][response_list[i]])
    return translated_responses


def scored_chickens(chickens, translated_responses):
    scores = {}
    chickens_dictionary = {}
    for chicken in chickens:
        chickens_dictionary[chicken[0]] = chicken
        for i in range(1,len(chicken) - 1):
            current_chicken = chicken[i]
            translated = translated_responses[i - 1]
            if chicken[i] == translated_responses[i - 1]:
                scores[chicken[0]] = scores.get(chicken[0],0) + 1
    sorted_scores = dict(reversed(sorted(scores.items(), key=lambda score: score[1])))
    best_chickens = []
    for top_scorer in list(sorted_scores.items())[:3]:
        best_chickens.append(chickens_dictionary[top_scorer[0]])
    return best_chickens
