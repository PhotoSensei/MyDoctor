from tkinter import *
import tkinter.messagebox as m
import sqlite3

con = sqlite3.connect('healthcare.db')
c = con.cursor()

def submit(self):
#Database for Registration form

    if(self.epass.get() != self.cpass.get()):
        m.showerror('Password Error', 'Password not matching')
    elif not self.ename.get() and  not self.eid.get() and not self.edes.get() and not self.epass.get() and not self.cpass.get():
        m.showerror('Error','Enter Details')
    elif not self.ename.get():
        m.showerror('Error','Enter Name')
    elif not self.eid.get():
        m.showerror('Error', 'Enter ID')
    elif not self.espec.get():
        m.showerror('Error', 'Enter Designation')
    elif not self.var.get():
        m.showerror('Error', 'Select your gender')
    elif not self.epass.get() and not self.cpass.get():
        m.showerror('Error', 'Enter Password')

    elif(self.epass.get() == self.cpass.get()):
        c.execute('''CREATE TABLE IF NOT EXISTS Doctor (name VARCHAR(20) NOT NULL ,
                                                        id INTEGER UNIQUE NOT NULL ,
                                                        gender VARCHAR(20) NOT NULL ,
                                                        spec VARCHAR (20) NOT NULL )''')
        c.execute('''CREATE TABLE IF NOT EXISTS userpwd (username VARCHAR(20) UNIQUE NOT NULL, 
                                                         password VARCHAR(20) NOT NULL )''')
        # new code
        a1 = self.ename.get()
        b1 = int(self.eid.get())
        c1 = self.var.get()
        d1 = self.espec.get()
        e = self.epass.get()
        user = self.euser.get()
        try:
            c.execute("INSERT INTO Doctor (name, id, gender, spec) VALUES (?, ?, ?, ?)", (a1, b1,c1, d1))
            c.execute('SELECT * FROM Doctor')
            print(c.fetchall())
            c.execute("INSERT INTO userpwd (username, password) VALUES (?, ?)",(user, e))
            c.execute('SELECT * FROM userpwd')
            print(c.fetchall())
            m.showinfo('Registered', 'Saved Successfully')
        except:
            m.showerror('Error', "User already exist")
        con.commit()
    else:
        m.showerror('Error', 'Enter details')

def data_entry(self):
    c.execute('''CREATE TABLE IF NOT EXISTS PRESCRIBED (DOC_NAME VARCHAR(20),DISEASE_NAME VARCHAR(20), MEDICINE_NAME VARCHAR(20))''')
    self.a = self.ed.get()
    self.b = self.er.get()
    self.c = self.edoc.get()
    c.execute('INSERT INTO PRESCRIBED(DOC_NAME,DISEASE_NAME, MEDICINE_NAME) VALUES (?,?,?)', (self.c,self.a, self.b))
    #self.cur.execute('INSERT INTO MEDICINE(NAME) VALUES (?)', (self.b))
    c.execute('SELECT * FROM PRESCRIBED')
    print(c.fetchall())
    m.showinfo('Saved', 'Saved Successfully')
    con.commit()

