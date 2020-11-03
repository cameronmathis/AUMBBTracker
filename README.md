# AUMB Score Tracker
This is a Python Application that text live score updates for Auburn's mens basketball team to my phone.

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Language details](#Language-details)
* [Contact](#contact)

## General info
This is a project I decided I wanted to do in order to familiarize myself with Python Automation. It runs on my RaspberryPi and text me the final score to the Auburn Mens Basketball games. If you have a Twilio account, this script can be run to text the scores to any phone number using the setup below.

## Setup
In order to run this application you will need a Twilio account. It is recommended that you use environment variables to store your Twilio credentials, but you can also hardcode them if you would like. A link on setting up environment variables can be found [here](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). <br/>
Once you have your Twilio account set up, clone this repo onto your local machine and navigate to the project folder. <br/>
First activate the python virtual environment with the command:
>source env/bin/activate

Run the run.sh script with the command:
>./run.sh [phone number]

Example:
>./run.sh '+13345550198'

The application is now running, and will text the phone number provided with the final scores of the Auburn Mens Basketball games.

## Features
Implemented:
* Twilio
* Gets final score
* Sends final score

## Status
Project is: _finished_

## Language details
Language used: Python </br>
Version used: 3.8

## Contact
Created by [@cameronmathis](https://github.com/cameronmathis/) - feel free to contact me!