from model.Player import Player
from model.Weapon import Weapon

knife = Weapon("Couteau", 3)
gun = Weapon("Pistolet", 5)

player1 = Player("Moodk", 50, 3)
player1.get_weapon(knife)

player2 = Player("Doomk", 20, 3)
player2.get_weapon(gun)

player1.attack_with_weapon(knife, player2)
player2.get_health()
