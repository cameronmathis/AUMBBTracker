#!/bin/bash
# check for phone number argument
if test "$#" -ne 1; 
then
    echo "Twilio not active"
    # compile and execute the program in Python3
    python3 AUMBScoreTracker.py
else
    echo "Twilio active"
    # compile and execute the program in Python3
    python3 AUMBScoreTracker.py $1
fi