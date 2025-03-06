from art import *
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def hit():
    player.append(random.choice(cards))
    dealer.append(random.choice(cards))

    print(f"Your cards: {player} current score: {sum(player)}")
    print(f"Computer's first card: {dealer[0]}")
    return input("Type 'y' to get another card, type 'n' to pass\n").lower()


print(logo)
game = True

player = []
dealer = []

play = input("Do you want to play a game of BlackJack? 'y', or 'n'?\n").lower()

while game:
    if play == "y":

        hit()


        while True:
            decision = hit()
            if decision == "y":
                hit()
            elif decision == "n":
                break


        player_score = sum(player)
        dealer_score = sum(dealer)


        while dealer_score < 17:
            dealer.append(random.choice(cards))
            dealer_score = sum(dealer)

        print(f"Your final score: {player_score}")
        print(f"Dealer's final score: {dealer_score}")

        if player_score > dealer_score and player_score <= 21:
            print(f"You win with a score of {player_score}! The dealer had {dealer_score}")
        elif dealer_score > player_score and dealer_score <= 21:
            print(f"The dealer wins with a score of {dealer_score}. Your score was {player_score}")
        elif player_score > 21:
            print(f"You went over 21 with a score of {player_score}. The dealer wins!")
        elif dealer_score > 21:
            print(f"The dealer went over 21 with a score of {dealer_score}. You win!")

        game = False
    elif play == "n":
        print("Goodbye!")
        game = False
