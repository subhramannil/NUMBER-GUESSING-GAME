import random

from art import logo
print(logo)

def guessgame():
    welcome = input(
        "Welcome to the Number Guessing Game!\nI am thinking a number between 1 and 100\nChoose a Difficulty. type 'easy' or 'hard': "
    )
    auto_gen = 0
    guess_u = 0
    auto_gen = random.randint(0, 100)

    if welcome == "easy":
        att = 10
        print(f"You have {att} attempts to guess the number.")
    elif welcome == "hard":
        att = 5
        print(f"You have {att} attempts to guess the number")

    while att>0:

        guess_u = int(input("Make a guess: "))

        if auto_gen > guess_u:
            att -= 1
            if att != 0:
                print("Too low.\nGuess agian.")
                print(f"You have {att} attempts remaining to guess the number")

        elif auto_gen < guess_u:
            att -= 1
            if att != 0:
                print("Too high.\nGuess again.")
                print(f"You have {att} attempts remaining to guess the number")

        else:
            print(f"You got it! the correct answer is {guess_u}")

        if att == 0:
            print("You've run out of attempts.")
            print(f"The corrct answer is {auto_gen}")
            return


guessgame()
