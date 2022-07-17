import requests
from bs4 import BeautifulSoup


def get_citations_needed_count():
    URL = 'https://en.wikipedia.org/wiki/Ottoman_Empire'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")


def get_citations_needed_report():

    citation_needed = soup.find(title="Citation needed")