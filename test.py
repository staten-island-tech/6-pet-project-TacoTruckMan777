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
        self.inventory = [Battle Axe, Large Leather Shield]
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
        self.inventory = [Great Knife, Shortbow, Buckler, Bone Arrow -Fletched-]
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
        self.inventory = [Short Sword, Astrologers Staff, Scripture Wooden Shield, Glintstone Pebble, Glintstone Arc]
        self.Vigor = 9
        self.Mind = 15
        self.Endurance = 9
        self.Strength = 8
        self.Dex = 12
        self.IQ = 16
        self.Faith = 7
        self.Arcane = 9

class Warrior(Player):
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = [Scimitar, Scimitar, Riveted Wooden Shield]
        self.Vigor = 11
        self.Mind = 12
        self.Endurance = 11
        self.Strength = 10
        self.Dex = 16
        self.IQ = 10
        self.Faith = 8
        self.Arcane = 9

class Prisoner(Player):
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = [Glintstone Staff, Estoc, Rift Shield, Magic Glintblade]
        self.Vigor = 11
        self.Mind = 12
        self.Endurance = 11
        self.Strength = 11
        self.Dex = 14
        self.IQ = 14
        self.Faith = 6
        self.Arcane = 9

class Confessor(Player):
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = [Broadsword, Blue Crest Heater Shield, Finger Seal, Urgent Heal, Assassins Approach]
        self.Vigor = 10
        self.Mind = 13
        self.Endurance = 10
        self.Strength = 12
        self.Dex = 12
        self.IQ = 9
        self.Faith = 14
        self.Arcane = 9
    
class Wretch(Player):
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = [Club, air, atom]
        self.Vigor = 10
        self.Mind = 10
        self.Endurance = 10
        self.Strength = 10
        self.Dex = 10
        self.IQ = 10
        self.Faith = 10
        self.Arcane = 10
    
class Vagabond(Player):
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = inventory
        self.Vigor = 15
        self.Mind = 10
        self.Endurance = 11
        self.Strength = 14
        self.Dex = 13
        self.IQ = 9
        self.Faith = 9
        self.Arcane = 7

class Prophet(Player):
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = inventory
        self.Vigor = 10
        self.Mind = 14
        self.Endurance = 8
        self.Strength = 11
        self.Dex = 10
        self.IQ = 7
        self.Faith = 16
        self.Arcane = 10
    
class Samurai(Player):
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = inventory
        self.Vigor = 12
        self.Mind = 11
        self.Endurance = 13
        self.Strength = 12
        self.Dex = 15
        self.IQ = 9
        self.Faith = 8
        self.Arcane = 8

class HeavyKnight(Player):
    def __init__(self, name, Runes, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = 500
        self.inventory = inventory
        self.Vigor = 14
        self.Mind = 7
        self.Endurance = 17
        self.Strength = 15
        self.Dex = 11
        self.IQ = 7
        self.Faith = 7
        self.Arcane = 10
    
    