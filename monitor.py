import psutil
import time

while True:
    print ("CPU:", psutil.cpu_percent())
    print ("Memory:", psutil.virtual_memory().percent)
    print ("Disk:", psutil.disk_usage('/').percent)
    time.sleep(3)
