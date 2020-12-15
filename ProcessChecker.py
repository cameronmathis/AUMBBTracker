from datetime import datetime
import os
from auth import (
    phoneNumber
)

# check if the app is still running
while True:
    processName = 'AUMBTracker.py'

    tmp = os.popen('ps -Af').read()

    if processName not in tmp[:]:
        print(f'\nThe process is not running. Restarting now ({datetime.now()}).\n')
        process = './runAUMBTracker.sh ' + phoneNumber 
        os.system(process)  
