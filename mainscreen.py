from tkinter import *
import mysql.connector
from tkinter import messagebox
import sys
sys.path.insert(1, 'C:\Program Files\AV')
import HMSGui

win2 = Tk()

username = "bajumba"

password = "jumbaba"

def work(event):
    db = mysql.connector.connect(host='localhost',user='root',passwd='password313',database='HospitalAV')
    cursor = db.cursor()
    win = Tk()

    win.title("Hospital Management System")
    win.geometry("228x200")

def open1():
    x = E2.get()
    y = E3.get()
    
    if x == "bajumba":
        HMSGui.main()

    else:
        winError = Tk()
        winError.withdraw()
        messagebox.showerror("Error!", "Wrong user or pass")
        winError.mainloop()

def open2():

    win = Tk()

    lab = Label(win,text="Forename: ")
    ent = Entry(win)
    lab2 = Label(win,text="Surname: ")
    ent2 = Entry(win)
    lab3 = Label(win,text="Create a password: ")
    ent3 = Entry(win)
    lab4 = Label(win,text="Re-enter password: ")
    ent4 = Entry(win)
    lab5 = Label(win,text="Gender: ")
    rad = Radiobutton(win,text="Male",value=1)
    rad2 = Radiobutton(win,text="Female",value=0)
    B = Button(win,text="SIGN UP")
    lab.grid(row=1,column=1,sticky=W)
    ent.grid(row=1,column=2)
    lab2.grid(row=2,column=1,sticky=W)
    ent2.grid(row=2,column=2)
    lab3.grid(row=3,column=1,sticky=W)
    ent3.grid(row=3,column=2)
    lab4.grid(row=4,column=1,sticky=W)
    ent4.grid(row=4,column=2)
    lab5.grid(row=5,column=1,sticky=W)
    rad.grid(row=5,column=2)
    rad2.grid(row=5,column=3)
    B.grid(row=6,column=1,columnspan=3,ipadx=130)
    win.mainloop()
       
F1 = Frame(win2)
F1.pack(side=TOP,ipady=10)
L1 = Label(F1,text=" HOSPITAL AUV ",fg="red",font=("Calibri",64))
L1.pack(side=TOP,ipadx=50)

F2 = Frame(win2)
F2.pack(side=TOP)
L2 = Label(F2,text="Username: ")
L2.grid()
E2 = Entry(F2)
E2.grid(pady=15)

F3 = Frame(win2)
F3.pack(side=TOP)
L3 = Label(F3,text="Password: ")
L3.grid()
E3 = Entry(F3)
E3.grid(pady=15)

photo1 = PhotoImage(file=r"C:\Program Files\AV\LOGIN.png").subsample(20,20)
B1 = Button(F3,image=photo1,compound=TOP,command=open1)
B1.grid(ipadx=50,pady=15)

B2 = Button(F3,text="SIGN UP IF YOU DONT HAVE AN ACCOUNT",compound=BOTTOM,command=open2)
B2.grid(pady=5,ipadx=250)

win2.mainloop()
