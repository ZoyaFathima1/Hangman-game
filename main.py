import random
from  Hangman_Art import *
from User_message import message
placeholder = ""
print(hangman_art)

word_selected = random.choice(words)
print(word_selected)
length=len(word_selected)
for i in range(length) :
    placeholder+="_"
print(placeholder)
correct_letter = []

lives=6
game_over = False
while not game_over :
    print(f" You have {lives} lives left")
    guess = input("Choose any letter")
    if guess in correct_letter :
        print(f"You have already guessed {guess}")

    display = ""
    for i in word_selected :
      if i == guess :
        display += guess
        correct_letter.append(guess)
        print(random.choice(message))
      elif i in correct_letter:
          display += i
      else :
        display += "_"
    print(display)


    if guess not in word_selected:
      print(f"You guessed {guess} . Sorry ! You lose a life")
      lives = lives - 1
      if lives == 0:
          print(f"-----------------------It was {word_selected}. Sorry You Lose -----------------------")
          game_over = True
    if "_" not in placeholder:
      print(" ----------------------- you won -----------------------")
      game_over = True

    print(stages[6-lives])
