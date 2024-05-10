import os
import time
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

def countdown(t):
    while t:
        hours, remainder = divmod(t, 3600)
        mins, secs = divmod(remainder, 60)
        print(f"Countdown: {int(hours)} Stunden, {int(mins)} Minuten, {int(secs)} Sekunden", end='\r')
        time.sleep(1)
        t -= 1

def shutdown():
    root.destroy()
    time.sleep(600)  # 10 Minuten warten, bevor der PC heruntergefahren wird
    os.system("shutdown /s /t 1")

# Benutzerdefinierte Zeit für den Shutdown abfragen
shutdown_time_input = simpledialog.askstring("Shutdown Zeit", "Geben Sie die Zeit für den Shutdown im Format HH:MM ein:")
try:
    shutdown_hour, shutdown_minute = map(int, shutdown_time_input.split(":"))
except ValueError:
    messagebox.showerror("Fehler", "Ungültiges Zeitformat. Bitte geben Sie die Zeit im Format HH:MM ein.")
    exit()

current_time = time.localtime(time.time()) # Aktuelle lokale Zeit
shutdown_time = time.mktime((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, shutdown_hour, shutdown_minute, 0, 0, 0, 0))

if shutdown_time <= time.time():
    messagebox.showerror("Fehler", "Die eingegebene Zeit ist bereits vergangen. Bitte geben Sie eine zukünftige Zeit ein.")
    exit()

root = tk.Tk()
root.withdraw()

time_until_shutdown = shutdown_time - time.time()

if time_until_shutdown > 600:  # Wenn mehr als 10 Minuten bis zum Shutdown verbleiben
    countdown_thread = threading.Thread(target=countdown, args=(time_until_shutdown,))
    countdown_thread.start()
    messagebox.showinfo("Warnung", "Der Computer wird in 10 Minuten heruntergefahren. Bitte sichern Sie alle Daten.")
else:
    # Weniger als 10 Minuten bis zum Shutdown
    time.sleep(time_until_shutdown)

shutdown()
