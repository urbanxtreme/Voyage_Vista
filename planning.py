import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
from datetime import datetime, timedelta

class VoyageVistaWindow:
    def __init__(self, master):
        self.master = master
        master.title("Voyage Vista")
        image = Image.open('voyage_vista_icon.png')
        photo = ImageTk.PhotoImage(image)
        master.iconphoto(True, photo)
        master.resizable(False, False)
        master.geometry("360x640+600+100")  # Typical Android phone screen size

        # Load and set the background image
        self.bg_image = Image.open("1.jpg")
        self.bg_image = self.bg_image.resize((360, 640), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a label to hold the background image
        self.bg_label = tk.Label(master, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Create a frame for the form
        form_frame = tk.Frame(master, bg="light pink", padx=10, pady=10)
        form_frame.pack(pady=(20, 0))  # Adjusted padding to move it up

        # Configure the grid in the form frame
        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        # Create labels and entry fields for arrival, checkpoint, and dropping location
        self.arrival_label = tk.Label(form_frame, text="Arrival Location:", font=("Arial", 10), bg="light pink", fg="#000000")
        self.arrival_label.grid(row=0, column=0, pady=5, sticky=tk.W)
        self.arrival_entry = tk.Entry(form_frame, font=("Arial", 10), bd=2, relief="solid")
        self.arrival_entry.grid(row=0, column=1, pady=5, sticky=tk.EW)

        self.checkpoint_label = tk.Label(form_frame, text="Checkpoint (optional):", font=("Arial", 10), bg="light pink", fg="#000000")
        self.checkpoint_label.grid(row=1, column=0, pady=5, sticky=tk.W)
        self.checkpoint_entry = tk.Entry(form_frame, font=("Arial", 10), bd=2, relief="solid")
        self.checkpoint_entry.grid(row=1, column=1, pady=5, sticky=tk.EW)

        self.drop_label = tk.Label(form_frame, text="Dropping Location:", font=("Arial", 10), bg="light pink", fg="#000000")
        self.drop_label.grid(row=2, column=0, pady=5, sticky=tk.W)
        self.drop_entry = tk.Entry(form_frame, font=("Arial", 10), bd=2, relief="solid")
        self.drop_entry.grid(row=2, column=1, pady=5, sticky=tk.EW)

        # Create labels and entry fields for time
        self.time_label = tk.Label(form_frame, text="Time (HH:MM:SS):", font=("Arial", 10), bg="light pink", fg="#000000")
        self.time_label.grid(row=3, column=0, pady=5, sticky=tk.W)
        self.time_entry = tk.Entry(form_frame, font=("Arial", 10), bd=2, relief="solid")
        self.time_entry.grid(row=3, column=1, pady=5, sticky=tk.EW)

        # Create labels and dropdown for luggage
        self.luggage_label = tk.Label(form_frame, text="Luggage:", font=("Arial", 10), bg="light pink", fg="#000000")
        self.luggage_label.grid(row=4, column=0, pady=5, sticky=tk.W)

        self.luggage_var = tk.StringVar(form_frame)
        self.luggage_var.set("Normal quantity luggage")  # Default value

        self.luggage_dropdown = tk.OptionMenu(form_frame, self.luggage_var, "Normal quantity luggage", "Medium quantity luggage", "Heavy quantity luggage")
        self.luggage_dropdown.config(font=("Arial", 10), bg="light pink", relief="solid")
        self.luggage_dropdown.grid(row=4, column=1, pady=5, sticky=tk.EW)

        # Create a frame for the search button
        button_frame = tk.Frame(master, bg="light pink")
        button_frame.pack(side=tk.BOTTOM, fill="x")  # Adjusted to stick to the bottom

        # Create a search button with a modern look
        self.search_button = tk.Button(button_frame, text="Search", font=("Arial", 14), fg="#ffffff", bg="#2ecc71", relief="flat", padx=20, pady=5, command=self.search_data)
        self.search_button.pack(pady=(0, 10), fill="x")  # Added some padding to look better at the bottom

    def search_data(self):
        arrival_location = self.arrival_entry.get().strip()
        checkpoint_location = self.checkpoint_entry.get().strip()
        dropping_location = self.drop_entry.get().strip()
        time = self.time_entry.get().strip()
        luggage = self.luggage_var.get()

        if not arrival_location or not dropping_location or not time:
            messagebox.showwarning("Input Error", "Please enter arrival location, dropping location, and time.")
            return

        # Validate time format
        try:
            datetime.strptime(time, "%H:%M:%S")
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid time in HH:MM:SS format.")
            return

        # Database connection and data retrieval
        conn = None
        try:
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="19112005",
                database="school"
            )

            cursor = conn.cursor()

            # Update the arrtime field with the user's input time
            update_query = """UPDATE students
                              SET arrtime = %s
                              WHERE pickuploc = %s AND droploc = %s"""
            cursor.execute(update_query, (time, arrival_location, dropping_location))
            conn.commit()

            # Fetch data for the first leg of the journey
            query1 = """SELECT company, pickuploc, droploc, price, trtime, name, arrtime
                       FROM students
                       WHERE pickuploc = %s AND droploc = %s"""
            cursor.execute(query1, (arrival_location, checkpoint_location if checkpoint_location else dropping_location))
            rows1 = cursor.fetchall()

            # Calculate and update ttime for each record in the first leg
            for row in rows1:
                company, pickuploc, droploc, price, trtime, name, arrtime = row

                arrtime_dt = datetime.strptime(arrtime, "%H:%M:%S") if isinstance(arrtime, str) else datetime.strptime(
                    "00:00:00", "%H:%M:%S")
                trtime_td = datetime.strptime(trtime, "%H:%M:%S") - datetime.strptime("00:00:00",
                                                                                      "%H:%M:%S") if isinstance(trtime,
                                                                                                                str) else timedelta(
                    0)

                # Calculate total time
                total_time_td = arrtime_dt + trtime_td
                total_time = total_time_td.time().strftime("%H:%M:%S")

                update_ttime_query = """UPDATE students
                                        SET ttime = %s
                                        WHERE pickuploc = %s AND droploc = %s AND arrtime = %s"""
                cursor.execute(update_ttime_query, (total_time, arrival_location, checkpoint_location if checkpoint_location else dropping_location, arrtime))
                conn.commit()

            # Fetch updated data for the first leg
            query1 = """SELECT company, pickuploc, droploc, price, ttime, name
                       FROM students
                       WHERE pickuploc = %s AND droploc = %s"""
            cursor.execute(query1, (arrival_location, checkpoint_location if checkpoint_location else dropping_location))
            rows1 = cursor.fetchall()

            # If checkpoint is provided, fetch data for the second leg of the journey
            if checkpoint_location:
                query2 = """SELECT company, pickuploc, droploc, price, trtime, name, arrtime
                           FROM students
                           WHERE pickuploc = %s AND droploc = %s"""
                cursor.execute(query2, (checkpoint_location, dropping_location))
                rows2 = cursor.fetchall()

                # Calculate and update ttime for each record in the second leg
                for row in rows2:
                    company, pickuploc, droploc, price, trtime, name, arrtime = row

                    arrtime_dt = datetime.strptime(arrtime, "%H:%M:%S") if isinstance(arrtime, str) else datetime.strptime(
                        "00:00:00", "%H:%M:%S")
                    trtime_td = datetime.strptime(trtime, "%H:%M:%S") - datetime.strptime("00:00:00",
                                                                                          "%H:%M:%S") if isinstance(trtime,
                                                                                                                    str) else timedelta(
                        0)

                    # Calculate total time
                    total_time_td = arrtime_dt + trtime_td
                    total_time = total_time_td.time().strftime("%H:%M:%S")

                    update_ttime_query = """UPDATE students
                                            SET ttime = %s
                                            WHERE pickuploc = %s AND droploc = %s AND arrtime = %s"""
                    cursor.execute(update_ttime_query, (total_time, checkpoint_location, dropping_location, arrtime))
                    conn.commit()

                # Fetch updated data for the second leg
                query2 = """SELECT company, pickuploc, droploc, price, ttime, name
                           FROM students
                           WHERE pickuploc = %s AND droploc = %s"""
                cursor.execute(query2, (checkpoint_location, dropping_location))
                rows2 = cursor.fetchall()
            else:
                rows2 = []

            self.show_data(rows1, rows2)
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"Database error occurred: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            if conn:
                conn.close()

    def show_data(self, rows1, rows2):
        result_window = tk.Toplevel(self.master)
        result_window.title("Available Trips")
        result_window.geometry("600x600")

        canvas = tk.Canvas(result_window, bg="light pink")
        scrollbar = tk.Scrollbar(result_window, orient="vertical", command=canvas.yview)

        data_frame = tk.Frame(canvas, bg="light pink", padx=10, pady=10)
        canvas.create_window((0, 0), window=data_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        def update_scroll_region(event=None):
            canvas.config(scrollregion=canvas.bbox("all"))

        data_frame.bind("<Configure>", update_scroll_region)

        info_label = tk.Label(data_frame,
                              text=f"Luggage: {self.luggage_var.get()}\nTime: {self.time_entry.get().strip()}",
                              font=("Arial", 12), bg="light pink")
        info_label.pack(pady=10)

        def book_trip(trip_data):
            company, pickuploc, droploc, price, ttime, name = trip_data
            ttime_display = ttime if ttime else "Not available"
            booking_message = (
                f"Booking details:\n"
                f"Company: {company}\n"
                f"Pickup Location: {pickuploc}\n"
                f"Drop Location: {droploc}\n"
                f"Price: {price}\n"
                f"Approx Travel Time: {ttime_display}\n"
                f"Name: {name}\n\n"
                "Would you like to confirm the booking?"
            )
            if messagebox.askyesno("Confirm Booking", booking_message):
                messagebox.showinfo("Booking Confirmed", "Your trip has been booked successfully.")
            else:
                messagebox.showinfo("Booking Canceled", "Your booking has been canceled.")

        tk.Label(data_frame, text="First Leg:", font=("Arial", 14), bg="light pink").pack(pady=10)
        for row in rows1:
            company, pickuploc, droploc, price, ttime, name = row

            record_frame = tk.Frame(data_frame, bg="light pink", padx=10, pady=10)
            record_frame.pack(pady=5, fill=tk.X)

            tk.Label(record_frame, text=f"Company: {company}", font=("Arial", 12), bg="light pink").pack(anchor=tk.W)
            tk.Label(record_frame, text=f"Pickup Location: {pickuploc}", font=("Arial", 12), bg="light pink").pack(
                anchor=tk.W)
            tk.Label(record_frame, text=f"Drop Location: {droploc}", font=("Arial", 12), bg="light pink").pack(
                anchor=tk.W)
            tk.Label(record_frame, text=f"Price: {price}", font=("Arial", 12), bg="light pink").pack(anchor=tk.W)
            tk.Label(record_frame, text=f"Approx Travel Time: {ttime if ttime else 'Not available'}",
                     font=("Arial", 12), bg="light pink").pack(anchor=tk.W)
            tk.Label(record_frame, text=f"Name: {name}", font=("Arial", 12), bg="light pink").pack(anchor=tk.W)

            book_button = tk.Button(record_frame, text="Book Now", font=("Arial", 12), bg="#3498db", fg="#ffffff",
                                    command=lambda row=row: book_trip(row))
            book_button.pack(pady=5)

        if rows2:
            tk.Label(data_frame, text="Second Leg:", font=("Arial", 14), bg="light pink").pack(pady=10)
            for row in rows2:
                company, pickuploc, droploc, price, ttime, name = row

                record_frame = tk.Frame(data_frame, bg="light pink", padx=10, pady=10)
                record_frame.pack(pady=5, fill=tk.X)

                tk.Label(record_frame, text=f"Company: {company}", font=("Arial", 12), bg="light pink").pack(anchor=tk.W)
                tk.Label(record_frame, text=f"Pickup Location: {pickuploc}", font=("Arial", 12), bg="light pink").pack(
                    anchor=tk.W)
                tk.Label(record_frame, text=f"Drop Location: {droploc}", font=("Arial", 12), bg="light pink").pack(
                    anchor=tk.W)
                tk.Label(record_frame, text=f"Price: {price}", font=("Arial", 12), bg="light pink").pack(anchor=tk.W)
                tk.Label(record_frame, text=f"Approx Travel Time: {ttime if ttime else 'Not available'}",
                         font=("Arial", 12), bg="light pink").pack(anchor=tk.W)
                tk.Label(record_frame, text=f"Name: {name}", font=("Arial", 12), bg="light pink").pack(anchor=tk.W)

                book_button = tk.Button(record_frame, text="Book Now", font=("Arial", 12), bg="#3498db", fg="#ffffff",
                                        command=lambda row=row: book_trip(row))
                book_button.pack(pady=5)

        close_button = tk.Button(result_window, text="Close", command=result_window.destroy, font=("Arial", 12),
                                 bg="#e74c3c", fg="#ffffff")
        close_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = VoyageVistaWindow(root)
    root.mainloop()
