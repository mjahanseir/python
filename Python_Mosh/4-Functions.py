#  1- Defining Functions
def greet():
    print("Hi there")
    print("Welcome abroad")


greet()


#  2- Arguments

def greet(fname, lname):
    print(f"Hi {fname}  {lname}")


greet("Mo", "Jahan")
greet("John", "Smith")


#  3- Types of Functions

def greeting(name):
    return f"Hi {name}"


print(greeting("Mo"))
print(greet("Mo", "jahan"))

#  4- Keyword Arguments


def increment(number, by=1):
    return number + by


print(increment(number=3, by=2))


#  5- Default Arguments

print(increment(2))

#  6- xargs


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5, 6, 7))


#  7- xxargs

def save_user(**users):
    print(users)
    print(users["id"])
    print(users["name"])


save_user(id=1, name="John", age=33)


#  8- Scope
def scope(name):
    message = "a"


def send_email(name):
    message = "b"


#  9- Debugging

def sum(*numbers):
    total = 0
    for number in numbers:
        total += number

    return total


print("Start")
print(sum(1, 2, 3))


#  10- VSCode Coding Tricks - Windows

# alt+up/down moveup and down
# shift+alt+down duplicate


#  11- VSCode Coding Tricks - Mac


#  12- Exercise


#  13- Solution
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fiz buzz"
    elif input % 3 == 0:
        return "fiz"
    elif input % 5 == 0:
        return "buzz"
    else:
        return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
