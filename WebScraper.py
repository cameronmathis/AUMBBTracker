from datetime import datetime
from bs4 import BeautifulSoup
import requests

def getCurrentRecord():
    url = "https://www.espn.com/mens-college-basketball/team/_/id/2/auburn-tigers"
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.content, 'lxml')

    record = soup.find('ul', class_ = 'ClubhouseHeader__Record')
    
    return record.li.text

def getGamesOpponent():
    todaysGame = getTodaysGame()

    opponent = todaysGame.find('a', class_ = 'AnchorLink').find('img', alt=True).get('title')
        
    return opponent

def getGamesResult():
    todaysGame = getTodaysGame()
    
    cells = todaysGame.find_all('td')
    i = 0
    for cell in cells:
        if i == 2:
            if cell.find('span').text == 'W':
                return 'win'
            elif cell.find('span').text == 'L':
                return 'lose'
            else:
                return '?'
        i += 1

def getGamesScore():
    todaysGame = getTodaysGame()
    
    cells = todaysGame.find_all('td')
    i = 0
    for cell in cells:
        if i == 2:
            spans = cell.find_all('span')
            y = 0
            for span in spans:
                if y == 1:
                    return span.find('a', class_ = 'AnchorLink').text.strip()
                y += 1
        i += 1

def getTodaysGame():
    #get todays date
    todaysDate = datetime.today().strftime('%a, %b %d')
    url = "https://www.espn.com/mens-college-basketball/team/schedule/_/id/2"
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.content, 'lxml')

    table = soup.find('tbody', class_='Table__TBODY')
    rows = table.find_all('tr')

    i = 0
    for row in rows:
        if i >= 2:
            cells = row.find_all('td')
            if cells[0].find('span').text == todaysDate:
                return row
        
        i += 1
