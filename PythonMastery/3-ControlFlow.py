print(10 > 3)
print(10 >= 3)
print(10 < 3)
print(10 <= 3)
print(10 == 3)
print(10 == "3")
print(10 != 3)

print("+++++++++++++++++++++++++++++++++++++++++++++")

print(ord("B"))


temp = 15
if temp > 30:
    print("warm")
    print("drink water")
elif temp > 20:
    print("it's nice")
else:
    print("cold")
print("done")


print("                  3- Ternary Operator                    ")

age = 10
message = "Young"if age <= 20 else "Old"
print(message)


print("                  4- Logical Operators                   ")

high_income = True
good_credit = False

if (high_income and good_credit):
    print("Eligible")
else:
    print("Not Eligible")


if (high_income or good_credit):
    print("Eligible")
else:
    print("Not Eligible")

student = True

if not student:
    print("not Student")
else:
    print("Student")

if high_income or good_credit and not student:
    print("Eligible")


print("                5- Short-circuit Evaluation              ")
if high_income and good_credit and not student:
    print("Eligible")


print("              6- Chaining Comparison Operators           ")

myAge = 22
if 18 <= myAge < 65:
    print("Middle Age")

print("             8- For Loops               ")
for number in range(3):
    print("Sending a message", number+1, (number+1)*".")

for number in range(1, 10, 2):
    print("Attempt", number, number*".")


print("             9- For..Else               ")

Successful = False
for number in range(3):
    print("Attempt")
    if Successful:
        print("Successful")
        break
else:
    print("Attemptad 3 times and failes")


print("             10- Nested Loops           ")

for x in range(3):
    for y in range(3):
        print(f"( {x} , {y} )")


print("             11- Iterables               ")

print(type(5))
print(type(range(5)))


print("             12- While Loops              ")

numbers = 1
while numbers < 10:
    print(numbers)
    numbers += 1

print("             13- Infinite Loops           ")


print("             14- Exercise                  ")
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f" number of {count} created")
