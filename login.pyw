#import
from tkinter import *
from tkinter import messagebox
import hashlib
from other.combocreator import *
from other.checkcred import *
from other.settings import *
import os
import time



#def
def work():
    usr = str(usrTV.get())
    pwd = str(pwdTV.get())

    localcombo = combocreator(usr, pwd)

    f = open(datalocation)

    for line in f:
        if line == localcombo:
            os.system(succesRun)
            loginpy.destroy()
            break
    else:
        messagebox.showinfo(title="FAIL - LOGINPANEL", message="Login failed! Wrong username or password.")

    f.close()



#main
loginpy = Tk()
loginpy.title("LOGIN")
loginpy.iconbitmap("assets/icon32.ico")
loginpy.geometry("300x200")
loginpy.resizable(False, False)


usrTV = StringVar()
pwdTV = StringVar()


usrL = Label(loginpy, text="USERNAME"); usrL.pack()
usrE = Entry(loginpy, textvariable=usrTV); usrE.pack()
pwdL = Label(loginpy, text="PASSWORD"); pwdL.pack()
pwdE = Entry(loginpy, textvariable=pwdTV, show="*"); pwdE.pack()

workB = Button(loginpy, text="LOGIN", command=work); workB.pack(pady=10)

authorL = Label(loginpy, text="www.filiprokita.com"); authorL.pack(pady=10)


loginpy.mainloop()