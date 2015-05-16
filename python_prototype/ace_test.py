from card import Card
from player import Player

tester = Player(name="tester", money=20)

ace = Card(suit=Card.suits[0], name=Card.names[0])
king = Card(suit=Card.suits[0], name=Card.names[12])

tester.add_card(ace)
tester.add_card(king)

print(tester.get_score())
