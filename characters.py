class Character:
    def __init__(self,health,damage,speed):
        self.health=health
        self.damage=damage
        self.speed=speed
    def take_damage(self,amount):
        self.health-=amount
    
class Warrior(Character):
     def __init__(self,health,damage,speed):
         super().__init__(health,damage,speed)
         self.damage_resistence=0.9
         self.speed_multiplier=0.2
     def take_damage(self,amount):
         damage_resisted=amount*self.damage_resistence
         super().take_damage(damage_resisted)

class Ninja(Character):
     def __init__(self,health,damage,speed):
         super().__init__(health,damage,speed)
         self.damage_resistence=0.4
         self.speed_multiplier=0.9
     def take_damage(self,amount):
         damage_resisted=amount*self.damage_resistence
         super().take_damage(damage_resisted)

w=Warrior(100,50,10)
n=Ninja(100,50,10,0.4)
w.take_damage(n.damage)
print(n.damage_resistence)
print(w.health)