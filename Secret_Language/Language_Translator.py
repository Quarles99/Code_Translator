__author__ = 'Will'

restart = 1

while restart != "x":
    word = str(input("Please input the word you would like to translate: "))

    firstLetter = word[0]
    secondLetter = word[1]
    lastLetter = word[-1:]
    secondLastLetter = word[-2]

    if len(word) > 3:
        word = word[2:-2]
        print("Here is the translation: " + secondLetter + firstLetter + word + lastLetter + secondLastLetter)

    elif len(word) == 3 or len(word) == 2:
        word = word[2:]
        print("Here is the translation: " + secondLetter + firstLetter + word)

    else:
        print(word)

    input("Press any key to translate another word again, hit x to exit.")