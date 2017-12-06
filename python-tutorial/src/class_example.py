class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

class Dog:

    kind = 'canine'          # class variable shared by all instances

    def __init__(self, name):
        self.name = name     # instance variable unique to each instance

def hello_class():
    x = MyClass()
    # x.f is a method object
    # can be stored away anc called at a later time
    xf = x.f
    print xf()

class MistakenDog():

    tricks = [] # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

class CorrectDog():

    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list fo each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

def hello_dog():
    d = Dog('Fido')
    e = Dog('Buddy')
    print d.kind
    print e.kind
    print d.name
    print e.name

def wrong_dog():
    d = MistakenDog('Buddy')
    e = MistakenDog('Fido')
    d.add_trick('roll over')
    e.add_trick('play dead')

    print d.tricks

def correct_dog():
    d = CorrectDog('Buffee')
    e = CorrectDog('Mug')
    d.add_trick('roll over')
    e.add_trick('play dead')

    print d.tricks
    print e.tricks

if __name__ == '__main__':
    # hello_class()
    # hello_dog()
    # wrong_dog()
    correct_dog()
