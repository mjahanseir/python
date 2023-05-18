weight  = input("Weight : ")
type= input("(L)bs or (K)g: ")
if type.lower()=='l':
    convert = float(weight)* 0.45
    print(f"You are {convert} kilos")
elif type.lower()=='k' :
    convert = float(weight)*2.2
    print(f"You are {convert} pound")
else :
    print("Invalid Input")