#!/bin/bash
# check for phone number argument
if test "$#" -ne 1; 
then
    # don't run program
    echo "Illegal number of parameters"
else
    # compile and execute the program in Python3
    python3 AuburnScoreTracker.py $1
fi