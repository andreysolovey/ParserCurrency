import requests
from bs4 import BeautifulSoup
from scraping.models import Job
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'https://www.nbrb.by/statistics/rates/ratesdaily.asp'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('tr')
        names = soup.find_all('span', class_='text')
        number = soup.find_all('td', class_='curAmount')
        curCour = soup.find_all('td', class_='curCours')

        for i in range(0, len(quotes)):
            name = names[i].text
            numbers = number[i].text
            curCours = curCour[i].text
            try:
                Job.objects.auto_created(
                    name=name,
                    numbers=numbers,
                    ExchangeRates=curCours
                )
                print('%s added' % (name,))
            except:
                print('%s already exists' % (name,))
        self.stdout.write('job complete')
