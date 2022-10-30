import json
import difflib
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        while True:
            update =  input(f"Do you mean the word: {get_close_matches(word, data.keys())[0]}? If yes, enter 'Y', otherwise, enter 'N': ")
            if update.upper() == 'Y':
                return data[get_close_matches(word, data.keys())[0]]
                break
            elif update.upper() == 'N':
                return "The word does not exist. Please double check it."
                break
            else:
                print('Looks like you did not type Y or N, please enter again.')
                continue
    else:
        return "The word does not exist. Please double check it."

word = input('Enter the word: ')
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
