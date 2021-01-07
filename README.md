# AUMB Tracker
This is a Python Application that tweets final score updates for the Auburn Men's Basketball team while also texting the results to my phone.

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Language details](#Language-details)
* [Contact](#contact)

## General info
This is a project I decided I wanted to do in order to familiarize myself with Python Automation. It runs on my RaspberryPi and tweets/text me the final score to the Auburn Men's Basketball games. The Twitter account associated with this project can be found [here](https://twitter.com/AUMBtracker). If you have a Twilio account, this script can be run to text the scores to any phone number using the setup below.

## Setup
_Disclaimer: All instructions given are for a linux based machine._ <br/>
In order to run this application you will need a Twitter Developer Account and a Twilio account. It is recommended that you use environment variables or an authentication file to store your account credentials, but you can also hard code them if you would like. A link on setting up environment variables can be found [here](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). <br/>
Once you have your Twilio account set up, clone this repo onto your local machine and navigate to the project folder. <br/>

In order to use this application with the texting feature the run.sh script with the command:
>./runAUMBTracker.sh.sh [phone number]

Example:
>./runAUMBTracker.sh '+13345550198'

In order to use this application with only the Twitter feature the run.sh script with the command:
>./runAUMBTracker.sh

The application is now running, and will provide updates for the final scores of the Auburn Men's Basketball games.

If you want to check if the application is running, simply type the command:
>ps aux | grep AUMBTracker.py <br/>

I am currently working on an untrusted SSL certificate exception that causes the application to shut down. In the mean time, running this script will ensure that the application stays running 24/7:
>./runProcessChecker.sh

If you want to kill the application, simply type the commands:
>pkill -f ProcessChecker.py <br/>
>pkill -f AUMBTracker.py

_*Note: There is a current bug in the tweepy library when it comes to cloning from github._

## Features
Implemented:
* Tweets the final scores
* The tweets are different for home and away games
* Texts final score using Twilio

Work in progress:
* Solve untrusted SSL certificate exception

Feature features:
* Tweets that a game is about to start
* Tweet halftime scores
* Tweet that a game is headed to overtime
* Tweet that the starting line up is changing from last game
* Tweet post game stats

## Status
Version: 2.0.0 Beta <br/>
Project is: _finished_

## Language details
Language used: Python </br>
Version used: 3.8

## Contact
Created by [@cameronmathis](https://github.com/cameronmathis/) - feel free to contact me!
