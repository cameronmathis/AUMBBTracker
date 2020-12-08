import os
from auth import (
    phoneNumber
)

# check if the app is still running
while True:
    processName = 'AUMBTracker.py'

    tmp = os.popen('ps -Af').read()

    if processName not in tmp[:]:
        print('The process is not running. Restarting now.')
        processOne = 'source env/bin/activate'
        processTwo = './runAUMBTracker.sh ' + phoneNumber
        os.system(processOne)  
        os.system(processTwo)  
    else:
        print('The process is running.')

