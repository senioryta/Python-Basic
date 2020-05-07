from getpass import *

while True:
	username = str(input("Username : "))
	password = getpass(prompt="Password : ",stream=None)

	if username.lower() == "jm-kodigu" and password.lower() == "jjmq112":
		print("SUCCESS LOGIN!\nWelcome " + username.title())
		break
	elif len(username) == 0 and len(password) == 0:
		print("please insert a character!")
	else:
		print("Username or Password incorrect!")


print("(C) 2020. jm")