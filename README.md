[![license](https://img.shields.io/github/license/cameronmathis/AUMBBTracker)](LICENSE)
[![CodeFactor](https://www.codefactor.io/repository/github/cameronmathis/AUMBBTracker/badge)](https://www.codefactor.io/repository/github/cameronmathis/AUMBBTracker)

# AU MBB Tracker

This is a Python Application that tweets the number of days since the Auburn Men's Basketball team lost.

## Table of contents

- [General info](#general-info)
- [Setup](#setup)
- [Status](#status)
- [Language details](#Language-details)
- [Contact](#contact)

## General info

This is a project I decided I wanted to do in order to familiarize myself with Twitter APIs. The Twitter account associated with this project can be found [here](https://twitter.com/AUMBBTracker).

## Setup

_Disclaimer: All instructions given are for a linux based machine._ </br>
In order to run this application you will need a Twitter Developer Account. It is recommended that you use environment variables or an authentication file to store your account credentials, but you can also hard code them if you would like. A link on setting up environment variables can be found [here](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). </br>

Before you run this application, you need to install the required packages with the below command:

> pip install -r requirements.txt

In order to run this application, use the below command:

> ./runAUMBBTracker.sh

_You may need to run the following command on the script:_

> sed -i 's/\r$//' runAUMBBTracker.sh

## Status

Version: 3.0.0 Beta </br>
Project is: _finished_

## Language details

Language used: Python </br>
Version used: 3.8

## Contact

Created by [@cameronmathis](https://github.com/cameronmathis/) - feel free to contact me!
