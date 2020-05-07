print("Jogu Cerdas Cermak")

score = 0

while True:
	ops = str(input('ita prontu (y/n) '))
	if ops.lower() == 'y':

		perg1 = str(input('se mak kria lingua python? '))
		if perg1.lower() == 'guido van rossum':
			score += 20
			print("lo'os!")
		else:
			print("sala!")
		
		perg2 = str(input('se mak kria lingua java? '))
		if perg2.lower() == "james gosling":
			score += 20
			print("lo'os!")
		else:
			print("sala!")

		perg3 = str(input("(10 + 20) / 3 = "))
		if perg3 == "10":
			score += 20
			print("lo'os!")
		else:
			print("sala!")

		perg4 = str(input("se mak fundador microsoft? "))
		if perg4.lower() == 'bill gates':
			score += 20
			print("lo'os!")
		else:
			print("sala!")

		perg5 = str(input("twiter hamri'ik ho lingua programasaun? "))
		if perg5.lower() == 'python':
			score += 20
			print("lo'os!")
		else:
			print("sala!")
		break

print('\n')
if score <= 100 and score >= 80:
	print("ita bo'ot hetan score " + str(score) + '% ' + 'maibe la iha premiu :) ba ita bo\'ot!')
elif score < 80 and score >= 60:
	print("ita bo'ot nia score " + str(score) + '% ' + 'presija buka referensia iha "internet" tan!')
else:
	print("ita nia score " + str(score) + '% ' + 'ladiak koko fila fali!')	
print('\n')
print("(C) 2020. jm")