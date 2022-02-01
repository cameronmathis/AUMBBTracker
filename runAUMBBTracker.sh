#!/bin/bash
# check for phone number argument
if test "$#" -ne 1; 
then
    echo "Twilio not active"
    # compile and execute the program in Python3
    source env/bin/activate
    nohup python3 AUMBTracker.py
    bg
else
    echo "Twilio active"
    # compile and execute the program in Python3
    source env/bin/activate
    nohup python3 AUMBTracker.py $1
    bg
fi