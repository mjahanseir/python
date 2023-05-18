name=input("Enter Your Name : ")
nameLn=len(name)
if nameLn<4:
    print("Your name is less than 4 charecters")
elif nameLn<10 :
    print("Your name at least 4 char and less than 10 char.")
else :
    print("your name is too long")