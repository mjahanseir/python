#                     1- Lists
from collections import deque
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
print(letters.index('d'))
if 'm' in letters:
    print(letters.index('m'))


print("***********         7         ***********")
#                     7- Sorting Lists
myNums = [3, 51, 2, 8, 6]
print(myNums)

myNums.sort()
print(myNums)


myNums.sort(reverse=True)
print(myNums)

print(sorted(myNums, reverse=True))
print(myNums)

items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 30),
]
items.sort()
print(items)


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

print("***********         8        ***********")
#                     8- Lambda Functions

items.sort(key=lambda item: item[1])
print(items)

print("***********         9        ***********")
#                     9- Map Function

item = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = []
for item in item:
    prices.append(item[1])
print(prices)


prices = list(map(lambda item: item[1], items))
print(prices)
# for item in x:
#     print(item)


print("***********         10        ***********")
#                     10- Filter Function
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)


print("***********         11        ***********")
#                     11- List Comprehensions

preice = [item[1] for item in items]
print(preice)

# filtr=[expression for item in items]
filtr = [item for item in items if item[1] >= 10]
print(filtr)


print("***********         12        ***********")
#                     12- Zip Function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

[(1, 10), (2, 20), (3, 30)]

print(list(zip("abc", list1, list2)))


print("***********         13        ***********")
#                     13- Stacks
# LIFO
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)
last = browsing_session.pop()
print(last)

print(browsing_session)

if not browsing_session:
    print("Redirect", browsing_session[-1])

if not browsing_session:
    print("disabled")


print("***********         14        ***********")
#                     14- Queues
# FIFO
[1, 2, 3]

queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

if not queue:
    print("Empty")
print("***********         15        ***********")
#                     15- Tuples


#                     16- Swapping Variables (2:37)


#                     17- Arrays (3:11)


#                     18- Sets (4:03)


#                     19- Dictionaries (5:24)


#                     20- Dictionary Comprehensions (3:19)


#                     21- Generator Expressions (3:51)


#                     22- Unpacking Operator (4:05)


#                     23- Exercise (6:21)
