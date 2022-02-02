from FirebaseUtil import *
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
