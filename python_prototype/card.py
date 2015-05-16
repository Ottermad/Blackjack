class Card:
    
    suits = ["hearts", "diamonds", "spades", "clubs"]
    names = [
        "ace",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "jack",
        "queen",
        "king",
    ]
    _values = {
        names[0]: 1,
        names[1]: 2,
        names[2]: 3,
        names[3]: 4,
        names[4]: 5,
        names[5]: 6,
        names[6]: 7,
        names[7]: 8,
        names[8]: 9,
        names[9]: 10,
        names[10]: 10,
        names[11]: 10,
        names[12]: 10,
    }

    def __init__(self, suit, name):
        self.suit = suit 
        self.name = name
        self.value = self._values[name]
        self.full_name = "{} Of {}".format(name,suit)
    
    def get_suit(self):
        return self.suit

    def get_value(self, is_high=False):
        value = self.value
        if is_high and self.name == self.names[0]:
            value += 10
        return value
