# Section 3.6 snippets

for character in 'Programming':
    print(character, end='  ')

# Function print’s sep Keyword Argument
print(10, 20, 30, sep=', ')

# 3.8.1 Iterables, Lists and Iterators
total = 0

for number in [2, -3, 0, 17, 9]:
    total = total + number

total

# 3.8.2 Built-In range Function and Generators
for counter in range(10):
    print(counter, end=' ')
