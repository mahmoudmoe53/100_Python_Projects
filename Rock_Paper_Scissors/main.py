import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = str(input("Rock, Paper, Scissors, Shoot!\n")).lower()

computer = random.randint(1, 3)

if computer == 1:
    print(f"Computer\n {rock}")
elif computer == 2:
    print(f"Computer\n {paper}")
else:
    print(f"Computer\n {scissors}")


if user == "rock":
    print(f"user\n {rock}")
    if computer == 1:
        print("It's a Tie!")
    elif computer == 2:
        print("You Lose!")
    else:
        print("You Win!")
elif user == "paper":
    print(f"user\n {paper}")
    if computer == 1:
        print("You Win!")
    elif computer == 2:
        print("It's a Tie!")
    else:
        print("You Lose!")
elif user == "scissors":
    print(f"user\n {scissors}")
    if computer == 1:
        print("You Lose!")
    elif computer == 2:
        print("You Win!")
    else:
        print("It's a Tie!")
else:
    print("Not valid. You lose!\n")