from tkinter import *
from tkinter import messagebox
import pymysql

# functions
def clear():
    emailentry.delete(0, END)
    usernameentry.delete(0, END)
    passwordentry.delete(0, END)
    confirmpasswordentry.delete(0, END)

def connect_database():
    if emailentry.get() == "" or usernameentry.get() == "" or passwordentry.get() == "" or confirmpasswordentry.get() == "":
        messagebox.showerror("Error", "All fields are required")
    elif passwordentry.get() != confirmpasswordentry.get():
        messagebox.showerror("Error", "Passwords don't match")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="19112005")
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error", "Database Connectivity issue, Try Again")
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
        query = "select * from data where username=%s"
        mycursor.execute(query, (usernameentry.get(),))
        row = mycursor.fetchone()
        query = "select * from data where email=%s"
        mycursor.execute(query, (emailentry.get(),))
        column = mycursor.fetchone()
        if row is not None:
            messagebox.showerror("Error", "Username Already exists")
        elif column is not None:
            messagebox.showerror("Error", "Email already exists")
        else:
            query = "insert into data(email,username,password) values(%s,%s,%s)"
            mycursor.execute(query, (emailentry.get(), usernameentry.get(), passwordentry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration Successful")
            clear()
            login()

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
    eyeButton1.config(command=hided)

def login():
    login_window.destroy()
    import loginpage

login_window = Tk()
login_window.title("Voyage Vista")
login_window.resizable(False, False)
login_window.configure(bg="white")
login_window.geometry("360x640+600+100")


# login frame
Frame_login = Frame(login_window, bg="white", relief=SOLID)
Frame_login.place(x=20, y=100, width=320, height=440)

# Title and subs
title = Label(Frame_login, text="Sign in", font=("Poppins", 20, "bold"), fg="#590A59", bg="white")
title.place(x=120, y=20)

# mail
email = Label(Frame_login, text="E-mail:", font=("Poppins", 12), fg="navy", bg="white")
email.place(x=20, y=80)
# entry box
emailentry = Entry(Frame_login, font=("Times New Roman", 12), bd=0, fg="dark blue", bg="ghost white")
emailentry.place(x=120, y=80, width=180, height=26)

# username
username = Label(Frame_login, text="Username:", font=("Poppins", 12), fg="navy", bg="white")
username.place(x=20, y=120)
# entry box
usernameentry = Entry(Frame_login, font=("Times New Roman", 12), bd=0, fg="dark blue", bg="ghost white")
usernameentry.place(x=120, y=120, width=180, height=26)

# password
password = Label(Frame_login, text="Password:", font=("Poppins", 12), fg="navy", bg="white")
password.place(x=20, y=160)
# entry box
passwordentry = Entry(Frame_login, font=("Times New Roman", 12), bd=0, fg="dark blue", bg="ghost white")
passwordentry.place(x=120, y=160, width=180, height=26)

# eye button
openeye = PhotoImage(file="openeye.png")
eyeButton = Button(Frame_login, image=openeye, bd=0, cursor="hand2", bg="alice blue", command=hide)
eyeButton.place(x=275, y=160)

# confirm password
confirmpassword = Label(Frame_login, text="Confirm:", font=("Poppins", 12), fg="navy", bg="white")
confirmpassword.place(x=20, y=200)
# entry box
confirmpasswordentry = Entry(Frame_login, font=("Times New Roman", 12), bd=0, fg="dark blue", bg="ghost white")
confirmpasswordentry.place(x=120, y=200, width=180, height=26)

# eye button
openeye1 = PhotoImage(file="openeye1.png")
eyeButton1 = Button(Frame_login, image=openeye1, bd=0, cursor="hand2", bg="alice blue", command=hided)
eyeButton1.place(x=275, y=200)

# sign in button
signinButton = Button(Frame_login, text="Sign In", font=("Open Sans", 15, "bold"), bd=0, cursor="hand2", fg="#590A59", bg="white", command=connect_database)
signinButton.place(x=120, y=320)

loginlabel = Label(Frame_login, text="Already have an acccount?", font=("Poppins", 9), fg="#590A59", bg="white")
loginlabel.place(x=50, y=355)

# sign up button
signupButton = Button(Frame_login, text="Login", font=("Poppins", 8, "bold underline"), bd=0, cursor="hand2", fg="blue", bg="white", activebackground="lemon chiffon", activeforeground="hot pink", command=login)
signupButton.place(x=210, y=355)

login_window.mainloop()
