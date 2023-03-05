class Hero:

    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    # Getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # Setter
    def diserang(self,damage):
        self.__health -= damage

    def setAttPower(self,nilaibaru):
        self.__attPower = nilaibaru

# Awal game
guinnevere = Hero('Guinnevere',100,40)

# Game Berjalan
print(guinnevere.getName())
print(guinnevere.getHealth())
guinnevere.diserang(20)
print(guinnevere.getHealth())