class Animal:

    alive= True
    def eat (self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")
class Rabbit(Animal):
    def run(self):
        print("This animal is capable of running")
class Fish(Animal):
    def swim(self):
        print("This animal is capable of swimming")
class Hawk(Animal):
    def fly(self):
        print("This animal is capable if flying") 


r=Rabbit()
f=Fish()
h=Hawk()

print(f.alive)
print(h.alive)
print(r.alive)
h.fly()
r.run()
f.swim()
