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
banker = Player(name="James",money=20, is_banker=True)
charlie = Player(name="Charles", money=20)

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
        bet = input("Bet: ")
        player.increment_bet(float(bet))
# Round
for player in players:
    if not player.is_banker:
        if player.has_pontoon():
            print("You have pontoon. Automatically sticking.")
        else:
            while True:
                if player.is_bust():
                    print("{} is bust!".format(player.name))
                    break
                else:
                    # Output options to stick, twist, or buy.
                    option = input("Option: ")
                    if option == "stick":
                        break
                    elif option == "twist":
                        card = random_card()
                        print("{} has been dealt {}".format(player.name, card.full_name))
                        player.add_card(card)
                        print("{}'s total score is: {}".format(player.name, player.get_score()))
                    elif option == "buy":
                        bet = input("Increment Bet By: ")
                        player.increment_bet(bet)
                        print("{} has incremented his bet by {}.{}'s Total Bet: {}".format(player.name, bet, player.name, player.bet))
                        card = random_card()
                        print("{} has been dealt {}".format(player.name, card.full_name))
                        player.add_card(card)
                        print("{}'s total score is: {}".format(player.name, player.get_score()))
    else:
        index_of_banker = players.index(player)
 
# Banker Logic
bank = players[index_of_banker]
for card in bank.cards: 
    print("{} (banker) has {}.".format(bank.name, card.full_name))

while True:
    if bank.get_score() < 17:
        # Twist
        card = random_card()
        print("{} (banker) has been dealt {}".format(bank.name, card.full_name))
        bank.add_card(card)
        if player.is_bust():
            print("{} (banker) is bust!".format(bank.name))
            break
    else:
        # Stick
        print("{} (banker) sticks.".format(bank.name))
        break

# Reveal
for player in players:
    if not player.is_banker:
        win =  False
        for card in player.cards: 
            print("{} has {}".format(player.name, card.full_name))
        print("{}'s total score is: {}".format(player.name, player.get_score()))
        if player.has_pontoon():
            print("{} has pontoon.".format(player.name))
            if not bank.has_pontoon():
                win = True
            else:
                bank_picture_card = None
                player_picture_card = None
                for card in bank.cards:
                    if card.name == "jack" or card.name == "queen" or card.name == "king":
                        bank_picture_card = card
                for card in player.cards:
                    if card.name == "jack" or card.name == "queen" or card.name == "king":
                        player_picture_card = card
                picture_card_scores = {"king": 3, "queen": 2, "jack": 1}
                if picture_card_scores[player_picture_card.name] > picture_card_scores[bank_picture_card.name]:
                    win = True
        if player.is_bust():
            print("{} is bust.".format(player.name))
        if player.get_score() > bank.get_score() and not player.is_bust():
            win = True
        if win:
            print("{} gains {}".format(player.name, player.bet))
            player.increment_money(player.bet)
        else: 
            print("{} (banker) gains {}".format(bank.name, player.bet))
            player.increment_money(-player.bet)
            bank.increment_money(player.bet)




