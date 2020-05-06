# single quote
print('Helo Mundu')
print('ha\'u mak JM')

# double quote
print("ha'u mak JM")
print('"JM", hakarak sai programador')
print("\"JM\", hakarak sai programador")
print('"ha\'u" hakarak sai programador')

print(10 * '=')

w = "linha primeiru.\nlinha segundu" # n mean new line
print(w)
print('\tjm respect') # t mean tab

print(10 * '=')

# raw input
print('C:\some\name') # without r
print(r'C:\some\name') # with r

print('\n')

print("""\
Identidade Pessoal
Naran Kompletu : Juliao Martins
Fatin-Moris	   : Dili, 17/07/2001
Enderesu 	   : Tasi-Tolu
N0. Telefone   : 932939242384
""")

# concetaned with + operator
print('juli' + 'ao')

# and repeated with * operator
print('un' * 3)
print('+' * 3)
print('=' * 3)
print('*' * 3)

# can write
print('py' 'thon')

print('ida ne\'e praragrafu naruk teb'
	'-tebes la halimar no ita bele hakerek hanesan ne\'e.')

# variable
prefix = 'py'

print(prefix + 'thon')

print('\n')

# slicing
word = 'python'

# the index firts character always 0
print(word[0]) # character position 0
print(word[5]) # character position 5

"""
p y t h o n 	   p  y  t  h  o  n
| | | | | |   or   |  |  |  |  |  |
0 1 2 3 4 5		  -6 -5 -4 -3 -2 -1

NOTE : 0 same as -0
"""

print(word[-6])
print(word[-3])

print(word[0:2])
print(word[2:5])

print(word[:2] + word[2:]) 
print(word[:4] + word[4:])

print(20*'=')

print(word[:2])
print(word[4:])
print(word[-2:])

print(word[4:42])
print(word[42:])

# string are immutable 
print('j' + word[1:])
print('py' + word[0:2])

a = 'hauhakaraksaiprogramadornohautenkeserestudabaraknobukareferensiabarak!'
print(len(a))