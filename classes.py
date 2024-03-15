# a basic class

# class TestClass:
#     test_var = "hello"
#     another_var = "ciao"

#     def test_func(self):
#         print("function in a class")
#         self.another_func(self.test_var)

#     def another_func(self, param):
#         print(f"{param} you")

# # create an instance

# test = TestClass()
# print(test.test_var, test.another_var)
# test.another_var = "bonjour"
# print(test.another_var)

# test2 = TestClass()
# print(test2.another_var)
# test2.test_func()
# test2.another_func("hola")

# mage class

# class Mage:
#     def __init__(self, health, mana):
#         self.health = health
#         self.mana = mana
#         print(f"the mage class was created with {health} health and {mana} mana")

#     def attack(self, target):
#         target.health -= 10

# class Monster:
#     health = 40

# mage = Mage(100, 200)
# monster = Monster()

# print(monster.health)
# mage.attack(monster)
# print(monster.health)

# inheritance

# class Human:
#     def __init__(self, health):
#         self.health = health
    
#     def attack(self):
#         print("attack")

# class Warrior(Human):
#     def __init__(self, health, defense):
#         super().__init__(health)
#         self.defense = defense

# class Barbarian(Human):
#     def __init__(self, health, damage):
#         super().__init__(health)
#         self.damage = damage

# warrior = Warrior(50, 5.5)
# barbarian = Barbarian(100, 8.1)
# warrior.attack()
# barbarian.attack()
# print(warrior.health)

# EXERCISE

class Entity:
    def __init__(self, damage):
        self.damage = damage

    def attack(self):
        print(f"attack! it inflicted {self.damage} damage!")


class Monster(Entity):
    def __init__(self, health, damage):
        self.health = health
        super().__init__(damage)

    def __repr__(self):
        return f"a monster with {self.health} hp."


monster = Monster(33, 2.6)
monster.attack()
print(monster)
