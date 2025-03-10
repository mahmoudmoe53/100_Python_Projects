from art import *
from game_data import *
import random

print(logo)

score = 0

celeb_a = data[random.randint(0, 49)]


def more_followers(person1, person2):
    """This function checks to see which celebrity has the higher follower count"""
    if person1["follower_count"] > person2["follower_count"]:
        return "A"
    else:
        return "B"


while True:

    celeb_b = data[random.randint(0, 50)]

    print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']}, from {celeb_a['country']}\n")

    print(vs)

    print(f"Compare B: {celeb_b['name']}, a {celeb_b['description']}, from {celeb_b['country']}")


    guess = input("Who has more followers? Type 'A' or  'B':\n").upper()

    print("\n" * 20)

    print(logo)

    if guess == more_followers(celeb_a, celeb_b):
        print("Well done")
        score += 1
        if more_followers(celeb_a, celeb_b) == "A":
            celeb_a = celeb_a
        else:
            celeb_a = celeb_b
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        break