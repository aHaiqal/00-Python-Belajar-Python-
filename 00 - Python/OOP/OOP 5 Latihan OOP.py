class Hero :
    def __init__(self,name,health,power,armor) :
          self.name = name
          self.health = health
          self.power = power
          self.armor = armor

    def serang(self,lawan):
        print(self.name + ' menyerang ' + lawan.name )
        lawan.diserang(self, self.power)

    def diserang(self, lawan, power_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = power_lawan/self.armor
        print('Serangan terasa ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah '+ self.name + ' tersisa '+ str(self.health))

miya = Hero('miya',90,760,19)
layla = Hero('layla',99,180,76)

miya.serang(layla)
print(10*'=')
layla.serang(miya)
     
  