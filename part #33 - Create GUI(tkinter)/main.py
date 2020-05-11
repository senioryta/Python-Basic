import tkinter as tk

main_window = tk.Tk()

main_window.title("GUI Apps")

def click():
	print('Hello, i\'m GUI ^_^')
def quit():
	exit()

button1 = tk.Button(main_window, text="click here!", command=click)
button2 = tk.Button(main_window, text="QUIT", bg="red", fg="white", command=quit)
copyright = tk.Label(main_window, text="(c) 2020. jm-kodigu", fg="blue")

button1.grid(column=0)
button2.grid(row=0,column=1)
copyright.grid(columnspan=2)

main_window.mainloop()