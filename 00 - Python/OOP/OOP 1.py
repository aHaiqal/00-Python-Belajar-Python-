class Hero:
    pass

hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = "Layla"
hero1.health = 100

hero2.name = "Balmond"
hero2.health = 190

hero3.name = "Miya"
hero3.health = 110

print(hero1)
print(hero1.__dict__)
print(hero1.name)
print(hero1.health)