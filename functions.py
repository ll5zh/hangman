import requests
import random
from hangman_words import word_list

# generate random word for user to guess
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
        word = random.choice(word_list)
        return word.upper()