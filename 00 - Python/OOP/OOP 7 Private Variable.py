class Hero :
    # class variabel
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health
        # variabel instance private
        self.__private = 'Private'
        # variabe; instance protected
        self._protected = 'Protected'

lesley = Hero("Lesley",90)
print(lesley.__dict__)
print(lesley._protected)
print(Hero.__privateJumlah)
