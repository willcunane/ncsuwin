import requests
from bs4 import BeautifulSoup

url = ('https://gopack.com/sports/womens-basketball/schedule')
response = requests.get(url)

if response.status_code == 200:
    print('Select the number to the desired sport and press enter...')
    print('')

    print('1. Mens Basketball')
    print('2. Womens Basketball')
    print('3. Football')
    print('4. Baseball')

    sport = input()

else:
    print('There has been an error, try again later')

if sport == 1:
    print('Loading stats for mens basketball...')
elif sport == 2:
    print('Loading stats for womens basketball...')
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup.find("div", class_="sidearm-schedule-game-result text-italic"))
elif sport == 3:
    print('Loading stats for football...')
elif sport == 4:
    print('loading stats for baseball...')


