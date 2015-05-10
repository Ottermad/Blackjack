from card import *
import random

# Create deck
deck = []
for suit in Card.suits:
    for name in Card.names:
        deck.append(Card(suit, name))

random.shuffle(deck)

dealt_cards = []

# Game start

# Player setup
banker = {}
charlie = {}

players = [banker, charlie]

# Deal cards
for player in players:
    random.randint(0, r



