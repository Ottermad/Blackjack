class Player:
    def __init__(self, name, is_banker=False):
        self.name = name
        self.is_banker = is_banker
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def has_pontoon(self):
        if len(self.cards) == 2:
            if bool(Card.names[10:13] in self.cards[0]) != bool(Card.names[10:13] in self.cards[1]):
                if bool(
                 
