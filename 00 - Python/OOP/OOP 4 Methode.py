from turtle import up


class Hero:
    # class variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    # void function, methode tanpa return, tanpa argumen
    def siapa(self):
        print("Namaku adalah = "+ self.name)

    # method dengan argumen tanpa return
    def healthUp(self,up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero('Sniper', 100, 90, 20)
hero2 = Hero('Atam', 80, 88, 18)

hero1.siapa()
hero1.healthUp(20)

print(hero1.getHealth())