import requests

# --- Elden Ring API helper (optional for now) ---

def get_weapon_name():
    url = "https://eldenring.fanapis.com/api/weapons?limit=1"
    response = requests.get(url)
    if response.status_code != 200:
        return "Basic Sword"
    data = response.json()
    return data["data"][0]["name"]


# --- Core player classes ---

class Player:
    def __init__(self, name, max_hp, strength, dex, iq, faith, arcane, weapon_name="Fists"):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.dex = dex
        self.iq = iq
        self.faith = faith
        self.arcane = arcane
        self.weapon_name = weapon_name

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

    def basic_attack_damage(self):
        # Simple damage formula you can tweak
        return self.strength + self.dex // 2


class Hero(Player):
    def __init__(self, name="Hero"):
        super().__init__(
            name=name,
            max_hp=100,
            strength=16,
            dex=9,
            iq=7,
            faith=8,
            arcane=11,
            weapon_name="Hero Sword"
        )


class Bandit(Player):
    def __init__(self, name="Bandit"):
        super().__init__(
            name=name,
            max_hp=85,
            strength=9,
            dex=13,
            iq=9,
            faith=8,
            arcane=14,
            weapon_name="Great Knife"
        )
