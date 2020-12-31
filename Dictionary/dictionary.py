import json
from difflib import get_close_matches

data = json.load(open("data.json"))

while(True):
    word = input("Enter the word to get deinition : ")
    word = word.lower()
    if word in data:
        print(data[word])
    elif word.upper() in data:
        print(data[word.upper()])
    elif word.title() in data:
        print(data[word.title()])
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" %
              get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no : ")
        if decide == "y":
            print(data[get_close_matches(word, data.keys())[0]])
        elif decide == "n":
            print("pugger your paw steps on wrong keys ")
        else:
            print("You have entered wrong input please enter just y or n")
    else:
        print("Not in dictionary")
    #word = input("Enter the word to get deinition : ")
