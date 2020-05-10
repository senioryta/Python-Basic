# superclass
class Estudent:
	# class attribute
	total = 0

	# constructor __init__()
	def __init__(self,name,id):
		self.name = name
		self.id = id

	# method
	def showinfo(self):
		print("{} \n\t id : {} \n".format(self.name,self.id))

# subclass
class Estudent_a(Estudent):
	
	def showinfo(self):
		print("checkin class A. estudante name " + self.name)

# object / instance 
angelina = Estudent("angelina",112)
angelia = Estudent_a("angelia",232)

angelina.showinfo()
angelia.showinfo()