import random
from hangman_words import word_list

# generate random word for user to guess
def get_word(list):
    word = random.choice(list)
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

# play(word) runs the hangman game with the passed word
def play(word):
    
    word_progress = "_ " * len(word)
    guessed = False
    guessed_letters = []
    guessed_letters_correct = []
    guessed_words = []
    tries = 6

    # game introduction
    print("Welcome to Hangman!")
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
play(get_word(word_list))
