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
        _names[0]: 1,
        _names[1]: 2,
        _names[2]: 3,
        _names[3]: 4,
        _names[4]: 5,
        _names[5]: 6,
        _names[6]: 7,
        _names[7]: 8,
        _names[8]: 9,
        _names[9]: 10,
        _names[10]: 10,
        _names[11]: 10,
        _names[12]: 10,
    }

    def __init__(self, suit, name):
        self.suit = _suits[suit]
        self.name = name
        self.value = _values[name]
    
    def get_suit():
        return self.suit

    def get_value(is_high=False):
        value = self.value
        if is_high and self.name == _names[0]:
            value += 10
        return value
