import random
words = ["kilo","below","hello","dish","drum"]
word_selected = random.choice(words)
letter = input("choose a letter")
for i in word_selected:
    if i == letter :
        print("true")
    else :
        print("false")
print("the chosen word was",word_selected)