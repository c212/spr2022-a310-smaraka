class Creature:
    # super class
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is",self.name,"and I am Creature.")

a = Creature("Micheal")
a.speak()

class Dog(Creature):
# subclass of creature
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("My name is",self.name,"and I am Dog: Woof.")

b = Dog("Bob")
b.speak()

class Cow(Creature):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("My name is",self.name,"and I am Cow: Moo.")

c = Cow("Jimmy")
c.speak()