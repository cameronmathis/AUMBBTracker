import logging
from datetime import datetime
from bs4 import BeautifulSoup
import requests


# Gets Auburn's current record according to https://www.espn.com/
# Returns:
#   a string
def scrapeCurrentRecord():
    url = "https://www.espn.com/mens-college-basketball/team/_/id/2/auburn-tigers"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    record = soup.find('ul', class_='ClubhouseHeader__Record')

    logging.info(
        f"Successfully scraped the current record. | Record: {record.li.text}")
    return record.li.text


# Gets a list of all of Auburn's losses according to https://www.sports-reference.com/
# Parameters:
#   year - an int indication the year of losses to scrape
# Returns:
#   a datetime array
def scrapeLosses(year):
    url = "https://www.sports-reference.com/cbb/schools/auburn/" + \
        str(year) + "-gamelogs.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    table = soup.find("table", class_="stats_table")
    tableBody = table.find("tbody")
    rows = tableBody.find_all("tr")

    losses = []
    i = 0
    for row in rows:
        if i >= 2:
            cells = row.find_all("td")
            if not (not cells) and ("L" in cells[3].text):
                lossDate = cells[0].text
                lossDateTime = datetime.strptime(
                    lossDate, "%Y-%m-%d")
                losses.append(lossDateTime)

        i += 1

    return losses


# Gets the date Auburn's last loss according to ESPN
# Returns:
#   a string
def scrapeLastLossDate():
    losses = []
    index = -1
    while not losses:
        losses = scrapeLosses(datetime.now().year - index)
        index += 1

    lastLossDate = max(losses).strftime("%m/%d/%Y")
    logging.info(
        f"Successfully scraped the last loss date. | Last Loss Date: {lastLossDate}")
    return lastLossDate
