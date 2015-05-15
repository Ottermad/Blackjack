from card import *
from player import *
import random

# Create deck
deck = []
for suit in Card.suits:
    for name in Card.names:
        deck.append(Card(suit, name))

random.shuffle(deck)

dealt_cards = []

# Deck funtions
def random_card():
    upper_limit = len(deck) - 1
    index = random.randint(0, upper_limit)
    card = deck.pop(index)
    dealt_cards.append(card)
    return card

# Game start

# Player setup
banker = {}
charlie = {}

players = [banker, charlie]

# Deal cards
for player in players:
    card1 = random_card()
    card2 = random_card()
    player.add_card(card1)
    player.add_card(card2) 

# Player output
for player in players:
    if not player.is_banker:
        for card in player.cards: 
            print(card.full_name)
        print(player.get_score())
        # Betting
        bet = input()
        player.increment_bet(int(bet))
# Round
for player in players:
    if not player.is_banker:
        if player.has_pontoon():
            print("You have pontoon. Automatically sticking.")
        else:
            while True:
                # Output options to stick, twist, or buy.
                option = input()
                if option == "stick":
                    break
                elif option == "twist"
                    card = random_card()
                    print("{} has been dealt {}".format(player.name, card.full_name))
                    if player.is_bust():
                        print("{} is bust!".format(player.name)
                elif option == "buy":
                    bet = input()
                    player.increment_bet(bet)
                    print("{} has incremented his bet by {}.{}'s Total Bet: {}".format(player.name, bet, player.name, player.bet)
    else:
        index_of_banker = players.index(player)
 
# Banker Logic
bank = player[index_of_banker]
for card in bank.cards: 
    print("{} (banker) has {}.".format(bank.name, card.full_name))

while True:
    if bank.get_score() < 17:
        # Twist
        card = random_card()
        print("{} (banker) has been dealt {}".format(bank.name, card.full_name))
        if player.is_bust():
            print("{} (banker) is bust!".format(bank.name)
    else:
        # Stick
        print("{} (banker) sticks.".format(bank.name)
        break

# Reveal
winners = 
for player in players:
    if not player.is_banker:
        for card in player.cards: 
            print("{} has {}".format(player.name, card.full_name))
        print("{}'s total score is: {}".format(player.name, player.get_score()))
        if player.has_pontoon():
            print("{} has pontoon.".format(player.name))
        if player.is_bust():
            print("{} is bust.".format(player.name))