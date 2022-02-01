# AU MBB Tracker

This is a Python Application that tweets final score updates for the Auburn Men's Basketball team while also texting the results to my phone.

## Table of contents

- [General info](#general-info)
- [Status](#status)
- [Language details](#Language-details)
- [Contact](#contact)

## General info

This is a project I decided I wanted to do in order to familiarize myself with Twitter APIs. The Twitter account associated with this project can be found [here](https://twitter.com/AUMBBTracker).

## Setup

In order to use this application with only the Twitter feature the run.sh script with the command:

> ./runAUMBBTracker.sh

The application is now running, and will provide updates for the final scores of the Auburn Men's Basketball games.

If you want to check if the application is running, simply type the command:

> ps aux | grep AUMBBTracker.py <br/>

I am currently working on an untrusted SSL certificate exception that causes the application to shut down. In the mean time, running this script will ensure that the application stays running 24/7:

> ./runProcessChecker.sh

If you want to kill the application, simply type the commands:

> pkill -f ProcessChecker.py <br/>
> pkill -f AUMBBTracker.py

## Status

Version: 3.0.0 Beta <br/>
Project is: _finished_

## Language details

Language used: Python </br>
Version used: 3.8

## Contact

Created by [@cameronmathis](https://github.com/cameronmathis/) - feel free to contact me!
