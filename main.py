import os
import time
import threading
import tkinter as tk
from tkinter import simpledialog
from datetime import datetime
from tkcalendar import Calendar, DateEntry

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

# Define a function to validate and process the input
def validate_input():
    selected_date = date_entry.get_date()
    shutdown_time = f"{selected_date.strftime('%Y-%m-%d')} {time_entry.get()}"

    try:
        shutdown_time = datetime.datetime.strptime(shutdown_time, "%Y-%m-%d %H:%M")

        # Check if the shutdown time is in the future
        if shutdown_time <= datetime.datetime.now():
            messagebox.showerror("Fehler", "Die eingegebene Zeit ist bereits vergangen. Bitte geben Sie eine zukünftige Zeit ein.")
            return

        # Schedule the shutdown
        schedule_shutdown(shutdown_time)
        root.destroy()

    except ValueError:
        messagebox.showerror("Fehler", "Ungültiges Format. Bitte geben Sie das Datum im Format JJJJ-MM-TT und die Zeit im Format HH:MM ein.")

# Create a button to submit the input
submit_button = tk.Button(input_frame, text="Shutdown planen", command=validate_input)
submit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()