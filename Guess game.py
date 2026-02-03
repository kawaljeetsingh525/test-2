# Make a game in python where we guess the numbers
import random

print("Welcome to the guessing game")
print("Guess a number between 1 and 100")

secret_number = random.randint(1, 100)
max_attempts = 8

attempts = 0

while attempts < max_attempts:
    user_guess = int(input("Enter your guess: "))
    attempts += 1

    if user_guess > secret_number:
        print("Too high")
    elif user_guess < secret_number:
        print("Too low")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
else:
    print(f"Out of attempts! The number was {secret_number}")
