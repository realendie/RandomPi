from bs4 import BeautifulSoup
import requests as re
import requests

html_text = requests.get("https://pypi.org/project/RandomPi/").text
soup = BeautifulSoup(html_text, features="html.parser")
name = soup.find("h1", class_="package-header__name").text.strip()
date = soup.find("p", class_="package-header__date").text
des = soup.find("p", class_="package-description__summary").text

print(f'Name:\n  {name}{date}Description:\n  {des}')
