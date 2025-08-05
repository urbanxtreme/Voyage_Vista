import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import planning  # Ensure planning is correctly imported

class TripPlannerWindow:
    def __init__(self, master):
        self.master = master
        master.title("Voyage Vista")
        master.resizable(False, False)
        master.geometry("360x640+600+100")  # Typical Android phone screen size
        master.iconphoto(True, tk.PhotoImage(file='voyage_vista_icon.png'))  # Set window icon

        # Add a background image
        master.configure(bg="white")

        # Create a frame for the title
        title_frame = tk.Frame(master, bg="white")
        title_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create a label for the title "Trip Planner"
        self.trip_planner_label = tk.Label(title_frame, text="", font=("Aharoni", 30, "bold"), fg="#590A59", bg="white")
        self.trip_planner_label.pack(side=tk.TOP)

        # Create a label for the tagline
        self.tagline_label = tk.Label(master, text="", font=("Arial", 18), fg="#590A59", bg="white")
        self.tagline_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Create buttons directly on the master window
        self.plan_trip_button = tk.Button(master, text="Plan a Trip", font=("Arial", 18), fg="#ffffff", bg="#590A59", command=self.plan_trip_func, relief="raised", borderwidth=5)
        self.plan_trip_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER, relwidth=0.8)

        self.book_ticket_button = tk.Button(master, text="Book Ticket", font=("Arial", 18), fg="#ffffff", bg="#590A59", command=self.book_ticket_func, relief="raised", borderwidth=5)
        self.book_ticket_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.8)

        self.view_profile_button = tk.Button(master, text="View Profile", font=("Arial", 18), fg="#ffffff", bg="#590A59", command=self.view_profile_func, relief="raised", borderwidth=5)
        self.view_profile_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER, relwidth=0.8)

        # Add a feedback button
        self.feedback_button = tk.Button(master, text="Feedback", font=("Arial", 18), fg="#ffffff", bg="#590A59", command=self.open_feedback_window, relief="raised", borderwidth=5)
        self.feedback_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER, relwidth=0.8)

        # Add some animations to the buttons
        self.plan_trip_button.bind("<Enter>", self.on_enter_plan_trip)
        self.plan_trip_button.bind("<Leave>", self.on_leave_plan_trip)

        self.book_ticket_button.bind("<Enter>", self.on_enter_book_ticket)
        self.book_ticket_button.bind("<Leave>", self.on_leave_book_ticket)

        self.view_profile_button.bind("<Enter>", self.on_enter_view_profile)
        self.view_profile_button.bind("<Leave>", self.on_leave_view_profile)

        self.feedback_button.bind("<Enter>", self.on_enter_feedback)
        self.feedback_button.bind("<Leave>", self.on_leave_feedback)

        # Create a frame for the footer
        footer_frame = tk.Frame(master, bg="#3498db")
        footer_frame.pack(fill="x", side=tk.BOTTOM)  # Pack at the bottom

        # Create a label for the footer
        footer_label = tk.Label(footer_frame, text="\u00A9 2024 Trip Planner", font=("Arial", 12), fg="#ffffff", bg="#590A59")
        footer_label.pack(fill="x")  # Fill horizontally

        # Add some animations to the title and tagline
        self.animate_title("Voyage Vista", self.trip_planner_label, 0, 100)
        self.animate_title("Plan Your Dream Trip", self.tagline_label, 0, 200)

    def plan_trip_func(self):
        self.master.withdraw()  # Hide the main menu window
        self.open_planner_window()

    def open_planner_window(self):
        # Create a new Tkinter window for the planner
        planner_root = tk.Toplevel(self.master)
        planner_root.title("Voyage Vista")
        planner_root.geometry("360x640+600+100")  # Same size as the original window

        # Initialize the VoyageVistaWindow class
        planner_app = planning.VoyageVistaWindow(planner_root)
        planner_root.mainloop()

    def open_feedback_window(self):
        # Create a new Tkinter window for feedback
        feedback_window = tk.Toplevel(self.master)
        feedback_window.title("Feedback Form")
        feedback_window.geometry("400x300")
        feedback_window.resizable(False, False)  # Disable resizing

        # Create a frame for the feedback form elements
        feedback_frame = tk.Frame(feedback_window, padx=10, pady=10)
        feedback_frame.pack(fill=tk.BOTH, expand=True)

        # Create labels and entry fields for feedback using grid layout
        feedback_frame.grid_rowconfigure(0, weight=1)
        feedback_frame.grid_rowconfigure(1, weight=1)
        feedback_frame.grid_rowconfigure(2, weight=1)
        feedback_frame.grid_rowconfigure(3, weight=1)
        feedback_frame.grid_rowconfigure(4, weight=0)  # Row for the submit button
        feedback_frame.grid_columnconfigure(0, weight=1)
        feedback_frame.grid_columnconfigure(1, weight=1)

        # Title Label
        tk.Label(feedback_frame, text="We value your feedback!", font=("Arial", 16)).grid(row=0, column=0, columnspan=2,
                                                                                          pady=(0, 10), sticky="n")

        # Name Entry
        tk.Label(feedback_frame, text="Name:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=(5, 0),
                                                                        sticky="e")
        name_entry = tk.Entry(feedback_frame, font=("Arial", 12))
        name_entry.insert(0, "Enter your name")
        name_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Enter your name"))
        name_entry.bind("<FocusOut>", lambda event: self.set_placeholder(event, "Enter your name"))
        name_entry.grid(row=1, column=1, padx=5, pady=(5, 0), sticky="ew")

        # Email Entry
        tk.Label(feedback_frame, text="Email:", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=(5, 0),
                                                                         sticky="e")
        email_entry = tk.Entry(feedback_frame, font=("Arial", 12))
        email_entry.insert(0, "Enter your email")
        email_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Enter your email"))
        email_entry.bind("<FocusOut>", lambda event: self.set_placeholder(event, "Enter your email"))
        email_entry.grid(row=2, column=1, padx=5, pady=(5, 0), sticky="ew")

        # Feedback Text Box
        tk.Label(feedback_frame, text="Feedback:", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=(5, 0),
                                                                            sticky="ne")
        feedback_text = tk.Text(feedback_frame, font=("Arial", 12), height=5)
        feedback_text.insert("1.0", "Enter your feedback here...")
        feedback_text.bind("<FocusIn>", lambda event: self.clear_placeholder_text(event, "Enter your feedback here..."))
        feedback_text.bind("<FocusOut>", lambda event: self.set_placeholder_text(event, "Enter your feedback here..."))
        feedback_text.grid(row=3, column=1, padx=5, pady=(5, 10), sticky="nsew")

        # Add the Submit Feedback button at the bottom center
        submit_button = tk.Button(feedback_frame, text="Submit Feedback", font=("Arial", 14), bg="#2ecc71",
                                  fg="#ffffff",
                                  command=lambda: self.submit_feedback(name_entry, email_entry, feedback_text))
        submit_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="s")

        # Ensure proper expansion of the text box
        feedback_frame.grid_rowconfigure(3, weight=1)

    def clear_placeholder(self, event, placeholder_text):
        entry = event.widget
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def set_placeholder(self, event, placeholder_text):
        entry = event.widget
        if not entry.get():
            entry.insert(0, placeholder_text)
            entry.config(fg='gray')

    def clear_placeholder_text(self, event, placeholder_text):
        text_widget = event.widget
        if text_widget.get("1.0", tk.END).strip() == placeholder_text:
            text_widget.delete("1.0", tk.END)
            text_widget.config(fg='black')

    def set_placeholder_text(self, event, placeholder_text):
        text_widget = event.widget
        if not text_widget.get("1.0", tk.END).strip():
            text_widget.insert("1.0", placeholder_text)
            text_widget.config(fg='gray')

    def submit_feedback(self, name_entry, email_entry, feedback_text):
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        feedback = feedback_text.get("1.0", tk.END).strip()

        if not name or not email or not feedback:
            messagebox.showwarning("Input Error", "Please fill out all fields.")
            return

        # In a real application, you might save this feedback to a database or send it via email
        # For now, we'll just show a confirmation message
        messagebox.showinfo("Feedback Received", "Thank you for your feedback!")

        # Clear the form
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        feedback_text.delete("1.0", tk.END)

    def book_ticket_func(self):
        # Add your code here for booking a ticket
        pass

    def view_profile_func(self):
        # Add your code here to view profile
        pass

    def on_enter_plan_trip(self, event):
        self.plan_trip_button.config(relief="sunken", bg="#1abc9c")

    def on_leave_plan_trip(self, event):
        self.plan_trip_button.config(relief="raised", bg="#2ecc71")

    def on_enter_book_ticket(self, event):
        self.book_ticket_button.config(relief="sunken", bg="#7f8c8d")

    def on_leave_book_ticket(self, event):
        self.book_ticket_button.config(relief="raised", bg="#8e44ad")

    def on_enter_view_profile(self, event):
        self.view_profile_button.config(relief="sunken", bg="#2980b9")

    def on_leave_view_profile(self, event):
        self.view_profile_button.config(relief="raised", bg="#3498db")

    def on_enter_feedback(self, event):
        self.feedback_button.config(relief="sunken", bg="#c0392b")

    def on_leave_feedback(self, event):
        self.feedback_button.config(relief="raised", bg="#e74c3c")

    def animate_title(self, text, label, idx, delay):
        if idx < len(text) and label.winfo_exists():
            label.config(text=text[:idx + 1])
            self.master.after(delay, self.animate_title, text, label, idx + 1, delay)


if __name__ == "__main__":
    root = tk.Tk()
    my_window = TripPlannerWindow(root)
    root.mainloop()
