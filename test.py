class Player:
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = inventory
        self.Vigor = Vigor
        self.Mind = Mind
        self.Endurance = Endurance
        self.Strength = Strength
        self.Dex = Dex
        self.IQ = IQ
        self.Faith = Faith
        self.Arcane = Arcane

class Hero(Player):
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = inventory
        self.Vigor = 14
        self.Mind = 9
        self.Endurance = 12
        self.Strength = 16
        self.Dex = 9
        self.IQ = 7
        self.Faith = 8
        self.Arcane = 11

class Bandit(Player):
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = inventory
        self.Vigor = 10
        self.Mind = 11
        self.Endurance = 10
        self.Strength = 9
        self.Dex = 13
        self.IQ = 9
        self.Faith = 8
        self.Arcane = 14
    
class Astrologer(Player):
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = inventory
        self.Vigor = 9
        self.Mind = 15
        self.Endurance = 9
        self.Strength = 8
        self.Dex = 12
        self.IQ = 16
        self.Faith = 7
        self.Arcane = 9
    
    