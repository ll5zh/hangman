// update game category
const categoryInfo = document.querySelector('.category');
categoryInfo.innerHTML = `Category: ${category}`;

// letters
const letters = document.querySelector('.letters');
const LetterInterface = (() => {
    const createLetters = () => {
        for (let i = 65; i <= 90; ++i) {
            const button = document.createElement('button');
            const buttonVal = String.fromCharCode(i);
            button.innerHTML = buttonVal;
            letters.appendChild(button);
            // on click, activate function from GamePlay module
            button.addEventListener('click', function(e) {
                Gameplay.playRound(buttonVal, button);
            });
        }
    };
    return {
        createLetters,
    }
})();

LetterInterface.createLetters();

// word display
const wordContainer = document.querySelector('.word');

const WordDisplay = (() => {
    const length = word.length;
    const wordChars = wordContainer.children;
    const createDisplay = () => {
        for (let i = 0; i < length; ++i) {
            const char = document.createElement('button');
            char.classList.add('char');
            char.innerHTML = '_';
            wordContainer.appendChild(char);
        }
    };

    // function to update display, takes in most recent character
    const updateDisplay = (letter) => {
        for (let i = 0; i < length; ++i) {
            if (word[i] == letter) {
                wordChars[i].innerHTML = letter;
            }
        }
    };

    const isGuessed = () => {
        for (let i = 0; i < length; ++i) {
            if (wordChars[i].innerHTML == '_') {
                return false;
            }
        }
        return true;
    }

    return {
        length,
        wordChars,
        createDisplay,
        updateDisplay,
        isGuessed,
    }
})();

WordDisplay.createDisplay();

// game control
const img = document.querySelector('img');

const Gameplay = (() => {
    let tries = 6;
    let isPlaying = true;
    let guessedLetters = [];
    const hangmans = [
        // position in array corresponds to number of tries
        'https://www.oligalma.com/downloads/images/hangman/hangman/10.jpg',
        'https://www.oligalma.com/downloads/images/hangman/hangman/9.jpg',
        'https://www.oligalma.com/downloads/images/hangman/hangman/8.jpg',
        'https://www.oligalma.com/downloads/images/hangman/hangman/7.jpg',
        'https://www.oligalma.com/downloads/images/hangman/hangman/6.jpg',
        'https://www.oligalma.com/downloads/images/hangman/hangman/5.jpg',
        'https://www.oligalma.com/downloads/images/hangman/hangman/4.jpg',
    ]
    // function that takes in a letter, its button, activates gameplay
    const playRound = (letter, key) => {
        if (!isPlaying) {
            return;
        }
        if (!(key.classList.contains('guessed'))) {
            key.classList.add('guessed');
            if (word.includes(letter)) {
                // edit word display
                WordDisplay.updateDisplay(letter);
                key.style.cssText = 'background-color: #8ac284';
            } else {
                --tries;
                // edit hangman photo
                img.src = hangmans[tries];
                key.style.cssText = 'background-color: #7a7b7a';
            }
        }
        if (tries == 0) {
            isPlaying = false;
            const redirect = document.createElement('div');
            redirect.classList.add('loser');
            redirect.innerHTML = `
            <a href=../lose><button style="padding: 0.7rem 1rem; border: none; font-family: inherit; font-size: 0.8rem; color: white; background-color: #c5a3d2; font-weight: 800; border-radius: 0.7rem; width: 11.3rem;">Game Over: Click Here</button></a>
            `;
            const wordContain = document.querySelector('.word-contain');
            wordContain.appendChild(redirect);
        }
        if (WordDisplay.isGuessed()) {
            isPlaying = false;
            const redirect = document.createElement('div');
            redirect.classList.add('winner');
            redirect.innerHTML = `
            <a href=../win><button style="padding: 0.7rem 1rem; border: none; font-family: inherit; font-size: 0.8rem; color: white; background-color: #c5a3d2; font-weight: 800; border-radius: 0.7rem; width: 11.3rem;">Game Over: Click Here</button></a>
            `;
            const wordContain = document.querySelector('.word-contain');
            wordContain.appendChild(redirect);
        }
    }
    return {
        tries,
        guessedLetters,
        hangmans,
        playRound,
    }
})();