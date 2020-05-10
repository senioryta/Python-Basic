# template
class Estudent:
	
	# method
	def showname(self):
		print("estudent name :", self.name)

	def showid(self):
		return 'estudent id : ' + str(self.id)

	def changeid(self,newid):
		self.id = newid

	def showall(self):
		return "estudent \n\t {} \n\t id : {}".format(self.name,self.id)

# object / instance
donacio = Estudent()
donacio.name = "donacio"
donacio.id = 183

elia = Estudent()
elia.name = "elia"
elia.id = 191

basilio = Estudent()
basilio.name = "basilio"
basilio.id = 200


# call method
print(elia.showall())
print('\n')
elia.showname()
print(elia.showid())
elia.changeid(138)
print(elia.showid())
print('\n')
print(elia.showall())