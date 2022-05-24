from tkinter import *

root = Tk()

def click():
    Label(root, text="Hello What is your name?").place(x=100, y=100)

# Button
Button1 = Button(root, text="Click me", command=click).place(x=250, y=250)

root.geometry("500x500")
root.mainloop()
