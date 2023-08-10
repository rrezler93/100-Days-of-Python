class Enemy:
    def __init__(self, name, health, damage):
        self.health = health
        self.name = name
        self.damage = damage

    def display_stats(self):
        print(f"**********************\n"
              f"Name: {self.name}\n"
              f"Health: {self.health}\n"
              f"Damage: {self.damage}\n"
              f"**********************")


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strong = 15
        self.weapon = "Fists"

    def display_stats(self):
        print(f"**********************\n"
              f"Name: {self.name}\n"
              f"Health: {self.health}\n"
              f"Weapon: {self.weapon}\n"
              f"**********************")

    def slash(self, enemy):
        print("Attack!")
        if self.weapon != "Fists":
            damage = (self.strong / 2) + self.weapon.damage
            enemy.health -= damage
        else:
            damage = self.strong / 2
            enemy.health -= damage
        print(f"You hit the {enemy.name} for {damage}.")

    def pick(self, weapon):
        print(f"Your new weapon is: {weapon.name}.")
        self.weapon = weapon


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Potion:
    def __init__(self, strong, effect):
        self.strong = strong
        self.effect = effect

    def use(self, character):
        if self.effect == "heal":
            character.health += self.strong
        elif self.effect == "poison":
            character.health -= self.strong


troll = Enemy(name="Troll", health=100, damage=20)
player = Player("Mordrag")
knife = Weapon(name="Knife", damage=15)
health_potion = Potion(strong=10, effect="heal")


# # Use potion:
#
# player.display_stats()
# health_potion.use(player)
# player.display_stats()

# # Attack (no weapon):
# #
# troll.display_stats()
# player.slash(troll)
# troll.display_stats()

# # Attack with weapon:
# #
# player.pick(knife)
# player.slash(troll)
# troll.display_stats()




