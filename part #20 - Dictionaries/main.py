phone = {"juliao":78742490,"leonardo":74213399,"licenia":73392084,"luduvina":77723902}

print(phone["juliao"])

phone["serafina"] = 79782100

print(phone)

print(phone.keys())
print(phone.values())

def douequalsp():
	print(15*"=+=")
douequalsp()

estudent1 = {"ID":173472,
			"name":"joaquim da s. gomes",
			"departament":"IT",
			"email":"aquimwinky00@gmail.com"
			}

estudent2 = {"ID":173482,
			"name":"marciana martins",
			"departament":"IT",
			"email":"marciamariasempre@gmail.com"
			}

estudent = {173472:estudent1,173482:estudent2}

print(estudent)
douequalsp()
print(estudent.keys())
douequalsp()
print(estudent.values())