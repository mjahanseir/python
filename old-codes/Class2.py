
class Parent:
    def __init__ (self):
        print("This is the PARENT class")

    def parentFunc(self):
        print("This is the PARENT function")


p = Parent()
p.parentFunc()

class Child(Parent):
    def __init__(self):
        print("This is the CHILD class")

    def childFunc(self):
        print("This is the CHILD function")


c = Child()
c.childFunc()
c.parentFunc()

