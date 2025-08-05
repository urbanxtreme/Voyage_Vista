import smtplib
from tkinter import *
from tkinter import messagebox
import pymysql
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the sign function
def sign():
    root.destroy()
    import new  # Ensure 'new' module is present

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Voyage Vista")
        self.root.resizable(False, False)
        icon = PhotoImage(file="voyage_vista_icon.png")
        root.iconphoto(True, icon)
        self.root.geometry("360x640+600+100")  # Adjusted for mobile screen size

        self.root.configure(bg="white")

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=30, y=100, width=300, height=400)

        title = Label(Frame_login, text="LOGIN MENU", font=("Poppins", 20, "bold"), fg="#590A59", bg="white")
        title.place(x=55, y=20)

        username = Label(Frame_login, text="E-mail:", font=("Poppins", 12), fg="navy", bg="white")
        username.place(x=15, y=100)

        self.usernameentry = Entry(Frame_login, font=("Times New Roman", 12), fg="dark blue")
        self.usernameentry.place(x=100, y=100, width=180, height=20)

        password = Label(Frame_login, text="Password:", font=("Poppins", 11), fg="navy", bg="white")
        password.place(x=15, y=170)

        self.passwordentry = Entry(Frame_login, font=("Times New Roman", 12), fg="dark blue", show='*')
        self.passwordentry.place(x=100, y=170, width=180, height=20)

        forgot_password = Button(Frame_login, cursor="hand2", command=self.forgotpswd, text="FORGOT PASSWORD?", bd=0, font=("Goudy old style", 8, "bold"), fg="#590A59", bg="white")
        forgot_password.place(x=165, y=190)

        submit = Button(Frame_login, command=self.check_function, cursor="hand2", text="LOGIN", bd=0, font=("Bubbly", 14, "bold"), fg="#590A59", bg="white", activebackground="magenta", activeforeground="black")
        submit.place(x=110, y=290)

        sign_inlabel = Label(Frame_login, text="Don't have an account?", font=("Open Sans", 8, "bold"), fg="#590A59", bg="white")
        sign_inlabel.place(x=60, y=325)

        sign_upbutton = Button(Frame_login, text="Sign In", font=("Open Sans", 8, "bold underline"), command=sign, bd=0, cursor="hand2", fg="blue", bg="white", activebackground="lemon chiffon", activeforeground="hot pink")
        sign_upbutton.place(x=190, y=325)

    def check_function(self):
        if self.usernameentry.get() == "" or self.passwordentry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="19112005", database="handsign")
                mycursor = con.cursor()
                query = "SELECT * FROM data WHERE email=%s AND password=%s"
                mycursor.execute(query, (self.usernameentry.get(), self.passwordentry.get()))
                row = mycursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    messagebox.showinfo("Welcome User", "Login Successful")
                    self.root.destroy()
                    # Execute main_menu.py
                    self.open_main_menu()
            except pymysql.err.OperationalError as e:
                messagebox.showerror("Error", f"Connection failed: {e}", parent=self.root)
            finally:
                if con:
                    con.close()

    def open_main_menu(self):
        import main_menu
        # Create the root window for the main menu
        main_menu_root = Tk()
        # Initialize the main menu with the newly created root window
        main_menu_app = main_menu.TripPlannerWindow(main_menu_root)
        # Run the main menu window
        main_menu_root.mainloop()

    def forgotpswd(self):
        def fetch_password(email):
            try:
                connection = pymysql.connect(host='localhost', user='root', password='19112005', database='handsign')
                cursor = connection.cursor()
                sql_query = "SELECT password FROM data WHERE email = %s"
                cursor.execute(sql_query, (email,))
                row = cursor.fetchone()
                cursor.close()
                connection.close()
                if row is None:
                    return None
                else:
                    return row[0]
            except pymysql.Error as e:
                print("Error:", e)
                return None

        def send_email(subject, message, to_email):
            email = "skrhari2020@gmail.com"
            password = "aueq tfzq qypp sxee"
            sender_email = email
            receiver_email = to_email
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()

        email = self.usernameentry.get()
        password = fetch_password(email)
        if password is not None:
            send_email("Your Password", password, email)
            messagebox.showinfo("Password Sent", "Your password has been sent to your email id")
        else:
            messagebox.showerror("Error", "Email not registered, Sign-in to create an account")

root = Tk()
obj = Login(root)
root.mainloop()
