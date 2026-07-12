# Inheritance = allows a class inherit attributs  and method from another class 
# helps with code reusability and extensibility 
# class child ( parent )

class Animal:
    def __init__(self,name):   # constructor -> use to assign attribut
        self.name = name 
        self.isalive=True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep (self):
        print(f"{self.name} is sleeping")
class Dog(Animal):
    def speak(helf):
        print("woof!")
class Cat(Animal):
    def speak(abc):
        print("meow!")
class mouse(Animal):
    def speak(anything):
        print("chick!")

dog = Dog("schooby")
cat = Cat("Grafield")
mous= mouse("mikky")


print(dog.name)
print(dog.isalive)
dog.eat()
dog.sleep()
print()
dog.speak()
cat.speak()
mous.speak()
print()
print(cat.name)
print(cat.isalive)
cat.eat()
cat.sleep()

print(mous.name)
print(mous.isalive)
mous.eat()
mous.sleep()