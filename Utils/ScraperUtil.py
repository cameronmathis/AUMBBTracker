from datetime import datetime
from bs4 import BeautifulSoup
import requests

'''
Gets Auburn's current record according to ESPN

Returns a string
'''


def scrapeCurrentRecord():
    url = "https://www.espn.com/mens-college-basketball/team/_/id/2/auburn-tigers"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    record = soup.find('ul', class_='ClubhouseHeader__Record')

    return record.li.text


'''
Gets a list of all of Auburn's losses according to ESPN

Returns a string array
'''


def scrapeLosses():
    url = "https://www.espn.com/mens-college-basketball/team/schedule/_/id/2"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    table = soup.find('tbody', class_='Table__TBODY')
    rows = table.find_all('tr')

    losses = []
    i = 0
    for row in rows:
        if i >= 2:
            cells = row.find_all('td')
            if cells[2].find('span').text == 'L':
                lossDate = cells[0].find('span').text
                lossDateTime = datetime.strptime(
                    lossDate, "%a, %b %d")
                # need to figure out how to get correct year
                lossDateTime = lossDateTime.replace(year=datetime.now().year)
                losses.append(lossDateTime.strftime("%m/%d/%Y"))

        i += 1

    return losses
