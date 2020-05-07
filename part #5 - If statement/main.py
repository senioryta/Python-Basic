a = 5

if a < 0:
	print('negative changed to zero!')
elif a == 0:
	print('zero!')
elif a == 1:
	print('single')
else:
	print('more!')

score = 89

if score <= 100 and score >= 90:
	print('you got "A"')
elif score < 90 and score >= 80:
	print('you got "B"')
elif score < 80 and score >= 60:
	print('you got "C"')
else:
	print("you lose!")

character = 'z'
animal = 'zebra'

if character in animal:
	print('have a character :', character)

name = "juliao"
member_group = ["genilda","maria","marcia","lurdes","lijania"]

if name not in member_group:
	print(name, "not exist member group")

print(20*'=')

randon_number = 9
number = 3

if number is randon_number:
	print('number is', number)
elif number is not randon_number:
	print('there number is a', number)
else:
	print('no have : ' + str(number))

