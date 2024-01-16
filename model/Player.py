from model.Weapon import Weapon


class Player:

    def __init__(self, pseudo: str, health: int, attack: int):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue ", pseudo, "/ Point de vie: ", health, "/ Point attack:", attack)

    def get_health(self):
        return self.health

    def get_pseudo(self):
        return self.pseudo

    def get_attack(self):
        return self.attack

    def get_weapon(self, weapon: Weapon):
        self.weapon = weapon.name
        return print(self.pseudo, "a un", weapon.name)

    def damage(self, damage: int):
        self.health -= damage
        return self.health

    def attack_player(self, target_player):
        target_player.damage(self.attack)

    def attack_with_weapon(self, weapon: Weapon, target_player):
        self.attack += weapon.damage
        target_player.damage(self.attack)
