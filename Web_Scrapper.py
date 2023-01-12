import requests
from bs4 import BeautifulSoup
import csv


base_url = 'https://www.nfl.com'
url = 'https://www.nfl.com/stats/player-stats/'



csv_file = open('nfl.csv', 'a')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'yards', 'attacks', 'touch_downs' ])

last_page = False
while not last_page:

    Source = requests.get(url).text

    soup = BeautifulSoup(Source, 'html.parser')

    for x in soup.find('tbody').find_all('tr'):

        try:
            name = x.find('a', class_='d3-o-player-fullname nfl-o-cta--link').text
            yards = x.find('td', class_='selected').text
            attacks = x.find_all('td')[2].text
            touch_downs = x.find_all('td')[3].text

        except Exception as e:
            name = None
            yards = None


        print(name)
        print(yards)
        print(attacks)
        print(touch_downs)
        print()

        csv_writer.writerow([name, yards, attacks, touch_downs])


    next_link = soup.find('a', class_='nfl-o-table-pagination__next')

    if next_link:
        next_url = next_link['href']
        url = base_url + next_url

    else:
        last_page = True


csv_file.close()



