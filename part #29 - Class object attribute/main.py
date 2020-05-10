# template
class Estudent:
	# class attribute
	# departament = None
	total = 0

	# constructor __init__()
	def __init__(self,name,id):
		# object / instance attribute
		self.name = name
		self.id = id
		Estudent.total += 1

# object / instance 
joaquim = Estudent("joaquim",123)
elia = Estudent("elia",129)
nidia = Estudent("nidia",132)
donacio = Estudent("donacio",133)

'''
print(donacio.__dict__)
print(donacio.departament)
donacio.departament = "IT"
print(donacio.departament)
print(donacio.__dict__)

print(elia.__dict__)
elia.hobby = "dance"
print(elia.hobby)
print(elia.__dict__)
'''

print("estudent total :", Estudent.total)