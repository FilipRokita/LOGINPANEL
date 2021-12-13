#import
from tkinter import *
from tkinter import messagebox
import hashlib
from other.combocreator import *
from other.checkcred import *
from other.settings import *



#def
def work():
    usr = str(usrTV.get())
    pwd = str(pwdTV.get())

    localcombo = combocreator(usr, pwd)

    if checkcred(usr, pwd, datalocation) == True:

        f = open(datalocation, "a")
        f.write(localcombo)
        f.close()

        messagebox.showinfo(title="SUCCESS - LOGINPANEL", message="You have been registered succesfully!")
        registerpy.destroy()
    else:
        messagebox.showinfo(title="FAIL - LOGINPANEL", message="""There is a problem registering!
Maybe:

- your username is taken
- your username is too short
- your username is the same as your password
- your username includes colon
- your password is too short
- your password doesn't include at least one special character, uppercase letter, lowercase letter and digit

Try again!""")



#main
registerpy = Tk()
registerpy.title("REGISTER")
registerpy.iconbitmap("assets/icon32.ico")
registerpy.geometry("300x200")
registerpy.resizable(False, False)


usrTV = StringVar()
pwdTV = StringVar()


usrL = Label(registerpy, text="USERNAME"); usrL.pack()
usrE = Entry(registerpy, textvariable=usrTV); usrE.pack()
pwdL = Label(registerpy, text="PASSWORD"); pwdL.pack()
pwdE = Entry(registerpy, textvariable=pwdTV, show="*"); pwdE.pack()

workB = Button(registerpy, text="REGISTER", command=work); workB.pack(pady=10)

authorL = Label(registerpy, text="www.filiprokita.com"); authorL.pack(pady=10)


registerpy.mainloop()