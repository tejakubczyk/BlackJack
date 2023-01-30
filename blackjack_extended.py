import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def current_score(deck):
    score = sum(deck)
    return score


def get_card(users_deck, main_deck):
    #print(cards)
    new_card = random.choice(main_deck)
    #print(new_card)

    new_card_position = cards.index(new_card)
    #print(new_card_position)

    cards.pop(new_card_position)
    #print(cards)

    if new_card == 11 and current_score(users_deck) + 11 > 21:
        new_card = 1

    users_deck.append(new_card)

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


def another_card(deck, cards, answear):
    #next_card = input("Do you want to get another card? y/n ")
    if answear == "y":
        get_card(deck, cards)
        print_your(deck)
    elif answear != "n":
        print("Error. Wrong typing.")
        another_card(deck, cards)


def play_again():
    again = input("Do you want to play again? y/n ")
    if again == "y":
        blackjack()
    elif again == "n":
        print("Bye!")
    else:
        print("Error. Wrong typing.")
        play_again()


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
                another_card(my_deck, cards, "y")
            elif next_card == "n":
                break
            else:
                print("Error. Wrong typing.")
                another_card(my_deck, cards, "n")

        while current_score(dealers_deck) <= 16:
            get_card(dealers_deck, cards)

        print(compare(my_deck, dealers_deck))

        play_again()


def play_game():
    wanna_play = input("Do you want to play blackjack? y/n ")
    if wanna_play == "y":
        blackjack()
    elif wanna_play == "n":
        print("We won't play.")
    else:
        print("Error. Wrong typing.")
        play_game()


play_game()
