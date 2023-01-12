NFL Player Stats Scraper
This script scrapes player stats data from the NFL website and saves it to a CSV file. The script visits each page of the player stats table and extracts the name, yards, number of attacks, and touch downs of each player.

How to run the script
Make sure you have the requests and BeautifulSoup4 libraries installed by running pip install requests bs4 in your command line.
Run the script using python nfl_scraper.py
The script will start scraping the data and saving it to a CSV file named nfl.csv.
Once the script finishes running, you can open the CSV file to view the scraped data.
Note
You can change the number of pages to scrape by modifying the next_link = soup.find('a', class_='nfl-o-table-pagination__next') in the while loop.
You can also change the name of the CSV file by modifying csv_file = open('nfl.csv', 'a')
