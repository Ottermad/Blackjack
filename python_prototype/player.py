class Player:
    def __init__(self, name, is_banker=False):
        self.name = name
        self.is_banker = is_banker
        self.cards = []
        self.bet = 0
    
    def add_card(self, card):
        self.cards.append(card)
    
    def has_pontoon(self):
        if len(self.cards) == 2:
            if bool(Card.names[10:13] in self.cards[0].name) != bool(Card.names[10:13] in self.cards[1].name):
                if bool(Card.names[0] in self.cards[0].name) != bool(Card.names[0] in self.cards.[1].name):
                    return True
        return False
    
    def get_score(self):
        aces = []
        for card in self.cards:
            if card.name == "ace":
                aces.append(card)
            else:
                score += card.get_value()
        return score
    
    def is_bust(self):
        if self.get_score() > 21:
            return True
        else:
            return False
 
    def increment_bet(self, increment):
        self.bet += increment
    
    def reset_bet(self):
        self.bet = 0
