colors = ['red', 'green', 'blue']


print(len(colors))
idx = 1
print(colors[idx + 1])
print(colors[-1])

colors.append('purple')

print('***************************************************')
print(colors)
print('***************************************************')
# basically the equivalent of adding two arrays
# colors + ['black', 'white']  --> methond(val) -> []
colors.extend(['orange', 'black'])

print(colors)
print('***************************************************')

colors.insert(1, 'yellow')

print(colors)

print('***************************************************')
# IF YOU WANT A COPY OF THE ITEM YOU REMOVE
green = colors.pop(2)
print(colors)
print(green)
print('***************************************************')
# IF YOU WANT TO REMOVE AN ITEM

# DEL operator 0(1)
del colors[1]
print(colors)

print('***************************************************')
#remove method - removes the first occurence of the value
# careful, this is just a hidden find loop ie O(n)
colors.remove('orange')

print(colors)
print('***************************************************')

# Resetting the list to empty
# colors.clear()


# LOOPING LISTS

# for in List - i just want to loop n times, to do something with each item
for color in colors:
  print(color)


print('***************************************************')

# when you need to know the INDEX AND ITEM, use the for in enumareate(list)

for idx, color in enumerate(colors):
  print(idx, color)

# LIST COMPREHENSIONS
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = []
for n in nums:
  squares.append(n * n)

print(nums)
print(squares)

print('***************************************************')
squares2 = [n * n for n in nums]

print(squares2)
print(nums)
print('***************************************************')

even_squares = []
for n in nums:
  square = n * n
  if square % 2 == 0:
    even_squares.append(square)

print(even_squares)

print('***************************************************')
 # I want 'n * n' for each 'n' in nums  if 'n * n' is even
square_evens2 = [n * n for n in nums if n % 2 == 0]
print(square_evens2)
print('***************************************************')



names = ('Bruce', 'Clark')
clark = names[1]
print(clark)

# peter_idx = names.index('gfsefadsfsd') <--- not in index error
# print(peter_idx)
print('***************************************************')

what, ever = names

print(what)
print(ever)


print('***************************************************')
obj = {"a":1, "b":2}

# (k,v) tuyple, we actually are unpacking the tuple into two variables
for dasda, jkdfsabhndsaf in obj.items():
  print(dasda)
  print(jkdfsabhndsaf)


print('***************************************************')

tup = (
   (1,(5,6)),
   (3,4)
   )

nums_string = ''
tup2 = (
  (1,2),
  (3,4),
  (5,6),
  (7,8)
)

# 1,2,3,4,5,6,7,8
for num1, num2 in tup2:
  nums_string += str(num1)
  nums_string += str(num2)

print(nums_string)

(num, (num2, num3)), second = tup
print(num3)

print('***************************************************')
# RANGES

# incremental range

for even in range(2, 10, 2):
  print(even)

odds = tuple(range(1, 10, 2))
print(odds)

for num in range(5, 0, -1):
 	print(num)

# Slicing Squence Types
# Strings
short_name = 'Alexandria'[0:4]

print(short_name)


# Lists
sliced_colors = colors[:2]
print(sliced_colors)

# Tuples
animals = ('cat', 'dog', 'mouse', 'bird', 'fish', 'lizard', 'snake', 'monkey')
sliced_animals = animals[1:]

print(sliced_animals)
