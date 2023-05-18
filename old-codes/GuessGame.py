secretNumber = 9
i = 0
while i < 3:
    guess = int(input("Guess number: "))
    i += 1
    if guess == secretNumber:
        print("Success!")
        break
else:
    print("Fail!")
