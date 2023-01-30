import random
from art import logo
from sys import exit

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def current_score(deck):
    score = sum(deck)
    return score


def get_card(users_deck, main_deck):
    new_card = random.choice(main_deck)
    if new_card == 11 and current_score(users_deck) + 11 > 21:
        new_card = 1

    users_deck.append(new_card)
    print(cards)

    return users_deck


def print_dealer(deck):
    print(f"Dealer's deck is {deck}. Dealer's score is {current_score(deck)}.")


def print_your(deck):
    print(f"Your deck is {deck}. Your score is {current_score(deck)}.")


def compare(my_deck, dealers_deck):
    if current_score(dealers_deck) == 21:
        print_your(my_deck)
        print_dealer(dealers_deck)
        return "Blackjack! Dealer wins."
    elif current_score(my_deck) == 21:
        print_your(my_deck)
        print_dealer(dealers_deck)
        return "Blackjack! You win."
    elif current_score(my_deck) > 21:
        print_your(my_deck)
        print_dealer(dealers_deck)
        return "You overreached 21. Dealer wins."
    elif current_score(dealers_deck) > 21:
        print_your(my_deck)
        print_dealer(dealers_deck)
        return "Dealer overreached 21. You win."
    elif current_score(my_deck) > current_score(dealers_deck):
        print_your(my_deck)
        print_dealer(dealers_deck)
        return "You win."
    elif current_score(my_deck) < current_score(dealers_deck):
        print_your(my_deck)
        print_dealer(dealers_deck)
        return "Dealer wins."
    elif current_score(my_deck) == current_score(dealers_deck):
        print_your(my_deck)
        print_dealer(dealers_deck)
        return "It's a draw."


def blackjack():
    my_deck = []
    dealers_deck = []

    #print(logo)

    # Beginning
    for _ in range(2):
        get_card(my_deck, cards)
        get_card(dealers_deck, cards)
    print(f"Your cards are {my_deck}. Your current score is {current_score(my_deck)}.")
    print(f"Dealer's first card is {dealers_deck[0]}.")

    if current_score(dealers_deck) == 21:
        print("Blackjack! Dealer wins.")
    elif current_score(my_deck) == 21:
        print("Blackjack! You win.")
    else:
        while current_score(my_deck) < 21:

            next_card = input("Do you want to get another card? y/n ")
            if next_card == "y":
                get_card(my_deck, cards)
                print_your(my_deck)
            else:
                break

        while current_score(dealers_deck) <= 16:
            get_card(dealers_deck, cards)

        print(compare(my_deck, dealers_deck))

    # again = input("Do you want to play again? y/n ")
    # if again == "y":
    #     blackjack()


# wanna_play = input("Do you want to play blackjack? y/n ")

while input("Do you want to play blackjack? y/n ") == "y":
    blackjack()

# if wanna_play == "y":
#     blackjack()
# else:
#     print("We won't play.")
