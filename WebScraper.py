from FirebaseUtil import *
from datetime import datetime
from bs4 import BeautifulSoup
import requests

'''
Returns Auburn's current record according to ESPN
'''


def getCurrentRecord():
    url = "https://www.espn.com/mens-college-basketball/team/_/id/2/auburn-tigers"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    record = soup.find('ul', class_='ClubhouseHeader__Record')

    return record.li.text


'''
Returns a boolean indicating if a game has been played
'''


def checkForGame():
    previousRecord = getPreviousRecord()
    currentRecord = getCurrentRecord()

    if not (previousRecord == currentRecord):
        return False

    return True


'''
Returns a boolean indicating if a loss has occurred
'''


def checkForLoss():
    if not (checkForGame):
        setDaysSinceLoss(getDaysSinceLoss() + 1)
        return

    compareRecords()
