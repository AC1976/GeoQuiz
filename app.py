from flask import Flask, render_template, request, session, redirect
from GeoQuizDataV4 import GeoQuizData

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = "John Frusciante is Jesus."

@app.route('/', methods=['GET'])
def index():

    if request.method == "GET":

        [session.pop(key) for key in list(session.keys())]
        return render_template('intro.html')

    else:
        
        pass 
    
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():

    if request.method == 'POST':
        
        if request.form['player'] == "":
            session['player'] = 'Max Verstappen'

        else:         
        
            player = request.form['player']
            session['player'] = player
       
        if session.get("country_list") is None:
            session['country_list'] = []
            
        quiz = GeoQuizData(session.get('country_list'))
        
        country = quiz.api[0]
        session['country'] = country 
        capital = quiz.api[1]
        session['capital'] = capital
        answers = quiz.api[3]
        lifes = 5
        session['lifes'] = lifes

        return render_template('quiz.html', a0=answers[0], a1=answers[1], a2=answers[2], a3=answers[3], a4=answers[4], a5=answers[5], country=session.get('country'), player=session.get('player'), lifes=session.get('lifes'))
        
    if request.method == 'GET':
                       
        quiz = GeoQuizData(session.get('country_list'))
        
        country = quiz.api[0]
        session['country'] = country 
        capital = quiz.api[1]
        session['capital'] = capital
        answers = quiz.api[3]
        cvalue = (len(session.get('country_list')))

        return render_template('quiz.html', a0=answers[0], a1=answers[1], a2=answers[2], a3=answers[3], a4=answers[4], a5=answers[5], country=session.get('country'), player=session.get('player'), countlist=cvalue, lifes=session.get('lifes'))


@app.route('/answer', methods=['POST'])
def answer():

        if request.method == 'POST':
        
            if session.get('capital') == request.form['sub']:

                country_list = session['country_list']
                country_list.append(session.get('country'))
                session['country_list'] = country_list
                
                return render_template('good_answer.html', message='GOED!', number=(198 - len(session['country_list'])))

            else:

                if int(session.get('lifes')) < 1:
                 
                    return render_template('end.html', message='GAME OVER', number=session.get('lifes'))

                else:

                    lifes = int(session.get('lifes')) - 1
                    session['lifes'] = lifes

                    return render_template('wrong_answer.html', message='FOUT!', number=session.get('lifes'))
               
        else:

            pass


if __name__ == '__main__':
    app.run()

