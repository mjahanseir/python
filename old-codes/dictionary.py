emp={}

emp["first"] = 2
emp["two"] = 3
emp["three"]  = 4
print(emp)
print(len(emp))

print(emp["first"])
emp["first"]=10
print(emp["first"])

del emp["two"]
print(emp)