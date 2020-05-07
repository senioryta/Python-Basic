print("SIMPLE GAME USE IF STATEMENT!\n")

print("si'ik numeru husi 1 - 100?")

nu_segredu = 57
naran = str(input("ita nia naran? "))
numeru = int(input("ita nia numeru? "))

if numeru == nu_segredu:
	print(naran + " ita bo'ot menan, maibe la iha premiu :)")
elif numeru == 0:
	print("favor priense numeru hahu husi 1 - 100?")
elif numeru < 0:
	numeru = 0
	print("numeru negativu troka ba zero!")
elif numeru < nu_segredu:
	print("ita nia numeru ki'ik liu!")
else:
	print("ita nia numeru bo'ot liu!")

print('\n(C) 2020. JM')