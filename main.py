import os
import time

# set shutdown time to 10 pm
shutdown_time = time.strptime("22:00:00", "%H:%M:%S")

while True:
    # get current time
    current_time = time.localtime()

    # check if current time is greater than or equal to shutdown time
    if current_time >= shutdown_time:
        # shutdown the computer
        os.system("shutdown /s /t 1")
        break

    # sleep for 60 seconds before checking the time again
    time.sleep(60)
