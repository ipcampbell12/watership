
""" Module  Contains Rabbit CLass and Rabbit Objects"""

all_rabbits = []


class Rabbit:
    def __init__(self, name, strength, cleverness, courage, charisma, kindness, hp, influence):
        self.name = name
        self.strength = strength
        self.cleverness = cleverness
        self.courage = courage
        self.charisma = charisma
        self.kindness = kindness
        self.hp = hp
        self.influence = influence
        all_rabbits.append(self)

    def show_stats(self):
        print(f"Here are the stas for: {self.name}")
        print(f"Strength: {self.strength}")
        print(f"Cleverness: {self.cleverness}")
        print(f"Courage: {self.courage}")
        print(f"Charisma: {self.charisma}")
        print(f"Kindness: {self.kindness}")
        print(f"Health: {self.hp}")
        print(f"Influence: {self.influence}")

    def change_hp(self, change):
        self.hp += change
        if change < 0:
            my_text = f'{self.name} has decreased to {self.hp} health points'
            x = my_text.center(20, " ")
            print(x)
        else:
            my_text = f'{self.name} has increased to {self.hp} health points'
            x = my_text.center(20, " ")
            print(x)

    def change_strength(self, change):
        self.strength += change
        if change < 0:
            my_text = f'{self.name} has decreased to {self.strength} strength points'
            x = my_text.center(20, " ")
            print(x)
        else:
            my_text = f'{self.name} has increased to {self.strength} strength points'
            x = my_text.center(20, " ")
            print(x)

    def change_cleverness(self, change):
        self.cleverness += change
        if change < 0:
            my_text = f'{self.name} has decreased to {self.cleverness} cleverness points'
            x = my_text.center(20, " ")
            print(x)
        else:
            my_text = f'{self.name} has increased to {self.cleverness} cleverness points'
            x = my_text.center(20, " ")
            print(x)

    def change_courage(self, change):
        self.courage += change
        if change < 0:
            my_text = f'{self.name} has decreased to {self.courage} courage points'
            x = my_text.center(20, " ")
            print(x)
        else:
            my_text = f'{self.name} has increased to {self.courage} courage points'
            x = my_text.center(20, " ")
            print(x)

    def change_charisma(self, change):
        self.charisma += change
        if change < 0:
            my_text = f'{self.name} has decreased to {self.charisma} charisma points'
            x = my_text.center(20, " ")
            print(x)
        else:
            my_text = f'{self.name} has increased to {self.charisma} charisma points'
            x = my_text.center(20, " ")
            print(x)

    def change_kindness(self, change):
        self.kindness += change
        if change < 0:
            my_text = f'{self.name} has decreased to {self.kindness} kindness points'
            x = my_text.center(20, " ")
            print(x)
        else:
            my_text = f'{self.name} has increased to {self.kindness} kindness points'
            x = my_text.center(20, " ")
            print(x)

    def change_influence(self, change):
        self.influence += change
        if change < 0:
            my_text = f'{self.name} has decreased to {self.influence} influence points'
            x = my_text.center(20, " ")
            print(x)
        else:
            my_text = f'{self.name} has increased to {self.influence} influence points'
            x = my_text.center(20, " ")
            print(x)

    def cuff(self, enemy):
        total_damage = 5 + self.strength
        enemy.hp -= total_damage
        print(f"{self.name} cuffed {enemy.name} in the head!")
        print(f"{enemy.name} has reduced to {enemy.hp} health points")

    def crush(self, enemy):
        total_damage = 12 + self.strength
        enemy.hp -= total_damage
        print(f"{self.name} tried crush {enemy.name} with his body weight!")
        print(f"{enemy.name} has reduced to {enemy.hp} health points")

    def scratch(self, enemy):
        total_damage = 4 + self.strength
        enemy.hp -= total_damage
        print(f"{self.name} scratched {enemy.name} acrosss the face!")
        print(f"{enemy.name} has reduced to {enemy.hp} health points")

    def bite(self, enemy):
        total_damage = 8 + self.strength
        enemy.hp -= total_damage
        print(f"{self.name} bit {enemy.name} in the shoulder!")
        print(f"{enemy.name} has reduced to {enemy.hp} health points")


bigwig = Rabbit("Bigwig", 7, 3, 6, 4, 2, 100, 50)

hazel = Rabbit("Hazel", 4, 6, 5, 7, 5, 80, 80)

fiver = Rabbit("Fiver", 2, 7, 5, 5, 6, 50, 80)

woundwort = Rabbit("The General", 9, 9, 5, 8, 0, 120, 90)


# print(bigwig.show_stats())
# print(hazel.show_stats())
# print(fiver.show_stats())
