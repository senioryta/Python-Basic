# template
class Estudent:
	# class attribute
	__total = 0

	# constructor __init__()
	def __init__(self,name,id):
		self.__name = name
		self.__id = id

	# method
	def showall(self):
		print("{} \n\t id : {}".format(self.__name,self.__id))

	def changename(self,newname):
		self.__name = newname

# object / instance
juliao = Estudent('juliao',126)

juliao.showall()
juliao.changename("jm")
juliao.showall()