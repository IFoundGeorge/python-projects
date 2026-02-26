import os
import random

while True:
    os.system('cls')

    num = random.randint(1, 10)
    ## print(num)

    print("Welcome to the Number Guessing Game!"
            " I'm thinking of a number between 1 and 10. \n")

    x = input("What number Am I thinking of? : ")

    if num == int(x):
        print("Congratulations! You guessed the number correctly! \n")
    else:
        print(f"Sorry, the correct number was {num}. Better luck next time! \n")

    # your code
    cont = input("Another one? yes/no > ")

    if cont == "no":
        print("Break")
        break

