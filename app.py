from flask import Flask, flash, render_template, request

import random

app = Flask(__name__)

attempts_list = []

def show_score():
    if not attempts_list:
        return 'There is currently no high score, it\'s yours for the taking!'
    else:
        return f'The current high score is {min(attempts_list)} attempts'


@app.route('/')
def index():
    return render_template('index.html', score=show_score())


@app.route('/startGame', methods=['GET', 'POST'])
def startGame():
    if request.method == 'POST':
        guess = int(request.form['guess'])
        attempts = int(request.form['attempts'])
        rand_num = int(request.form['rand_num'])
        message = ''

        if guess == rand_num:
            message = f'Nice! You got it! It took you {attempts} attempts'
            attempts_list.append(attempts)
            attempts = 0
            rand_num = random.randint(1, 10)
        else:
            if guess > rand_num:
                message = 'It\'s lower'
            elif guess < rand_num:
                message = 'It\'s higher'

        return render_template(
            'startGame.html', 
            message=message, 
            score=show_score(), 
            attempts=attempts, 
            rand_num=rand_num
            )
    
    else:
        rand_num = random.randint(1, 10)
        return render_template(
            'startGame.html', 
            message='', 
            score=show_score(), 
            attempts=0, 
            rand_num=rand_num
            )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
