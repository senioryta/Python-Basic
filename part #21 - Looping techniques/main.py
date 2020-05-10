estudent =  {"angelina":173420,"alexa":173421,"aprilia":173422}

for k,v in estudent.items():
	print(k,':',v)

print(10*'=')

date = ["tic","tac","toe"]

"""
for i in range(len(date)):
	print(i,":",date[i])
"""

for i,x in enumerate(date):
	print(i,":",x)

print(10*'+')

questions = ["name","favorite color","hobby"]
answers = ["juliao","lightblue","programming"]

for q,a in zip(questions,answers):
	print("what is your {}? it is {}".format(q,a))

print(10*'=')

for i in reversed(range(1,15,3)):
	print(i)

print(10*'=')

names = ["joaquim","januario","aurito","joaquim","aurito"]

for n in sorted(set(names)):
	print(n)