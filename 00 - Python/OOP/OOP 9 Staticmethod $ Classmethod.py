class Hero :

    #private class variabel
    __jumlah = 0;
    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # Method ini hanya untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # Method ini tidak berlaku untukk objek tapi berlaku untuk class
    def getJumlah(self):
        return Hero.__jumlah

    # Method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

layla = Hero('layla')
print(Hero.getJumlah2())
miya = Hero('miya')
print(layla.getJumlah2())
lesley = Hero('lesley')
print(Hero.getJumlah3())