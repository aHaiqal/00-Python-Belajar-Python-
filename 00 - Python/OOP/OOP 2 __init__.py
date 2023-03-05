class Hero:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("Layla", 100, 40, 5)
hero2 = Hero("Balmond", 300, 60, 7)
hero3 = Hero("Miya", 110, 50, 6)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
