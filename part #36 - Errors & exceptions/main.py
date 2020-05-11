'''
def division(a,b):
	print("{} / {} = {}".format(a,b,a/b))

while True:
	try:
		x = int(input("call number : "))
		y = int(input("division number : "))
		division(x,y)
		break
	except Exception as error:
		print("Error : {}".format(error))
	except ValueError:
		print("this is not a number!")
	except ZeroDivisionError:
		print("this is Zero!")
'''

try:
	import django
except ImportError:
	print("no module django!")

try:
	jm_kodigu
except NameError:
	print("variable is not define!")