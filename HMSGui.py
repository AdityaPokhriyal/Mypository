from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector

def main():
    db = mysql.connector.connect(host='localhost',user='root',passwd='password313',database='HospitalAV')
    cursor = db.cursor()

    win = Toplevel()
    win.title("Hospital Manegement System")
    win.geometry("228x200")

    #FUNCTION FOR ADDING DATA
    def adddata(event):
        win1 = Tk()
        #PATIENT ID
        l = Label(win1,text="Enter Patient ID: ")
        patientID = Entry(win1)
        l.grid(row=1,column=1,sticky=W)
        patientID.grid(row=1,column=2)
        
        #NAME ENTRY
        l2 = Label(win1,text="Enter Patient Name: ")
        name = Entry(win1)
        l2.grid(row=2,column=1,sticky=W)
        name.grid(row=2,column=2)
     
        #AGE ENTRY
        l3 = Label(win1,text="Enter Age:")
        age = Entry(win1)
        l3.grid(row=3,column=1,sticky=W)
        age.grid(row=3,column=2)
       
        #DISEASE ENTRY
        l4 = Label(win1,text="Enter Disease or Illness:")
        disease_illness = Entry(win1)
        l4.grid(row=4,column=1,sticky=W)
        disease_illness.grid(row=4,column=2)
       
        #DOCTOR NAME
        l5 = Label(win1,text="Enter Doctor Name:")
        doctorname = Entry(win1)
        l5.grid(row=5,column=1,sticky=W)
        doctorname.grid(row=5,column=2)
       
        #PHONE NUMBER
        l6 = Label(win1,text="Enter your Phone Number:")
        phonenumber = Entry(win1)
        l6.grid(row=6,column=1,sticky=W)
        phonenumber.grid(row=6,column=2)
        
        #ADDRESS
        l7 = Label(win1,text="Enter your Address:")
        address = Entry(win1)
        l7.grid(row=7,column=1,sticky=W)
        address.grid(row=7,column=2)

        a = patientID
        b = name
        c = age
        d = disease_illness
        e = doctorname
        f = phonenumber
        g = address

        global qry
        qry = "INSERT INTO patients VALUES(%s,%s,%s,%s,%s,%s,%s)"
        global data
        data = (a,b,c,d,e,f,g)
       
        def click():
            
            global a
            a = patientID.get()
            global b
            b = name.get()
            global c
            c = age.get()
            global d
            d = disease_illness.get()
            global e
            e = doctorname.get()
            global f
            f = phonenumber.get()
            global g
            g = address.get()
            print(a,b,c,d,e,f,g)

            if len(c) > 3:
                winError = Tk()
                winError.withdraw()
                messagebox.showerror("Error!", "Please enter a valid age")
                winError.mainloop()
                
            elif len(f) > 10:
                winError = Tk()
                winError.withdraw()
                messagebox.showerror("Error!", "Please enter a valid 10-digit phonenumber")
                winError.mainloop() 

            else:
                cursor.execute("insert into patients values("+'"'+a+'"'+','+'"'+b+'"'+','+ str(c) +','+'"'+d+'"'+','+'"'+e+'"'+','+'"'+f+'"'+','+'"'+g+'"'+')')
                db.commit()
                
        #ENTER BUTTON 
        b1 =  Button(win1,text="Enter",command=click)
        b1.grid(row=8,column=1)
          
        win1.mainloop()

    #FUNCTION TO UPDATE DATA    
    def updatedata(event):
        win2 = Tk()

        patientID = "a"

        def FinalUpdate1(event):
            global i
            i = ID.get()
            j = name.get()
            print(i)
            print(j)
            cursor.execute("update patients set name ="+'"'+str(j)+'"'+" where patientID ="+'"'+str(i)+'"')
            db.commit()
            
        def Nclick():   
            win6 = Tk()

            label5 = Label(win6,text="Enter New Name: ")
            global name
            name = Entry(win6)
            button12 = Button(win6,text="SAVE")
            label5.grid(row=1,column=1,sticky=W)
            name.grid(row=1,column=2)
            button12.grid(row=2,column=1)
            button12.bind("<Button-1>",FinalUpdate1)
            
            win6.mainloop()

        def FinalUpdate2(event):
            global i
            i = ID.get()
            j = age.get()
            print(i)
            print(j)
            if len(j) > 3:
                winError = Tk()
                winError.withdraw()
                messagebox.showerror("Error!", "Please enter a valid age")
                winError.mainloop()
            else:
                cursor.execute("update patients set age ="+'"'+str(j)+'"'+" where patientID ="+str(i))
                db.commit()    

        def Aclick():
            win7 = Tk()

            label6 = Label(win7,text="Enter New Age: ")
            global age
            age = Entry(win7)
            button13 = Button(win7,text="SAVE")
            label6.grid(row=1,column=1,sticky=W)
            age.grid(row=1,column=2)
            button13.grid(row=2,column=1)
            button13.bind("<Button-1>",FinalUpdate2)
            
            win7.mainloop()

        def FinalUpdate3(event):
            global i
            i = ID.get()
            j = disease_illness.get()
            print(i)
            print(j)
            cursor.execute("update patients set disease_illness ="+'"'+str(j)+'"'+" where patientID ="+'"'+str(i)+'"')
            db.commit()    

        def DISclick():
            win8 = Tk()

            label7 = Label(win8,text="Enter New Disease: ")
            global disease_illness
            disease_illness = Entry(win8)
            button14 = Button(win8,text="SAVE")
            label7.grid(row=1,column=1,sticky=W)
            disease_illness.grid(row=1,column=2)
            button14.grid(row=2,column=1)
            button14.bind("<Button-1>",FinalUpdate3)
            
            win8.mainloop()

        def FinalUpdate4(event):
            global i
            i = ID.get()
            j = doctorname.get()
            print(i)
            print(j)
            cursor.execute("update patients set doctorname ="+'"'+str(j)+'"'+" where patientID ="+'"'+str(i)+'"')
            db.commit()    

        def DOCclick():
            win9 = Tk()

            label8 = Label(win9,text="Enter New Doctor: ")
            global doctorname
            doctorname = Entry(win9)
            button15 = Button(win9,text="SAVE")
            label8.grid(row=1,column=1,sticky=W)
            doctorname.grid(row=1,column=2)
            button15.grid(row=2,column=1)
            button15.bind("<Button-1>",FinalUpdate4)
            
            win9.mainloop()

        def FinalUpdate5(event):
            global i
            i = ID.get()
            j = phonenumber.get()
            print(i)
            print(j)
            if len(j) > 10:
                winError = Tk()
                winError.withdraw()
                messagebox.showerror("Error!", "Please enter a valid 10-digit phonenumber")
                winError.mainloop()
            else:
                cursor.execute("update patients set phonenumber ="+'"'+str(j)+'"'+" where patientID ="+'"'+str(i)+'"')
                db.commit()

        def PHclick():
            win10 = Tk()

            label9 = Label(win10,text="Enter New Phone Number: ")
            global phonenumber
            phonenumber = Entry(win10)
            button16 = Button(win10,text="SAVE")
            label9.grid(row=1,column=1,sticky=W)
            phonenumber.grid(row=1,column=2)
            button16.grid(row=2,column=1)
            button16.bind("<Button-1>",FinalUpdate5)
            
            win10.mainloop()

        def FinalUpdate6(event):
            global i
            i = ID.get()
            j = address.get()
            print(i)
            print(j)
            cursor.execute("update patients set address ="+'"'+str(j)+'"'+" where patientID ="+'"'+str(i)+'"')
            db.commit()    

        def ADDclick():
            win11 = Tk()

            label10 = Label(win11,text="Enter New Address: ")
            global address
            address = Entry(win11)
            button17 = Button(win11,text="SAVE")
            label10.grid(row=1,column=1,sticky=W)
            address.grid(row=1,column=2)
            button17.grid(row=2,column=1)
            button17.bind("<Button-1>",FinalUpdate6)
            
            win11.mainloop()
            
        def click3():
            win4 = Tk()
            
            label3 = Label(win4,text="Choose what you want to update in the record.")
            button5 = Button(win4,text="NAME",command=Nclick)
            button6 = Button(win4,text="AGE",command=Aclick)
            button7 = Button(win4,text="DISEASE",command=DISclick)
            button8 = Button(win4,text="DOCTOR NAME",command=DOCclick)
            button9 = Button(win4,text="PHONE NUMBER",command=PHclick)
            button10 = Button(win4,text="ADDRESS",command=ADDclick)
            
            label3.grid(row=1,column=1)
            button5.grid(row=3,column=1)
            button6.grid(row=4,column=1)
            button7.grid(row=5,column=1)
            button8.grid(row=6,column=1)
            button9.grid(row=7,column=1)
            button10.grid(row=8,column=1)
            win4.mainloop()

        label1 = Label(win2,text="Enter Patient ID of the patient whose records are to be updated: ")
        ID = Entry(win2)
        button3 = Button(win2,text="Next",command=click3)
        button3.grid(row=2,column=1)
        label1.grid(row=1,column=1,sticky=W)
        ID.grid(row=1,column=2)

        win2.mainloop()
        

    #FUNCTION TO DELETE DATA        
    def deldata(event):
        win3 = Tk()
        def click2(event):
            global h
            h = ID.get()
            print(h)
            cursor.execute("delete from patients where patientID ="+str(h))
            db.commit()

        label2 = Label(win3,text="Enter Patient ID of the patient whose records are to be deleted: ")
        ID = Entry(win3)
        label2.grid(row=1,column=1,sticky=W)
        ID.grid(row=1,column=2)
        button2 = Button(win3,text="Delete")
        button2.grid(row=2,column=1,padx=150)
        button2.bind("<Button-1>",click2)

        win3.mainloop()    
 
    win.iconbitmap(r"C:\Program Files\AV\HMSicons(.ico)\HMS.ico")

    photo1 = PhotoImage(file=r"C:\Program Files\AV\NEW.png")
    photo1 = photo1.subsample(20,20)
    label1 = Label(image=photo1)
    label1.image = photo1
    addnew = Button(win,text="Add New",image=photo1,compound=TOP)
    addnew.grid(row=10,column=0,sticky=W,columnspan=1)
    addnew.bind("<Button-1>",adddata)

    photo3 = PhotoImage(file=r"C:\Program Files\AV\UPDATE.png").subsample(20,20)
    label3 = Label(image=photo3)
    label3.image = photo3
    update = Button(win,text="Update",image=photo3,compound=TOP)
    update.grid(row=10,column=3,sticky=W)
    update.bind("<Button-1>",updatedata)

    photo4 = PhotoImage(file=r"C:\Program Files\AV\DELETE.png").subsample(20,20)
    label4 = Label(image=photo4)
    label4.image = photo4
    delete = Button(win,text="Delete",image=photo4,compound=TOP)
    delete.grid(row=10,column=5,sticky=W)
    delete.bind("<Button-1>",deldata)

    win.after(30000,win.destroy)

    win.mainloop()    
