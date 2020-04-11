from tkinter import *
from tkinter.ttk import *

win = Tk()
    
def Ophthalmologist():
    win1 = Tk()
    win1.geometry("1000x1000")
    def A():
        print("you chose Dr.Negi")
    def B():
        print("you chose Dr.Pokhrial")
    def C():
        print("you chose Dr.Gupta")

    l = Label(win1,text="Here are some doctor you might want to see")
    b = Button(win1,text="1. Dr.Negi",command=A)
    b.grid()
    b1 = Button(win1,text="1. Dr.Pokhriyal",command=B)
    b1.grid()
    b2 = Button(win1,text="1. Dr.Gupta",command=C)
    b2.grid()
    
    win1.mainloop()    
    
def Nephrologist(event):
    print("Here are some doctor you might want to see:")
    print("1. Dr.Vidit")
    print("2. Dr.Aditya")
    print("3. Dr.Aryan")
    ch=int(input("enter choice"))
    if ch == 1:
        print("you chose dr.vidt")
    elif ch == 2:
        print ("you chose dr.aditya")
    elif ch == 3:
        print ("you chose dr.aryan")
    
def Otolaryngologist(event):
    print("Here are some doctor you might want to see:")
    print("1. Dr.laswai")
    print("2. Dr.bhandari")
    print("3. Dr.ojash")
    ch=int(input("enter choice"))
    if ch == 1:
        print("you chose dr.laswai")
    elif ch == 2:
        print ("you chose dr.bhandari")
    elif ch == 3:
        print ("you chose dr.ojash")
    
def Neurologist(event):
    print("Here are some doctor you might want to see:")
    print("1. Dr.utkarsh")
    print("2. Dr.rohan")
    print("3. Dr.rushil")
    ch=int(input("enter choice"))
    if ch == 1:
        print("you chose dr.utkarsh")
    elif ch == 2:
        print ("you chose dr.rohan")
    elif ch == 3:
        print ("you chose dr.rushil")
    
def Gastroenterologist(event):
    print("Here are some doctor you might want to see:")
    print("1. Dr.yashika")
    print("2. Dr.ganesh")
    print("3 Dr.mayank")
    ch=int(input("enter choice"))
    if ch == 1:
        print("you chose dr.yashika")
    elif ch == 2:
        print ("you chose dr.ganesh")
    elif ch == 3:
        print ("you chose dr.mayank")
    
def Endocrinologist(event):
    print("Here are some doctor you might want to see:")
    print("1. Dr.kartik")
    print("2. Dr.anurag")
    print("3. Dr.anushka")
    ch=int(input("enter choice"))
    if ch == 1:
        print("you chose dr.kartik")
    elif ch == 2:
        print ("you chose dr.anurag")
    elif ch == 3:
        print ("you chose dr.anushka")
    
def Dermatologist(event):
    print("Here are some doctor you might want to see:")
    print("1. Dr.aakash")
    print("2. Dr.raj")
    print("3. Dr.sharma")
    ch=int(input("enter choice"))
    if ch == 1:
        print("you chose dr.aakash")
    elif ch == 2:
        print ("you chose dr.raj")
    elif ch == 3:
        print ("you chose dr.sharma")
    
def Cardiologist(event):
    print("Here are some doctor you might want to see:")
    print("1. Dr.manaswini")
    print("2. Dr.roy")
    print("3. Dr.aviral")
    ch=int(input("enter choice"))
    if ch == 1:
        print("you chose dr.manaswini")
    elif ch == 2:
        print ("you chose dr.roy")
    elif ch == 3:
        print ("you chose dr.aviral")
    
def Psychiatrist(event):
    print("Here are some doctor you might want to see:")
    print("1. Dr.srishti")
    print("2. Dr.srivastava")
    print("3. Dr.ronit")
    ch=int(input("enter choice"))
    if ch == 1:
        print("you chose dr.srishti")
    elif ch == 2:
        print ("you chose dr.srivastava")
    elif ch == 3:
        print ("you chose dr.ronit")
    
def Surgeon(event):
    print("Here are some doctor you might want to see:")
    print("1. Dr.aggarwal")
    print("2. Dr.shobit")
    print("3. Dr.setty")
    ch=int(input("enter choice"))
    if ch == 1:
        print("you chose dr.aggarwal")
    elif ch == 2:
        print ("you chose dr.shobit")
    elif ch == 3:
        print ("you chose dr.setty")
    
def Gynecologist(event):
    print("Here are some doctor you might want to see:")
    print("1. Dr.post")
    print("2. Dr.malone")
    print("3. Dr.eminem")
    ch=int(input("enter choice"))
    if ch == 1:
        print("you chose dr.post")
    elif ch == 2:
        print ("you chose dr.malone")
    elif ch == 3:
        print ("you chose dr.eminem")
    
def Pediatrician(event):
    print("Here are some doctor you might want to see:")
    print("1. Dr.sza")
    print("2. Dr.halsey")
    print("3. Dr.john")
    ch=int(input("enter choice"))
    if ch == 1:
        print("you chose dr.sza")
    elif ch == 2:
        print ("you chose dr.halsey")
    elif ch == 3:
        print ("you chose dr.john")

#GUI-PART#

b1 = Button(win,text="Ophthalmologist",command=Ophthalmologist)
b1.grid(row=1,column=1)

b2 = Button(win,text="Nephrologist")
b2.grid(row=1,column=2)
b2.bind("<Button-1>",Nephrologist)

b3 = Button(win,text="ENT specialist")
b3.grid(row=1,column=3)
b3.bind("<Button-1>",Otolaryngologist)

b4 = Button(win,text="Neurologist")
b4.grid(row=1,column=4)
b4.bind("<Button-1>",Neurologist)        
        
b5 = Button(win,text="Gastroenterologist")
b5.grid(row=1,column=5)
b5.bind("<Button-1>",Gastroenterologist)


b6 = Button(win,text="Endocrinologist")
b6.grid(row=1,column=6)
b6.bind("<Button-1>",Endocrinologist)

b7 = Button(win,text="Dermatologist")
b7.grid(row=1,column=7)
b7.bind("<Button-1>",Dermatologist)

b8 = Button(win,text="Cardiologist")
b8.grid(row=1,column=8)
b8.bind("<Button-1>",Cardiologist)

b9 = Button(win,text="Psychiatrist")
b9.grid(row=1,column=9)
b9.bind("<Button-1>",Psychiatrist)

b10 = Button(win,text="Surgeon")
b10.grid(row=1,column=10)
b10.bind("<Button-1>",Surgeon)

b11 = Button(win,text="Gynecologist")
b11.grid(row=1,column=11)
b11.bind("<Button-1>",Gynecologist)

b12 = Button(win,text="Pediatrician")
b12.grid(row=1,column=12)
b12.bind("<Button-1>",Pediatrician)

win.after(30000,win.destroy)

win.mainloop()

















        

        
    

        
        
        
        
        
            
