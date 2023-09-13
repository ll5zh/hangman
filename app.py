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
    return render_template('play.html', word=word)

@app.route('/play/adjective')
def play_adjective():
    word = get_word('adjective')
    return render_template('play.html', word=word)

@app.route('/play/verb')
def play_verb():
    word = get_word('verb')
    return render_template('play.html', word=word)

@app.route('/play/random')
def play_random():
    word = get_word('')
    return render_template('play.html', word=word)

if __name__ == '__main__':
    app.run(debug=True)