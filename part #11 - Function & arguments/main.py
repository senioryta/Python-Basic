def addit(a,b):
	# argumen -> a & b 
	print("{} + {} = {}".format(a,b,a+b))

# 4 -> a & b -> 29
addit(4,29)

print(10*'=')

# default agrumen
def estudent(name="name",id=0):
	print("name", name,"\nid", id)

estudent()

# access agrumen
def securyti(name="name",work="work"):
	print("securyti name :", name, "\nwork :", work)

# without access
securyti("night","john")
# with access
securyti(name="michael",work="day")
securyti(work="night",name="john")