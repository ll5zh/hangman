import requests
import random
from hangman_words import word_list

# generate random word for user to guess
# def get_word(list):
#    word = random.choice(list)
#    return word.upper()
def get_word(category):
    api_url = "https://api.api-ninjas.com/v1/randomword?type=" + category
    response = requests.get(api_url, headers={'X-Api-Key': 'YQO2nUQrfI2ukzfAATOklw==f9q5FyhXvpBQC0mB'})
    if response.status_code == requests.codes.ok:
        retval = response.text
        length = len(retval)
        last = length - 2
        word = retval[10:last]
        return word.upper()
    # if api request fails, return word from word list
    else:
        word = random.choice(list)
        if (category != ""):
            print("At the moment, we cannot get a specific noun/adjective/verb for you. Enjoy playing Hangman with a randomized word!")
        return word.upper()

# consumes list of characters and the guessed letter. produces string with guessed letter appearing
# edit_word_as_list(list, letters) takes in a list of characters (spelling the word) and a list of correctly guessed letters
# it returns a new string representing the word in progress (displayed guessed letters, blanks in place of unguessed letters)
def edit_word_as_list(list, letters):
    new_list = []
    for element in list:
        if element in letters:
            new_list = new_list + [element]
        else:
            new_list = new_list + ["_"]
    return " ".join(new_list)

# introduce() runs the game introduction and allows users to choose word specifications
def introduce(is_new):
    if (is_new):
        print("Welcome to Hangman!")
    response = input("Press [i] to get instructions on how to play Hangman.\nPress [n] to play Hangman with a noun.\nPress [a] to play Hangman with an adjective.\nPress [v] to play Hangman with a verb.\nPress any other key to play with a random word! ").lower()
    if response == "i":
        print_instructions()
    elif response == "n":
        word = get_word("noun")
        play(word)
    elif response == "a":
        word = get_word("adjective")
        play(word)
    elif response == "v":
        word = get_word("verb")
        play(word)
    else:
        word = get_word("")
        play(word)


# print_instructions() displays the instructions to play hangman
def print_instructions():
    print("\nYou need to guess the hidden word before you end up hanging the Hangman! Guess letters in the word one by one - if you guess correctly, instances of that letter in the word will reveal themselves. If you guess incorrectly, the man will be one step closer to being hung... You have a maximum of 6 incorrect guesses!\n")
    introduce(False)

# play(word) runs the hangman game with the passed word
def play(word):
    
    word_progress = "_ " * len(word)
    guessed = False
    guessed_letters = []
    guessed_letters_correct = []
    guessed_words = []
    tries = 6

    # game introduction
    print("\nGood luck!")
    print(display_hangman(tries))
    print(word_progress)
    print("\n")

    # game is running
    while not guessed and tries > 0:

        guess = input("Enter your guess (letter or word): ").upper()
        
        # guessed a letter
        if len(guess) == 1 and guess.isalpha():

            # letter was guessed already
            if guess in guessed_letters: 
                print("You already guessed the letter " + guess + "!")
            
            # letter is not in the word
            elif guess not in word:
                print("The letter " + guess + " is not in the word...")
                tries -= 1
                guessed_letters.append(guess)
            
            # letter is in the word
            else:
                print("Yay, the letter " + guess + " is in the word!")
                guessed_letters.append(guess)
                guessed_letters_correct.append(guess)
                word_progress = edit_word_as_list(list(word), guessed_letters_correct)
                if "_ " not in word_progress:
                    guessed = True

        # guessed a word
        elif len(guess) == len(word) and guess.isalpha():

            # word was guessed already
            if guess in guessed_words:
                print("You already guessed the word " + guess + "!")
            
            # word is incorrect
            elif guess != word:
                print("Sorry, " + guess + " is not the word.")
                guessed_words.append(guess)
                tries -= 1
            
            # word is correct
            else:
                guessed = True
                word_progress = word

        # guess is invalid
        else:
            print("That's not a valid guess...")
        
        # after each guess is processed, print hangman and progress of word
        print(display_hangman(tries))
        print(word_progress)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word!")
    
    else:
        print("Sorry, you ran out of tries. The word was " + word + ".")
     

# hangman states
def display_hangman(tries):
    stages = [
        """
                --------
                |      |
                |      O
                |     \ | /
                |       |
                |     _/ \_
               ---
        """,
        """
                --------
                |      |
                |      O
                |     \ | /
                |       |
                |     _/ 
               ---
        """,
        """
                --------
                |      |
                |      O
                |     \ | /
                |       |
                |     
               ---
        """,
        """
                --------
                |      |
                |      O
                |     \ | 
                |       
                |     
               ---
        """,
        """
                --------
                |      |
                |      O
                |      | 
                |       
                |     
               ---
        """,
        """
                --------
                |      |
                |      O
                |     
                |       
                |     
               ---
        """,
        """
                --------
                |      |
                |      
                |     
                |       
                |     
               ---
        """,
    ]

    return stages[tries]

# run game
introduce(True)
