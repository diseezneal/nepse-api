from pathlib import Path
import csv
import requests
from bs4 import BeautifulSoup


class NepseScraper:
    def __init__(self, base_url='https://merolagani.com/LatestMarket.aspx'):
        self.base_url = base_url
        self.header = []
        self.body = []
        self.csv_loc = Path(__file__).resolve(
        ).parent.parent / 'data/todaysprice.csv'

    def get_soup(self):
        return BeautifulSoup(requests.get(self.base_url, timeout=5).content, 'html.parser')

    def scrape_data(self):
        soup = self.get_soup()
        table = soup.find(
            'table', attrs={'class': 'table table-hover live-trading sortable'})

        # Get header
        for data in table.find_all('thead'):
            rows = data.find_all('th')

            for row in rows:
                if row.text != '':
                    self.header.append(row.text)

        # Get body
        for data in table.find_all('tbody'):
            rows = data.find_all('tr')

            for row in rows:
                _data = []
                for _ in row.find_all('td'):
                    _data.append(_.text)

                self.body.append(_data)

    def dump_data(self):
        with open(self.csv_loc, 'w', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.header)
            for body in self.body:
                writer.writerow(body)

    def run_scraper(self):
        self.scrape_data()
        self.dump_data()
