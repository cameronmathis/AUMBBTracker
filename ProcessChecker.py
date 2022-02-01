from datetime import datetime
import os

# check if the app is still running
while True:
    processName = 'AUMBBTracker.py'

    tmp = os.popen('ps -Af').read()

    if processName not in tmp[:]:
        print(
            f'\nThe process is not running. Restarting now ({datetime.now()}).\n')
        process = './runAUMBBTracker.sh ' + phoneNumber
        os.system(process)
