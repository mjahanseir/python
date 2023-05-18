phone = input("Phone: ")
dogo_maping= {
    "1": "One",
    "2": "Two",
    "3": "Three"
}
str=""
for number in phone:
    str+= dogo_maping.get(number, "!") + " "

print(str)
