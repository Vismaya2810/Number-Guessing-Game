import random
from art import logo

print(logo)

def game(attempt):
    num = random.randint(1, 100)

    while attempt != 0:
        print(f"You have {attempt} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempt -= 1
        if attempt == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            print(f"The number is {num}")
        elif guess < num:
            print("Too low.")
            print("Guess again.")

        elif guess > num:
            print("Too high.")
        else:
            print(f"You got it! the answer was {num}")
            attempt = 0

print("Welcome to the Number Guessing Game!")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
    game(attempts)

elif difficulty == "hard":
    attempts = 5
    game(attempts)


else:
    print("Invalid input !!!")
