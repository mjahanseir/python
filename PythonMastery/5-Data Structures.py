#                     1- Lists
letter = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0]*5
print(zeros)
combined = zeros + letter
numbers = list(range(20))
print(combined)
print(numbers)
chars = list("Hello world")
print(chars)
print(len(chars))


print("***********         2         ***********")
#                     2- Accessing Items
letters = ["a", "b", "c", "d"]
letters[0] = 'A'
print(letters[0])
print(letters[-1])
print(letters[0:3])
print(letters[0:])
print(letters[2:])
print(letters[:])
print(letters[::2])
print(letters)


number = list(range(20))
print(number)
print(number[::2])
print(number[::-1])


print("***********         3         ***********")
#                     3- List Unpacking

num = [1, 2, 3]
first = num[0]
second = num[1]
third = num[2]
one, two, three = num
print(num)
print(one)
print(two)
print(three)

nums = [1, 2, 3, 4, 5]
on, tw, *others = nums  # unpack and pack

print(nums)
print(on)
print(tw)
print(others)


nums2 = [1, 2, 3, 4, 5]
on2, *others2, last = nums2  # unpack and pack

print(nums2)
print(on2)
print(others2)
print(last)


print("***********         4         ***********")
#                     4- Looping over Lists
letts = ["a", "b", "c"]
for lett in letts:
    print(lett)

letts2 = ["a", "b", "c"]
for lett2 in enumerate(letts2):
    print(lett2)

for index, lett2 in enumerate(letts2):
    print(index, lett2)


print("***********         5         ***********")
#                     5- Adding or Removing Items
lt = ['a', 'b', 'c', 'd']
print(lt)

lt.append('e')
print(lt)

lt.insert(0, "-")
print(lt)

lt.pop()
print(lt)

lt.pop(0)
print(lt)

lt.remove('b')
print(lt)

del lt[1:3]
print(lt)

lt.clear()
print(lt)


print("***********         6         ***********")
#                     6- Finding Items


#                     7- Sorting Lists


#                     8- Lambda Functions


#                     9- Map Function


#                     10- Filter Function


#                     11- List Comprehensions


#                     12- Zip Function


#                     13- Stacks


#                     14- Queues


#                     15- Tuples


#                     16- Swapping Variables (2:37)
#                     17- Arrays (3:11)
#                     18- Sets (4:03)
#                     19- Dictionaries (5:24)
#                     20- Dictionary Comprehensions (3:19)
#                     21- Generator Expressions (3:51)
#                     22- Unpacking Operator (4:05)
#                     23- Exercise (6:21)
