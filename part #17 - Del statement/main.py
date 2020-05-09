numbers = [1,2,9,0,69,33,4.7]

print(numbers)

del numbers[0]

print(numbers)

del numbers[2:5]

print(numbers)

del numbers[:]

print(numbers)

name = "juliao"

print(name)

del name

try:
	print(name)
except NameError:
	print("variable is not defined")