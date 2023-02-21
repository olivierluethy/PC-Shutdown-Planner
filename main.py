import os
import time

# get current time
current_time = time.localtime()

# set shutdown time to 10 pm
shutdown_time = time.strptime("22:00:00", "%H:%M:%S")

# calculate time difference in seconds
time_diff = time.mktime(shutdown_time) - time.mktime(current_time)

# sleep until shutdown time
if time_diff > 0:
    time.sleep(time_diff)

# shutdown the computer
os.system("shutdown /s /t 1")
