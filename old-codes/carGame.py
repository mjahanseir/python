command = input("")
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started :
            print("Car is already Started.")
        else:
            print("Car Started.")
            started= True
    elif command == "stop":
        if not started :
             print("Car is already Stoped")
        else :
            print("Car Stoped")
            started= False
    elif command == "help":
        print('''
start - to start car
stop - to stop car
quit - to exit
         ''')
    elif command == "quit" :
        break
else:
    print("Fail")
