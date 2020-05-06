friends = ['basilio','donacio','eusebio','hermengildo']
# 				0		1			2			3
# 				-4		-3			-2			-1

print(friends)

print('\n')

print(friends[1])
print(friends[3])
print(friends[-1])

print(10*'=')

print(friends[-2:])
print(friends[:])

# concetanation + operator
add = ['angelina','donilia','luduvina']

print(friends + add)

# list are mutable
number = [1,32,93,111,230,121]

print(number)
number[2] = 3.0
print(number)

# using append() method, add new item at the end list
number.append(17)
number.append(0.7)
print(number)

print(10 * '=')
print('\n')

fruits = ['apple','orange','painapple','guava','grape']
print(fruits)
fruits[1:4] = ['ORANGE','PAINAPPLE','GUAVA']
print(fruits)

fruits[2:5] = []
print(fruits)

fruits[:] = []
print(fruits)

print(10*'=')

letters = ['a','b','c','d']
print(len(letters))

print(10*'=')

items = ['window','door','table','chair','dipper']
basketball = ['ball','player','banana','boats']
date = [items,basketball]

print(date)
print(date[0])
print(date[1])
print(date[0][1])
print(date[0][-3])
print(date[1][1])
print(date[1][2:4])
print(date[1][-3:])