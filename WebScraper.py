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

    record = soup.find('ul', class_ = 'ClubhouseHeader__Record')
    
    return record.li.text

'''
Returns the row corresponding to today's game from Auburn's schedule on ESPN
'''
def getTodaysGame():
    #get todays date
    todaysDate = datetime.today().strftime('%a, %b %d').replace(' 0', ' ')
    url = "https://www.espn.com/mens-college-basketball/team/schedule/_/id/2"
    page = requests.get(url)
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

'''
Returns the location from Auburn's game today according to ESPN
'''
def getGamesLocation():
    todaysGame = getTodaysGame()
    
    cells = todaysGame.find_all('td')
    i = 0
    for cell in cells:
        if i == 1:
            if cell.find('span').text == 'vs':
                return 'against'
            elif cell.find('span').text == '@':
                return 'at'
            else:
                return '?'
        i += 1

'''
Returns the opponent from Auburn's game today according to ESPN
'''
def getGamesOpponent():
    todaysGame = getTodaysGame()

    opponent = todaysGame.find('a', class_ = 'AnchorLink').find('img', alt=True).get('title')
        
    return opponent

'''
Returns the final result from Auburn's game today according to ESPN
'''
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

'''
Returns the final score from Auburn's game today according to ESPN
'''
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
