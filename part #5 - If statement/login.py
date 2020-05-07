import getpass

print("Login")
print(8*'=')

username = str(input("Username : "))
password = getpass.getpass(prompt="Password : ",stream=None)

if username.lower() == "jm-kodigu" and password.lower() == "jjmq":
	print('SUCCESS LOGIN!')
elif len(username) == 0 and len(password) == 0:
	print("please enter a character!")
else:
	print("username or password incorrect!")
	exit()	

print("WELCOME " + username)
print("(C) 2020. JM")