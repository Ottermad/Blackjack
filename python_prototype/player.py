from card import Card

class Player:
    def __init__(self, name, money, is_banker=False):
        self.name = name
        self.is_banker = is_banker
        self.cards = []
        self.bet = 0
        self.money = money
    
    def add_card(self, card):
        self.cards.append(card)
    
    def has_pontoon(self):
        if len(self.cards) == 2:
            if bool(self.cards[0].name in Card.names[10:13])  != bool(self.cards[1].name in Card.names[10:13]):
                if bool(self.cards[0].name in Card.names[0]) != bool(self.cards[1].name in Card.names[0]):
                    return True
        return False
    
    def get_score(self):
        aces = []
        score = 0
        for card in self.cards:
            if card.name == "ace":
                aces.append(card)
            else:
                score += card.get_value() # 10
        if len(aces) > 0:
            possible = 21 - score # 21 - 10 = 11
            possible = possible // 11 # 21 // 11 = 1
            left_over = len(aces) - possible # 1 - 1 = 0
            for num in range(0, possible):
                score += aces[num].get_value(is_high=True)
            for num in range(0, left_over):
                score += aces[num].get_value()
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
    
    def increment_money(self, increment):
        self.money += increment
