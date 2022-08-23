from bs4 import BeautifulSoup
import requests

#F1 Driver Stats

def GetDriverWins(person):
    html_text = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    drivers = soup.tbody.find_all('tr')
    for driver in drivers:
        first_name = driver.find('span', class_='hide-for-tablet').text
        last_name = driver.find('span', class_='hide-for-mobile').text
        name = first_name + ' ' + last_name
        if name.upper() == person.upper():
            driver_link = 'https://www.formula1.com' + driver.a['href']
            html_text = requests.get(driver_link).text
            break

    soup = BeautifulSoup(html_text, 'lxml')
    races = soup.tbody.find_all('tr')
    wins = 0

    for race in races:
        race_position = race.find_all('td', class_='dark')[1].text
        if race_position == '1':
            wins += 1
    print(person, 'has', wins, 'race victories!')

def GetDriverDNFs(person):
    html_text = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    drivers = soup.tbody.find_all('tr')
    for driver in drivers:
        first_name = driver.find('span', class_='hide-for-tablet').text
        last_name = driver.find('span', class_='hide-for-mobile').text
        name = first_name + ' ' + last_name
        if name.upper() == person.upper():
            driver_link = 'https://www.formula1.com' + driver.a['href']
            html_text = requests.get(driver_link).text
            break

    soup = BeautifulSoup(html_text, 'lxml')
    races = soup.tbody.find_all('tr')
    DNFs = 0

    for race in races:
        race_position = race.find_all('td', class_='dark')[1].text
        if race_position == 'DNF':
            DNFs += 1
    print(person, 'has not finished', DNFs, 'races :(')

def GetDriverAveragePlacing(person):
    html_text = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    drivers = soup.tbody.find_all('tr')
    for driver in drivers:
        first_name = driver.find('span', class_='hide-for-tablet').text
        last_name = driver.find('span', class_='hide-for-mobile').text
        name = first_name + ' ' + last_name
        if name.upper() == person.upper():
            driver_link = 'https://www.formula1.com' + driver.a['href']
            html_text = requests.get(driver_link).text
            break

    soup = BeautifulSoup(html_text, 'lxml')
    races = soup.tbody.find_all('tr')
    PlacementTotal = 0
    FinishedRaces = 0

    for race in races:
        race_position = race.find_all('td', class_='dark')[1].text
        if race_position != 'DNF':
            FinishedRaces += 1
            PlacementTotal += int(race_position)
    print('His average placing everytime he finishes a race is', round(PlacementTotal/FinishedRaces))

def GetDriverPointsAndStanding(person):
    html_text = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    drivers = soup.tbody.find_all('tr')
    for driver in drivers:
        first_name = driver.find('span', class_ = 'hide-for-tablet').text
        last_name = driver.find('span', class_ = 'hide-for-mobile').text
        name = first_name + ' ' + last_name
        if name.upper() == person.upper():
            standing = driver.find('td', class_ = 'dark').text
            points = driver.find('td', class_ = 'dark bold').text
            print(person, 'WDC standing: ', standing)
            print(person, 'Points: ', points)
            return

def GetDriverHighestPlacing(person):
    return

def GetTeamWins(company):
    html_text = requests.get('').text
    soup = BeautifulSoup(html_text, 'lxml')

    return

def GetTeamPointsAndStanding(company):
    html_text = requests.get('').text
    soup = BeautifulSoup(html_text, 'lxml')

    return

driver_or_team = input("Do you want to enter a driver or team, type in D or T: ")
if driver_or_team.upper() == 'D':
    driver = input('Enter driver name: ')
elif driver_or_team.upper() == 'T':
    team = input('Enter team name: ')


GetDriverPointsAndStanding(driver)
GetDriverWins(driver)
GetDriverDNFs(driver)
GetDriverAveragePlacing(driver)
