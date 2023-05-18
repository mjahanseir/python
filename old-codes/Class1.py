# class Person:
#     def getName(self):
#         print("mo")
#
#     def getAge(self):
#         print("30")
#
#
# p = Person()
# p.getName()
# p.getAge()


class Person:
    def __init__ (self ,name , age):
        self.name = name
        self.age = age

    def getName(self):
        print("your name is "+ self.name)

    def getAge(self):
        print("your age is " + self.age)


p = Person("Mo", "22")
p.getName()
p.getAge()

