# Sleep-at-10-pm
Shuts the computer down when it gets 10 pm, so that I get enough sleep.

## Description
This script first gets the current time using the time.localtime() function. It then sets the shutdown time to 10 pm using the time.strptime() function. The time difference between the current time and the shutdown time is calculated in seconds using time.mktime() and stored in the time_diff variable.

If the shutdown time is in the future, the script sleeps for the remaining time until the shutdown time using the time.sleep() function. Finally, the script shuts down the computer using the os.system() function and the Windows shutdown command with the /s flag to shut down the computer and the /t flag to specify a delay of 1 second.
