numbers= [1,2,3,40,5,6,8,11]
numbers.append(20)
print(numbers)


number = [1,2,2,3,4,5,5]
unique =[]
print(number)
for item in number:
        if item not in unique:
            unique.append(item)

print(unique )