class Mains:

    def __init__(self, master):
                                                    #First Frame with all the widgets
        self.master = master
        self.ftop = Frame(self.master,width=800,height=100,bg='cornflowerblue')
        self.ftop.pack(side=TOP,fill=X)
        self.lb = Label(self.ftop, text='BE A DOCTOR', font=("Roman", 50, 'bold'), bg='cornflowerblue')
        self.lb.place(x=250, y=10)
        self.fbottom = Frame(self.master,width=800,height=100,bg='cornflowerblue')
        self.fbottom.pack(side=BOTTOM,fill=X)
        self.fleft = Frame(self.master, width=100, height=800, bg='cornflowerblue')
        self.fleft.pack(side=LEFT,fill=Y)
        self.fright = Frame(self.master, width=100, height=800, bg='cornflowerblue')
        self.fright.pack(side=RIGHT,fill=Y)
        self.fcenter = Frame(self.master, width=600, height=600, bg='white')
        self.fcenter.pack()

        self.l1 = Label(self.fcenter, text='Select Your Choice', font=('arial', 30, 'italic'), bg='white')
        self.l1.place(x=170, y=170)

        self.b3 = Label(self.fcenter, text=' ', bg='white', borderwidth=0, padx=10, pady=10)
        self.b3.place(x=230, y=10)
        self.file5 = PhotoImage(file="project.png")
        self.b3.config(image=self.file5, compound=CENTER)
        self.file6 = self.file5.subsample(9,9)
        self.b3.config(image=self.file6)

        self.b1 = Button(self.fcenter, text=' ', bg='sky blue', padx=10, pady=10,command=self.onButton1)
        self.b1.place(x=100, y=240)
        self.file1 = PhotoImage(file="doc3.png")
        self.b1.config(image=self.file1, compound=CENTER)
        self.file2 = self.file1.subsample(1, 1)
        self.b1.config(image=self.file2)

        self.b2 = Button(self.fcenter, text=' ', bg='dark blue', padx=10, pady=10,command=self.gotopatient)
        self.b2.place(x=350, y=240)
        self.file3 = PhotoImage(file="patient2.png")
        self.b2.config(image=self.file3, compound=CENTER)
        self.file4 = self.file3.subsample(1, 1)
        self.b2.config(image=self.file4)

                                                        #On clicking the Doctor Button

    def onButton1(self):
        self.l2 = Label(text='Enter Username', bg='White')
        self.l2.place(x=260, y=530)

        self.l3 = Label(text='Enter Password', bg='white')
        self.l3.place(x=260, y=560)

        self.e1 = Entry(width=18, fg="black", bg="lavender", font=('arial', 14))
        self.e1.place(x=420, y=530)

        self.e2 = Entry(width=18, fg="black", bg="lavender", font=('arial', 14),show="*")
        self.e2.place(x=420, y=560)

        self.b3 = Button(text='Login', bg='darkblue', padx=25, pady=5, command=self.loginValidate)
        self.b3.place(x=290, y=630)

        self.b3 = Button(text='Register', bg='yellow', padx=25, pady=5, command=self.gotoregister)
        self.b3.place(x=400, y=630)

    # Checking the username and password from database for logging

    def loginValidate(self):
        user = self.e1.get()
        pwd = self.e2.get()
        if not self.e1.get() or not self.e2.get():
            m.showerror('Login Error',"Enter username and password")
        elif not self.e1.get():
            m.showerror('Login Error', "Enter username and password")
        elif not self.e2.get():
            m.showerror('Login Error', "Enter username and password")
        else:
            c.execute("SELECT * FROM userpwd WHERE username =? AND password = ?", (user, pwd))
            result = c.fetchall()

            if result:
                for i in result:
                    self.gotodoctor()
                    break
            else:
                m.showerror('Login Error',"Username or password not recognised")

        # Go to Register Frame

    def gotoregister(self):
        self.master.withdraw()
        self.newWindow1 = Toplevel(self.master)
        cc = Register(self.newWindow1)

            # Go to Patient Frame

    def gotopatient(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        bb = Patient(self.newWindow)

    def gotodoctor(self):
        self.master.withdraw()
        self.newWindow2 = Toplevel(self.master)
        bb = Doctor(self.newWindow2)

            # Patient Frame with all widgets

class Patient():

    def __init__(self, master):

        self.master = master
        self.ftop = Frame(self.master, width=800, height=100, bg='steelblue')
        self.ftop.pack(side=TOP, fill=X)
        self.fbottom = Frame(self.master, width=800, height=100, bg='steelblue')
        self.fbottom.pack(side=BOTTOM, fill=X)
        self.fleft = Frame(self.master, width=100, height=800, bg='steelblue')
        self.fleft.pack(side=LEFT, fill=Y)
        self.fright = Frame(self.master, width=100, height=800, bg='steelblue')
        self.fright.pack(side=RIGHT, fill=Y)

        self.fcenter = Canvas(self.master,width= 600, height= 600)
        self.fcenter.pack(expand=True, fill=BOTH)
        self.image1 = PhotoImage(file="patientframe.png")
        self.fcenter.img = self.image1
        self.fcenter.create_image(0, 0, anchor=NW, image=self.image1)

        self.label = Label(self.ftop, text="Healthcare", font=('Verdana', 50, 'bold'), bg='steelblue',fg='yellow')
        self.label.pack(side="top", fill="x", pady=10)
        #self.l2 = Label(self.fcenter, text='Enter your disease', bg='teal', font=('lato', 25, 'bold'))
        #self.l2.place(x=100, y=100)
        #self.e10 = Entry(self.fcenter, width=30, bg='lavender', font=('arial', 10))
        #self.e10.place(x=350, y=105)
        self.b = Button(self.fcenter, text="Search Medicine",padx=25,pady=5, fg="black", bg='yellow', font='Verdana',command=self.medicine)
        self.b.place(x=380, y=180)
        self.h = Button(self.fcenter, text="Search Hospitals",padx=25,pady=5, fg="black", bg='yellow', font='Verdana',command=self.local)
        self.h.place(x=80, y=180)
        self.home = Button(self.fcenter, text="Go Back",padx=25,pady=5, fg="black", bg='yellow', font='Verdana',command=self.new_window)
        self.home.place(x=250, y=250)

    def local(self):
        self.fcenter.pack_forget()
        self.fnew = Frame(self.master,bg="white",width=600,height=600)
        self.fnew.pack()

        c.execute('CREATE TABLE IF NOT EXISTS CLINIC (NAME VARCHAR(40), ADDRESS VARCHAR(40), AREA VARCHAR(20))')
        c.execute('INSERT INTO CLINIC(NAME, ADDRESS, AREA) VALUES ("Bhagwati_hospital", "SV-Road", "Borivali" )')
        c.execute('INSERT INTO CLINIC(NAME, ADDRESS, AREA) VALUES ("Sankalp_hospital", "LinkRoad", "Borivali" )')
        c.execute('INSERT INTO CLINIC(NAME, ADDRESS, AREA) VALUES ("Cooper_hospital", "Link-Road", "Malad" )')
        c.execute('INSERT INTO CLINIC(NAME, ADDRESS, AREA) VALUES ("SVP_hospital", "SV-Road", "Kandivali" )')
        con.commit()


        self.tilt = Label(self.fnew, text=' Hospital/Clinic near you' , font=('Verdana', 30, 'italic'), fg='blue',bg='white')
        self.tilt.place(x=100, y=50)
        self.ask = Label(self.fnew, text='Select Your Locality', fg='blue', font=('Verdana', 20, 'italic'),bg='white')
        self.ask.place(x=50, y=180)
        self.vt = StringVar()
        self.spin = Spinbox(self.fnew, values=('Borivali', 'Kandivali', 'Malad', 'Andheri'), textvariable=self.vt,width=25, fg='black', bg='lavender', font=('Verdana', 12, 'italic'))
        self.spin.place(x=350, y=180)
        # lst1 = ['Borivali', 'Kandivali', 'Malad', 'Goregaon', 'Andheri']
        # self.vt.set(lst1[0])
        # self.drop = OptionMenu(self.opt, self.vt,  *lst1)
        # self.drop.set('Borivali')
        # self.drop.place(x=390, y=180)
        self.search = Button(self.fnew, text='Search', bg='blue',padx=30, pady=5, font='Verdana',command=self.search1)
        self.search.place(x=200, y=275)
        self.home = Button(self.fnew, text="Go Back", padx=25, pady=5, fg="black", bg='yellow', font='Verdana',command=self.new_window)
        self.home.place(x=320, y=275)

    def search1(self):
        srt = self.spin.get()
        c.execute('SELECT * FROM CLINIC WHERE AREA=(?)', (srt,))
        result = c.fetchone()
        for i in result:
            print(result)
            break
        self.lb = Label(self.fnew,text='Hospital Location',font=('Roman',20,'bold underline'))
        self.lb.place(x=220,y=350)
        self.lr = Label(self.fnew, text=result,font=('Roman',20,'bold'),bg='lightgray')
        self.lr.pack(side=BOTTOM)
        self.lr.place(x=150, y=400)


    def medicine(self):
        self.fcenter.pack_forget()
        self.dat = Frame(self.master, bg="white", width=600, height=600)
        self.dat.pack()
        self.l2 = Label(self.dat, text='Enter your disease', bg='white', font=('lato', 30, 'bold'))
        self.l2.place(x=50, y=100)
        self.e10 = Entry(self.dat, width=25,bg='lavender', font=('arial', 15))
        self.e10.place(x=350, y=105)
        self.bsearch = Button(self.dat,text='Search',padx=25,pady=5,command=self.search)
        self.bsearch.place(x=200,y=200)
        self.bback = Button(self.dat,text='GoBack',padx=25,pady=5,command=self.new_window)
        self.bback.place(x=320,y=200)

    def search(self):
        v = self.e10.get()
        if not self.e10.get():
            m.showerror('Error','Enter Disease')
        else:
            c.execute("SELECT MEDICINE_NAME FROM PRESCRIBED  WHERE DISEASE_NAME=?", (v,))
            result = c.fetchall()
            for i in result:
                print(result)
                break
            self.lb = Label(self.dat, text='Medicine Prescribed', font=('Roman', 20, 'bold underline'))
            self.lb.place(x=220, y=300)
            self.lr = Label(self.dat, text=result,font=('Roman',15,'italic'),bg='lightgray')
            self.lr.place(x=280, y=350)
            c.execute("SELECT DOC_NAME FROM PRESCRIBED  WHERE DISEASE_NAME=?", (v,))
            result1 = c.fetchall()
            self.lb = Label(self.dat, text='Medicine Prescribed by Doctor', font=('Roman', 20, 'bold underline'))
            self.lb.place(x=150, y=400)
            self.lr = Label(self.dat, text=result1, font=('Roman', 15, 'italic'), bg='lightgray')
            self.lr.place(x=280, y=450)




            # Back to Main Frame
    def new_window(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        bb = Mains(self.newWindow)

                # Register Frame with all widgets

class Register():
    def __init__(self,master):

        self.master = master
        self.ftop = Canvas(self.master,width= 800, height= 100)
        self.image1 = PhotoImage(file="docframe.png")
        self.ftop.img = self.image1
        self.ftop.create_image(0, 0, anchor=NW, image=self.image1)
        self.ftop.pack(side=TOP, fill=X)

        self.fbottom = Canvas(self.master,width= 800, height= 100)
        self.image4 = PhotoImage(file="docframe.png")
        self.fbottom.img = self.image4
        self.fbottom.create_image(0,0,anchor=NW,image=self.image4)
        self.fbottom.pack(side=BOTTOM, fill=X)
        self.fleft = Canvas(self.master,width= 100, height= 600)
        self.image2 = PhotoImage(file="docframe.png")
        self.fleft.create_image(0, 0, anchor=NW, image=self.image2)
        self.fleft.pack(side=LEFT, fill=Y)
        self.fright = Canvas(self.master,width= 100, height= 600)
        self.image3 = PhotoImage(file="docframe.png")
        self.fright.create_image(0, 0, anchor=NW, image=self.image3)
        self.fright.pack(side=RIGHT, fill=Y)

            # Registration Form Details

        self.fcenter = Frame(self.master,width=600,height=600,bg='lightgray')
        self.fcenter.pack()

        self.lb = Label(self.ftop,text="Registration Form",font=("Roman",50),bg="white",fg='red')
        self.lb.place(x=220,y=30)

        self.l1 = Label(self.fcenter,text="Name:",font=('arial',20),bg='lightgray')
        self.l1.place(x=50,y=70)

        self.l2 = Label(self.fcenter,text='ID:',font=('arial',20),bg='lightgray')
        self.l2.place(x=50,y=110)

        self.l = Label(self.fcenter,text='Username:',font=('arial',20),bg='lightgray')
        self.l.place(x=50,y=150)

        self.l3 = Label(self.fcenter,text='Enter Your City:',font=('arial',20),bg='lightgray')
        self.l3.place(x=50,y=190)

        self.l4 = Label(self.fcenter, text='Select Your Gender:',font=('arial',20),bg='lightgray')
        self.l4.place(x=50,y=230)

        self.l5 = Label(self.fcenter,text='Enter Speciality:',font=('arial',20),bg='lightgray')
        self.l5.place(x=50,y=270)

        self.p = Label(self.fcenter,text='Enter password:',font=('arial',20),bg='lightgray')
        self.p.place(x=50,y=320)

        self.c = Label(self.fcenter,text='Confirm password:',font=('arial',20),bg='lightgray')
        self.c.place(x=50,y=370)

        self.ename = Entry(self.fcenter, width=30, font=('arial', 14),bg='lavender')
        self.ename.place(x=300,y=70)

        self.eid = Entry(self.fcenter, width=30, font=('arial', 14), bg='lavender')
        self.eid.place(x=300, y=110)

        self.euser = Entry(self.fcenter, width=30, font=('arial', 14), bg='lavender')
        self.euser.place(x=300, y=150)

        self.variable = StringVar(self.fcenter)
        self.variable.set("Choose")
        self.w = OptionMenu(self.fcenter, self.variable, "Mumbai", "Chennai", "Rajkot", "Surat")
        self.w.config(width=19)
        self.w.place(x=300, y=190)

        self.var = StringVar()
        self.r1 = Radiobutton(self.fcenter, text='Male',bg='lightgray', variable=self.var, value='M')
        self.r1.place(x=310,y=230)
        self.r2 = Radiobutton(self.fcenter, text='Female',bg='lightgray', variable=self.var, value='F')
        self.r2.place(x=400, y=230)

        self.espec = Entry(self.fcenter, width=30, font=('arial', 14), bg='lavender')
        self.espec.place(x=300, y=270)

        self.epass = Entry(self.fcenter, width=30, font=('arial', 14), bg='lavender',show='*')
        self.epass.place(x=300, y=320)

        self.cpass = Entry(self.fcenter, width=30, font=('arial', 14), bg='lavender',show='*')
        self.cpass.place(x=300, y=370)

        self.b = Button(self.fcenter, text="Submit", padx=25, pady=5, command=lambda: submit(self))
        self.b.place(x=200,y=450)

        self.b1 = Button(self.fcenter, text="Home",padx=30,pady=5,command=self.new_window1)
        self.b1.place(x=320, y=450)

            # Back to Main Frame

    def new_window1(self):
        self.master.withdraw()
        self.newWindow1 = Toplevel(self.master)
        cc = Mains(self.newWindow1)

class Doctor():
    def __init__(self,master):
        self.master = master
        self.fr = Frame(self.master, bg="cyan",width=800,height=800)
        self.fr.pack()
        self.label2 = Label(self.fr, text="Healthcare", font=('Verdana', 50, 'bold'), bg='cyan')
        self.label2.place(x=250,y=10)
        self.s = Label(self.fr, text='Doctor Name:', font=('Verdana', 25, 'bold'), bg='cyan')
        self.s.place(x=50, y=150)
        self.edoc = Entry(self.fr, width=30, font=('arial', 12),bg='lavender')
        self.edoc.place(x=200, y=200)
        self.s1 = Label(self.fr, text='Disease name:', font=('Verdana',25, 'bold'), bg='cyan')
        self.s1.place(x=50, y=250)
        #self.rr = StringVar()
        #self.rr.set('Enter disease name')
        self.ed = Entry(self.fr, width=30, font=('arial', 12),bg='lavender')
        self.ed.place(x=200, y=300)
        self.sl = Label(self.fr, text='Prescribe a medicine for disease', font=('Verdana', 25, 'bold'), bg='cyan')
        self.sl.place(x=50, y=350)
        # self.sl.pack()
        # self.mi = StringVar()
        # self.mi.set('Enter medicine name here')
        self.er = Entry(self.fr, width=30, font=('arial', 12),bg='lavender')
        self.er.place(x=200, y=400)
        self.save = Button(self.fr, text='Save', bg='yellow', fg='black', padx=25,pady=5, font=('Verdana', 12, 'bold'),command=lambda: data_entry(self))
        self.save.place(x=300, y=450)
        self.save = Button(self.fr, text='Logout', bg='yellow', fg='black', padx=25,pady=5, font=('Verdana', 12, 'bold'),command=self.new_window2)
        self.save.place(x=400, y=450)

    def new_window2(self):
        self.master.withdraw()
        self.newWindow2 = Toplevel(self.master)
        bb = Mains(self.newWindow2)

if __name__ == '__main__':
    root = Tk()
    root.title('Healthcare')
    b = Mains(root)
    root.mainloop()

