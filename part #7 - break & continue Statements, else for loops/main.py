for i in range(2,10):
	for x in range(2,i):
		if i % x == 0:
			print(i, '=', x, ' * ', i//x)
			break
	else:
		print(i, 'is a prime number!')

print(10*'=')

for i in range(3,40,3):
	if i == 24:
		print("your number is " + str(i))
		break

	print(i)

else:
	print("outside for loops!")

for x in range(2,12):
	if x % 2 == 0:
		print("found an even number", x)
		continue

	print("found a number", x)

else:
	print("outside for loops!")