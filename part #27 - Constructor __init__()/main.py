# template
class Estudent:
	# class attribute
	total = 0

	# constructor __init__()
	def __init__(self,inputName,inputId):
		self.name = inputName
		self.id = inputId
		self.showall()

	def showall(self):
		print("{} \n\t id : {}".format(self.name,self.id))

# object / instance
juliao = Estudent("juliao",126)
eusebio = Estudent("eusebio",192)
aurito = Estudent("aurito",188)

'''
juliao.showall()
eusebio.showall()
aurito.showall()
'''