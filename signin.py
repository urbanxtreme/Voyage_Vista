from tkinter import *
from tkinter import messagebox
import pymysql
#functions
def clear():
    emailentry.delete(0,END)
    usernameentry.delete(0,END)
    passwordentry.delete(0,END)
    confirmpasswordentry.delete(0,END)
def connect_database():
    if emailentry.get()=="" or usernameentry.get()=="" or passwordentry.get()=="" or confirmpasswordentry.get()=="":
        messagebox.showerror("Error","All fields are required")
    elif passwordentry.get()!=confirmpasswordentry.get():
        messagebox.showerror("Error","Passwords doesn't match")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="19112005")
            mycursor=con.cursor()
        except:
            messagebox.showerror("Error","Database Connectivity issue, Try Again")
            return
        try:
            query = "create database handsign"
            mycursor.execute(query)
            query = "use handsign"
            mycursor.execute(query)
            query = "create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))"
            mycursor.execute(query)
        except:
            mycursor.execute("use handsign")
        query="select * from data where username=%s"
        mycursor.execute(query,(usernameentry.get()))
        row = mycursor.fetchone()
        query="select * from data where email=%s"
        mycursor.execute(query,(emailentry.get()))
        column=mycursor.fetchone()
        if row!=None:
            messagebox.showerror("Error","Username Already exists")
        elif column!=None:
            messagebox.showerror("Error","Email already exists")
        else:
            query = "insert into data(email,username,password) values(%s,%s,%s)"
            mycursor.execute(query, (emailentry.get(), usernameentry.get(), passwordentry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration Successful")
            clear()
            login_window.destroy()
def hide():
    openeye.config(file="closeye.png")
    passwordentry.config(show="*")
    eyeButton.config(command=show)
def show():
    openeye.config(file="openeye.png")
    passwordentry.config(show="")
    eyeButton.config(command=hide)
def hided():
    openeye1.config(file="closeye1.png")
    confirmpasswordentry.config(show="*")
    eyeButton1.config(command=showed)
def showed():
    openeye1.config(file="openeye1.png")
    confirmpasswordentry.config(show="")
    eyeButton1.config(command=hide)
def login():
    login_window.destroy()
    import loginpage
login_window=Tk()
icon =PhotoImage(file="icon.png")
login_window.iconphoto(True, icon)
login_window.geometry("1920x1080+0+2")
bgImage=PhotoImage(file="bg.png")
bgLabel=Label(login_window,image=bgImage).place(x=0,y=0,relwidth=1,relheight=1)
#login frame
Frame_login=Frame(login_window, bg="lemon chiffon",relief=SOLID)
Frame_login.place(x=500,y=200,width=500,height=400)
#Title and subs
title=Label(Frame_login,text="Sign in", font=("Impact",25,"bold","underline"),fg="yellow",bg="black")
title.place(x=180, y=30)
#mail
email= Label(Frame_login, text="E-mail:", font=("Algerian", 15), fg="navy",bg="alice blue")
email.place(x=0, y=110)
#entry box
emailentry= Entry(Frame_login, font=("Times New Roman", 15),bd=0, fg="dark blue",bg="ghost white")
emailentry.place(x=210, y=110, width=280, height=26)
#username
username= Label(Frame_login, text="USERNAME:", font=("Algerian", 15), fg="navy",bg="alice blue")
username.place(x=0, y=160)
# entry box
usernameentry = Entry(Frame_login, font=("Times New Roman", 15),bd=0, fg="dark blue",bg="ghost white")
usernameentry.place(x=210, y=160, width=280, height=26)
#password
password= Label(Frame_login, text="PASSWORD:", font=("Algerian", 15), fg="navy",bg="alice blue")
password.place(x=0, y=210)
# entry box
passwordentry= Entry(Frame_login, font=("Times New Roman", 15),bd=0, fg="dark blue",bg="ghost white")
passwordentry.place(x=210, y=210, width=280, height=26)
#confirm password
confirmpassword= Label(Frame_login, text="CONFIRM PASSWORD:", font=("Algerian", 15), fg="navy",bg="alice blue")
confirmpassword.place(x=0, y=260)
# entry box
confirmpasswordentry= Entry(Frame_login, font=("Times New Roman", 15),bd=0, fg="dark blue",bg="ghost white")
confirmpasswordentry.place(x=210, y=260, width=280, height=26)
#login label
loginlabel= Label(Frame_login, text="Already have an acccount?", font=("Open Sans", 9,"bold"), fg="black",bg="lemon chiffon")
loginlabel.place(x=150, y=370)
#buttons
#sign in
signinButton=Button(Frame_login,text="Sign In",font=("Open Sans",15,"bold"),bd=0,cursor="hand2",fg="white",bg="firebrick1",command=connect_database)
signinButton.place(x=215,y=310)
#login
loginbutton=Button(Frame_login,text="Login",font=("Open Sans",9,"bold underline"),bd=0,command=login,cursor="hand2",fg="blue",bg="lemon chiffon",activebackground="lemon chiffon",activeforeground="hot pink")
loginbutton.place(x=305,y=370)
#eye button
openeye=PhotoImage(file="openeye.png")
eyeButton=Button(Frame_login,image=openeye,bd=0,bg="ghost white",activebackground="ghost white",activeforeground="ghost white",cursor="hand2",command=hide)
eyeButton.place(x=460,y=210)
#eye button2
openeye1=PhotoImage(file="openeye1.png")
eyeButton1=Button(Frame_login,image=openeye1,bd=0,bg="ghost white",activebackground="ghost white",activeforeground="ghost white",cursor="hand2",command=hided)
eyeButton1.place(x=460,y=260)
login_window.mainloop()