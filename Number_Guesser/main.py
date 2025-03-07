from art import *
import random

print(logo)

print("Welcome to the Number Guessing Game!\n")

print("Im thinking of a number between 1 and 100.\n")


chosen_number = random.randint(1, 100)


def easy():
    choice = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
    count = 0
    if choice == "easy":
        count += 10
    elif choice == "hard":
        count += 5
    for i in range(count):
        print(f"You have {count} attempts remaining to guess the number.\n")
        guess = int(input("Make a guess:\n"))
        if guess == chosen_number:
            print(f"Congratulations!! You've guessed the correct number {chosen_number}")
            print(win)
            return
        elif guess > chosen_number:
            print(f"Too high")
            count -= 1
        elif guess < chosen_number:
            print(f"Too low")
            count -= 1
        if count == 0:
            print(f"You are out of guesses! the correct number was {chosen_number}")
            return


easy()
