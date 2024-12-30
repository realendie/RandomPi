from bs4 import BeautifulSoup
import requests

url = "https://pypi.org/project/RandomPi/"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

date = soup.find_all(class='package-header__date')
print(date)