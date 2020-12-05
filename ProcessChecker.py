import os

# check if the app is still running
while True:
    processName = 'AUMBScoreTracker.py'

    tmp = os.popen('ps -Af').read()

    if processName not in tmp[:]:
        print('The process is not running. Restarting now.')
        newprocess = "./runScoreTracker.sh '+13347146447'"
        os.system(newprocess)  
    else:
        print('The process is running.')

