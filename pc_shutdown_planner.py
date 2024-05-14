import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry
from time import sleep
from plyer import notification
import schedule

# Funktion zur Anzeige der Notifikation
def show_notification(title, message, icon_path):
    notification.notify(
        title=title,
        message=message,
        app_name="Shutdown Reminder",
        app_icon=icon_path,
        timeout=15
    )

def countdown(shutdown_datetime, countdown_label):
    informed = False
    try:
        while True:
            current_time = datetime.now()
            time_difference = shutdown_datetime - current_time
            if time_difference.total_seconds() <= 0:
                countdown_label.config(text="Shutdown time reached!")
                shutdown()
                break

            hours, remainder = divmod(time_difference.total_seconds(), 3600)
            mins, secs = divmod(remainder, 60)

            # Check if less than 10 minutes remaining
            if time_difference.total_seconds() <= 600:
                if not informed:
                    # Setze den absoluten Pfad zum Bild
                    icon_path = os.path.join(os.getcwd(), "assets/alert.ico")

                    show_notification("Important", "10 minutes until shutdown. Please save your work.", icon_path)
                    informed = True

            countdown_label.config(text=f"Time until shutdown: {int(hours)} hours {int(mins)} minutes {int(secs)} seconds")
            root.update()  # Update the Tkinter window
            sleep(1)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to initiate system shutdown
def shutdown():
    try:
        os.system("shutdown /s /t 1")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to schedule shutdown
def schedule_shutdown(shutdown_datetime):
    try:
        shutdown_time_str = shutdown_datetime.strftime("%H:%M")
        schedule.every().day.at(shutdown_time_str).do(shutdown)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to validate user input
def validate_input():
    try:
        selected_date = date_entry.get_date()
        shutdown_time_str = time_entry.get()

        shutdown_time = datetime.strptime(shutdown_time_str, "%H:%M").time()

        current_datetime = datetime.now()

        shutdown_datetime = datetime.combine(selected_date, shutdown_time)

        if shutdown_datetime <= current_datetime:
            messagebox.showerror("Error", "Please select a date and time in the future.")
        else:
            schedule_shutdown(shutdown_datetime)
            messagebox.showinfo("Info", f"PC will shutdown at: {shutdown_time_str}")
            countdown(shutdown_datetime, countdown_label)  # Moved here
            
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please enter time in HH:MM format.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Define the main window
root = tk.Tk()
root.title("Shutdown Scheduler")

# Set desktop icon
root.iconbitmap("assets/icon.ico")

# Create a frame for user input
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Add a label for shutdown time
shutdown_time_label = tk.Label(input_frame, text="Shutdown Zeit: Month | Day | Year")
shutdown_time_label.pack(side=tk.LEFT)

# Create a date entry widget using tkcalendar
date_entry = DateEntry(input_frame, year=2024)
date_entry.pack(side=tk.LEFT, padx=5)

# Add a label for time input
time_input_label = tk.Label(input_frame, text="Uhrzeit (HH:MM):")
time_input_label.pack(side=tk.LEFT, padx=5)

# Create a time entry field
time_entry = tk.Entry(input_frame)
time_entry.pack(side=tk.LEFT)

# Create a button to submit the input
submit_button = tk.Button(input_frame, text="Shutdown planen", command=validate_input)
submit_button.pack(pady=10)

# Create a label to display the countdown
countdown_label = tk.Label(root, text="")
countdown_label.pack()

# Define the shutdown datetime
shutdown_datetime = datetime(2024, 5, 12, 12, 0)  # Example datetime

# Run the Tkinter event loop
root.mainloop()