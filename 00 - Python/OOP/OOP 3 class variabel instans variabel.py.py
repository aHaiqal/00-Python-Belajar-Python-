class Hero: #template
    # class variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Hero dengan nama : "+ inputName)


hero1 = Hero("Layla", 100, 40, 5)
print(Hero.jumlah)
hero2 = Hero("Balmond", 300, 60, 7)
print(Hero.jumlah)
hero3 = Hero("Miya", 110, 50, 6)
print(Hero.jumlah)


