# Sleep-at-10-pm
Shuts the computer down when it gets 10 pm, so that I get enough sleep.

## Description
The script uses a while loop to keep checking the current time every minute. If the current time is greater than or equal to the specified shutdown time of 10 pm, the computer is shut down using the os.system() method with the command "shutdown /s /t 1". The script then exits the loop using break. If the current time is not yet 10 pm, the script sleeps for 60 seconds before checking the time again.
