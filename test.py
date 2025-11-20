class Player:
    def __init__(self, name, Runes, StartingClass, inventory, Vigor, Mind, Endurance, Strength, Dex, IQ, Faith, Arcane ):
        self.name = name
        self.Runes = Runes
        self.inventory = inventory
        self.StartingClass = StartingClass
        self.Vigor = Vigor
        self.Mind = Mind
        self.Endurance = Endurance
        self.Strength = Strength
        self.Dex = Dex
        self.IQ = IQ
        self.Faith = Faith
        self.Arcane = Arcane
        
    def StartingClass(Hero, Bandit, Astrologer, Warrior, Prisoner, Confessor, Wretch, Vagabond, Prophet, Samurai, Heavy Knight):
        