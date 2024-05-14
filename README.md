<p align="center">
  <a href="https://github.com/olivierluethy/PC-Shutdown-Planner">
    <img src="assets/logo.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Welcome to the <strong>PC Shutdown Planner!</strong></h3>
  <p align="center">
    PC Shutdown Planner is a simple Python application that allows users to schedule automatic shutdowns for their computers. This tool helps users plan shutdowns at specific dates and times, allowing for efficient management of system shutdowns.
    The idea came to me when I wanted to go to bed at 10. Because I was working hard on something, I forgot the time and it was already 12. So now it will happen automatically, so I'll get enough sleep.
  </p>
</p>

### How It Works

The application utilizes the Tkinter library for creating a graphical user interface (GUI) and provides a straightforward interface for users to input the desired shutdown time. The key functionalities of the application include:

- **User Input**: Users can select a date and enter a time in hours and minutes (in 24-hour format) when they want their PC to shut down.
- **Validation**: The application validates user input to ensure that the selected shutdown time is in the future and in the correct format.
- **Countdown Display**: Once the shutdown is scheduled, a countdown timer is displayed, showing the remaining time until the scheduled shutdown.
- **Scheduled Shutdown**: The application utilizes the `schedule` library to schedule the system shutdown at the specified time.

### Prerequisites

Before running the PC Shutdown Planner, ensure that you have Python installed on your system. Additionally, you need to install the following Python packages:

- `tkinter`: This package is typically included with Python and provides the necessary tools for creating GUI applications.
- `tkcalendar`: This package provides a date entry widget for selecting dates.
- `schedule`: This package is used for scheduling tasks.

You can install these packages using pip:

```
pip install tk tkcalendar schedule
```

### How to Run

To run the PC Shutdown Planner:

1. Clone this repository to your local machine.
2. Make sure you have Python and the required packages installed (see Prerequisites).
3. Navigate to the directory where the project is located.
4. Run the Python script `pc_shutdown_planner.py`:

```
python pc_shutdown_planner.py
```

5. The GUI window will appear, allowing you to input the desired shutdown time.

### Usage

1. Select a date using the date entry widget.
2. Enter the desired shutdown time in the format HH:MM (24-hour format).
3. Click the "Shutdown planen" (Schedule Shutdown) button.
4. If the input is valid, you will receive a confirmation message indicating the scheduled shutdown time.
5. A countdown timer will be displayed, showing the remaining time until the scheduled shutdown.

### Issues during the project
1. Error message: Exception: Could not load icon C:\Users\Username\Documents\Projectname\logo.png
   We encountered this error message while adding an icon to the project in Tkinder. If you meet this problem, click [here](https://stackoverflow.com/questions/64601038/could-not-load-icon-plyer-library):

   If it still does not work as it did for us, do the following
   1. Close and re-open Visual Studio Code, and
   2. Put the raw PNG file into a .ico converter and replace it with the old .ico file.
  
   Then it should work!

### Note

- Ensure that you have saved any important work before scheduling a shutdown, as the application initiates an automatic shutdown of the system. But you will be notified 10 minutes before a shutdown happens, so you know how much time remains.
- The application may require administrative privileges to execute the shutdown command, depending on the system configuration.

Enjoy using the PC Shutdown Planner to efficiently manage your system shutdowns!
