import tkinter as tk
from PIL import Image, ImageTk

class RoundedButton(tk.Canvas):
    def __init__(self, master, text, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.text = text
        self.create_rounded_button()
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def create_rounded_button(self):
        self.delete("all")  # Clear any existing items

        # Draw rounded rectangle
        self.create_arc((10, 10, 50, 50), start=90, extent=90, outline='', fill='#590A59')
        self.create_arc((self.winfo_reqwidth() - 50, 10, self.winfo_reqwidth() - 10, 50), start=0, extent=90, outline='', fill='#590A59')
        self.create_arc((10, self.winfo_reqheight() - 50, 50, self.winfo_reqheight() - 10), start=180, extent=90, outline='', fill='#590A59')
        self.create_arc((self.winfo_reqwidth() - 50, self.winfo_reqheight() - 50, self.winfo_reqwidth() - 10, self.winfo_reqheight() - 10), start=270, extent=90, outline='', fill='#590A59')
        self.create_rectangle((10, 25, self.winfo_reqwidth() - 10, self.winfo_reqheight() - 25), outline='', fill='#590A59')
        self.create_rectangle((25, 10, self.winfo_reqwidth() - 25, self.winfo_reqheight() - 10), outline='', fill='#ffffff')

        # Draw text
        self.create_text(self.winfo_reqwidth() / 2, self.winfo_reqheight() / 2, text=self.text, font=("Arial", 18, "bold"), fill='#590A59')

    def on_click(self, event):
        if self.command:
            self.command()

    def on_enter(self, event):
        self.config(bg='#E3DD2B')

    def on_leave(self, event):
        self.config(bg='#590A59')

class VoyageVistaWindow:
    def __init__(self, master):
        self.master = master
        master.title("Voyage Vista")
        master.resizable(False, False)
        master.geometry("360x640+600+100")  # Typical Android phone screen size
        master.iconphoto(True, tk.PhotoImage(file='voyage_vista_icon.png'))  # Set window icon

        # Set background color to white
        master.configure(bg="white")

        # Create a frame for the title
        title_frame = tk.Frame(master, bg="white")
        title_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create a label for the title "Voyage"
        self.voyage_label = tk.Label(title_frame, text="VOYAGE", font=("Aharoni", 30, "bold"), fg="#590A59", bg="white")
        self.voyage_label.pack(side=tk.TOP)

        # Create a label for the title "Vista"
        self.vista_label = tk.Label(title_frame, text="VISTA", font=("Arial", 30, "bold"), fg="#590A59", bg="white")
        self.vista_label.pack(side=tk.TOP)

        # Create a label for the tagline
        self.tagline_label = tk.Label(master, text="Explore the Horizon", font=("Arial", 18), fg="#590A59", bg="white")
        self.tagline_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Create rounded buttons directly on the master window
        self.start_button = RoundedButton(master, text="Start Your Journey", command=self.func, width=320, height=60, bg="#590A59")
        self.start_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.settings_button = RoundedButton(master, text="Settings", command=self.open_settings_window, width=320, height=60, bg="#590A59")
        self.settings_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.about_button = RoundedButton(master, text="About Us", command=self.open_about_window, width=320, height=60, bg="#590A59")
        self.about_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Add a feedback button
        self.feedback_button = RoundedButton(master, text="Feedback", command=self.open_feedback_window, width=320, height=60, bg="#590A59")
        self.feedback_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        # Create a frame for the footer
        footer_frame = tk.Frame(master, bg="#3498db")
        footer_frame.pack(fill="x", side=tk.BOTTOM)  # Pack at the bottom

        # Create a label for the footer
        footer_label = tk.Label(footer_frame, text="\u00A9 2024 Voyage Vista", font=("Arial", 12), fg="#ffffff", bg="#590A59")
        footer_label.pack(fill="x")  # Fill horizontally

    def func(self):
        self.master.destroy()
        import new

    def open_settings_window(self):
        # Placeholder for opening settings window
        print("Settings button clicked")

    def open_about_window(self):
        # Placeholder for opening about window
        print("About Us button clicked")

    def open_feedback_window(self):
        # Create a new Tkinter window for feedback
        feedback_window = tk.Toplevel(self.master)
        feedback_window.title("Feedback Form")
        feedback_window.geometry("400x300")
        feedback_window.resizable(False, False)  # Disable resizing

        # Create a frame for the feedback form elements
        feedback_frame = tk.Frame(feedback_window, padx=10, pady=10, bg="cyan")
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
        tk.Label(feedback_frame, text="We value your feedback!", font=("Arial", 16), bg="cyan").grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="n")

        # Name Entry
        tk.Label(feedback_frame, text="Name:", font=("Arial", 12), bg="cyan").grid(row=1, column=0, padx=5, pady=(5, 0), sticky="e")
        name_entry = tk.Entry(feedback_frame, font=("Arial", 12))
        name_entry.insert(0, "Enter your name")
        name_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Enter your name"))
        name_entry.bind("<FocusOut>", lambda event: self.set_placeholder(event, "Enter your name"))
        name_entry.grid(row=1, column=1, padx=5, pady=(5, 0), sticky="ew")

        # Email Entry
        tk.Label(feedback_frame, text="Email:", font=("Arial", 12), bg="cyan").grid(row=2, column=0, padx=5, pady=(5, 0), sticky="e")
        email_entry = tk.Entry(feedback_frame, font=("Arial", 12))
        email_entry.insert(0, "Enter your email")
        email_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Enter your email"))
        email_entry.bind("<FocusOut>", lambda event: self.set_placeholder(event, "Enter your email"))
        email_entry.grid(row=2, column=1, padx=5, pady=(5, 0), sticky="ew")

        # Feedback Text Box
        tk.Label(feedback_frame, text="Feedback:", font=("Arial", 12), bg="cyan").grid(row=3, column=0, padx=5, pady=(5, 0), sticky="ne")
        feedback_text = tk.Text(feedback_frame, font=("Arial", 12), height=5)
        feedback_text.insert("1.0", "Enter your feedback here...")
        feedback_text.bind("<FocusIn>", lambda event: self.clear_placeholder_text(event, "Enter your feedback here..."))
        feedback_text.bind("<FocusOut>", lambda event: self.set_placeholder_text(event, "Enter your feedback here..."))
        feedback_text.grid(row=3, column=1, padx=5, pady=(5, 10), sticky="nsew")

        # Add the Submit Feedback button at the bottom center
        submit_button = tk.Button(feedback_frame, text="Submit Feedback", font=("Arial", 14), bg="#2ecc71", fg="#ffffff",
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
            tk.messagebox.showwarning("Input Error", "Please fill out all fields.")
            return

        # In a real application, you might save this feedback to a database or send it via email
        # For now, we'll just show a confirmation message
        tk.messagebox.showinfo("Feedback Received", "Thank you for your feedback!")

        # Clear the form
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        feedback_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    my_window = VoyageVistaWindow(root)
    root.mainloop()
