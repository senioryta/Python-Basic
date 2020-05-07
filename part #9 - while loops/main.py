a = 0

while a < 10:
	if a == 5:
		print("checkpoint 1")
		a += 1
		break
		print("checkpoint 2")

	print(a)
	a += 1
else:
	print('else got', a)

b = 0

while b < 200:
	print('inside while!')
	if b == 100:
		print("your number is",b)
		break

	b += 1
