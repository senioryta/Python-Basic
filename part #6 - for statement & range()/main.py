text = ['cow','pig','window','apple']

for txt in text:
	print(txt, len(txt))

print(20*'=')

"""
for i in range(6):
	print(i) # 0, 1, 2, 3, 4, 5

print(20*'=')

for l in range(2,9):
	print(l) # 2, 3, 4, 5, 6, 7, 8

print(20*'=')
for x in range(1,20,5):
	print(x) # 1, 6, 11, 16

print(20*'=')

for y in range(-10,-100,-40):
	print(y) # -10, -50, -90
"""

barcelona_team = ['messi','suarez','rakitik','ter stegen']

for player in range(len(barcelona_team)):
	print(player, barcelona_team[player])

print(range(0,10))
print(sum(range(6))) # 0 + 1 + 2 + 3 + 4 + 5 = 15
print(list(range(2,9)))