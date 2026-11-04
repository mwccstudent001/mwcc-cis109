from ascii_cards import ascii_cards
import random

suits = ['♥','♦','♣','♠']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []

def get_deck():
    for suit in suits:
        for value in values:
            deck.append([value, suit])
    return deck


def display_deck():
    for card in deck:
        print(ascii_cards.display_cards([card]))


def shuffle_deck(deck):
    shuffled_deck = []
    while len(deck) > 0:
        card = random.randint(0, len(deck) - 1)
        shuffled_deck.append(deck.pop(card))
    return shuffled_deck


def play_game():
    player_score = 0
    house_score = 0
    response = 'Y'
    valid_responses = ['Y', 'N']
    while response != 'N' and player_score <= 21:
        # Player turn
        card = deck.pop()
        if card[0].isdigit():
            player_score += int(card[0])
        else:
            player_score += 10

        if player_score < 21:
            response = (input('Hit? [Y or N]: ')).upper()
        elif player_score == 21:
            print('Player wins')
        else:
            print('House wins')


get_deck()
deck = shuffle_deck(deck)
display_deck()
