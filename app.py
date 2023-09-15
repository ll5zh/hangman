from flask import Flask, render_template
from functions import get_word

app = Flask(__name__)

# homepage
@app.route('/')
def home():
    return render_template('home.html')

# game routes
# note: can use functions.py to get the word. store
@app.route('/play/noun')
def play_noun():
    word = get_word('noun')
    data = {'word': word, 'category': 'Noun'}
    return render_template('play.html', data=data)

@app.route('/play/adjective')
def play_adjective():
    word = get_word('adjective')
    data = {'word': word, 'category': 'Adjective'}
    return render_template('play.html', data=data)

@app.route('/play/verb')
def play_verb():
    word = get_word('verb')
    data = {'word': word, 'category': 'Verb'}
    return render_template('play.html', data=data)

@app.route('/play/random')
def play_random():
    word = get_word('')
    data = {'word': word, 'category': 'Random'}
    return render_template('play.html', data=data)

# end of game routes
@app.route('/win/<word>')
def win(word):
    data = {'word': word}
    return render_template('win.html', data=data)

@app.route('/lose/<word>')
def lose(word):
    data = {'word': word}
    return render_template('lose.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
