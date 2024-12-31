from bs4 import BeautifulSoup
import requests as re
import requests

html_text = requests.get('https://pypi.org/project/RandomPi/').text
soup = BeautifulSoup(html_text, features='html.parser')
name = soup.find('h1', class_ = 'package-header__name').text

print(name)