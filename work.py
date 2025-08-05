import tkinter as tk
from tkinter import messagebox

class LoginSignUpPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Login/Sign Up")
        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack()

        # Login/Sign Up widgets and functionality
        self.username_label = tk.Label(self.login_frame, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()
        self.password_label = tk.Label(self.login_frame, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack()
        self.sign_up_button = tk.Button(self.login_frame, text="Sign Up", command=self.sign_up)
        self.sign_up_button.pack()

    def login(self):
        # Login functionality
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Check if username and password are correct
        if username == "admin" and password == "password":
            self.login_frame.destroy()
            MainMenuPage(self.master)
        else:
            messagebox.showerror("Invalid Credentials", "Username or password is incorrect")

    def sign_up(self):
        # Sign Up functionality
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Create a new user
        # For simplicity, we'll just store the username and password in a dictionary
        users = {"admin": "password"}
        users[username] = password
        self.login_frame.destroy()
        MainMenuPage(self.master)

class MainMenuPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Voyage Vista")
        self.main_menu_frame = tk.Frame(self.master)
        self.main_menu_frame.pack()

        # Main Menu widgets and functionality
        self.plan_trip_button = tk.Button(self.main_menu_frame, text="Plan Trip", command=self.plan_trip)
        self.plan_trip_button.pack()
        self.book_ticket_button = tk.Button(self.main_menu_frame, text="Book Ticket", command=self.book_ticket)
        self.book_ticket_button.pack()
        self.trip_planner_label = tk.Label(self.main_menu_frame, text="")
        self.trip_planner_label.pack()
        self.tagline_label = tk.Label(self.main_menu_frame, text="")
        self.tagline_label.pack()

        self.animate_title()
        self.animate_tagline()

    def plan_trip(self):
        # Plan Trip functionality
        pass

    def book_ticket(self):
        # Book Ticket functionality
        pass

    def animate_title(self):
        title = "Voyage Vista"
        for i in range(len(title)):
            self.trip_planner_label.config(text=title[:i+1])
            self.master.update()
            self.master.after(100)

    def animate_tagline(self):
        tagline = "Plan Your Dream Trip"
        for i in range(len(tagline)):
            self.tagline_label.config(text=tagline[:i+1])
            self.master.update()
            self.master.after(100)

root = tk.Tk()
login_page = LoginSignUpPage(root)
root.mainloop()