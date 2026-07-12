# multiple inheritance = inherit from more then one parent class
               # c(a,b) -> c class inherit from class a and b both parent
# multilevel inheritance = inherit from a parent which inherit's from another parent
              # c(b)<-b(a)<-a   // a is tha grandparent so b inherit a and c inherit both b and a.
        # a parent can inherit from  another parent.
class animal():
    def eat(self): 
        print("This animal is eating")
class prey(animal):
    def flee(self):
        print("This animal is fleeing")
class predator(animal):
    def hunt(self):
        print("This animal is hunting")

class rabbit(prey):
    pass
class hawk(predator):
    pass
class fish(prey,predator):
    pass

rbit= rabbit()
hk= hawk()
fsh= fish()


rbit.flee()
hk.hunt()
fsh.flee()
fsh.hunt()

print()

rbit.eat()
hk.eat()
fsh.eat()

