"""
catname = "donasyo"

def changecatname(newname):
	global catname
	catname = newname
	print('changed cat name to', catname)

changecatname("aurito")

print('cat name now is ', catname)
"""

catname = "leonardo"
eat = "universal"

def change_nameat(newname,neweat):
	global catname, eat
	catname = newname
	eat = neweat
	print('changed cat name & eat to\nname :',catname,'\neat :',eat)
	print(10*'+')

change_nameat(newname="rivaldo",neweat="royal canin")

print('cat name now is', catname, 'and eat', eat)