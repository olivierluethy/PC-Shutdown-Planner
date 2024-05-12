import os
import time
import threading
import schedule
import tkinter as tk
from tkinter import simpledialog
from datetime import datetime, time
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from time import sleep

def countdown(shutdown_datetime):
    while True:
        current_time = datetime.now()
        time_difference = shutdown_datetime - current_time
        if time_difference.total_seconds() <= 0:
            print("\rShutdown time reached!")
            break

        hours, remainder = divmod(time_difference.total_seconds(), 3600)
        mins, secs = divmod(remainder, 60)

        # Clear the previous countdown message
        print("\r", end="")
        
        print(f"Time until shutdown: {int(hours)} hours, {int(mins)} minutes, {int(secs)} seconds", end='\r')
        sleep(1)

def shutdown():
    os.system("shutdown /s /t 1")

def schedule_shutdown(shutdown_datetime):
    schedule.every().day.at(shutdown_datetime.strftime("%H:%M")).do(shutdown)

def validate_input():
    selected_date = date_entry.get_date()
    shutdown_time_str = time_entry.get()

    try:
        shutdown_time = datetime.strptime(shutdown_time_str, "%H:%M").time()
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please enter time in HH:MM format.")
        return
    
    current_datetime = datetime.now()

    shutdown_datetime = datetime.combine(selected_date, shutdown_time)

    if shutdown_datetime <= current_datetime:
        messagebox.showerror("Error", "The selected date and time are in the past. Please select a date and time in the future.")
    else:
        countdown(shutdown_datetime)
        schedule_shutdown(shutdown_datetime)
        messagebox.showinfo("Info", f"PC will shutdown at: {shutdown_time_str}")

# Define the main window
root = tk.Tk()
root.title("Shutdown Scheduler")

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

current_time = datetime.now().strftime("%H:%M:%S.%f")
current_date = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d").date()

# Run the Tkinter event loop
root.mainloop()