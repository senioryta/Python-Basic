# definitiong a function
def fibonacci():
	a,b = 0,1
	while a < 10:
		print(a, end=' ')
		print()
		a,b = b, a+b

# call function
fibonacci()

def fibonacci2(n):
	result = []
	a,b = 0,1
	while a < n:
		result.append(a)
		a,b = b, a+b
	return result

print(fibonacci2(200))

def doublequals():
	print(10*'=','\n')
doublequals()

# can call function inside function
def birdvoice():
	print("kokoreeeekkoooo....")

# call inside definitiong a function
def pricebird():
	birdvoice()
	print("1 bird get price 5$")

# now call
# pricebird()

# again call
def buybird(howbird):
	pricebird()
	t = howbird * 5
	print(str(howbird) + ' birt get price ' + str(t) + '$')

buybird(5)
buybird(34)
buybird(1.5)