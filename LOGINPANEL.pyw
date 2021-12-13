#figure out how to make line 17 and 20 work

#LOGINPANEL
#Filip Rokita
#www.filiprokita.com



#import
from tkinter import *
from tkinter import messagebox
import os



#def
def log():
    os.system("./login.pyw")

def reg():
    os.system("./register.pyw")



#main
root = Tk()
root.title("LOGINPANEL")
root.iconbitmap("assets/icon32.ico")
root.geometry("300x100")

askL = Label(root, text="What do you want to do?"); askL.pack()
logB = Button(root, text="LOGIN", command=log, width=10); logB.pack()
regB = Button(root, text="REGISTER", command=reg, width=10); regB.pack()

root.mainloop()