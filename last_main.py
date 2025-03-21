import requests
from bs4 import BeautifulSoup


url = "https://www.crimsonnovels.com/seaechbook"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h2')
    print(title)
else:
    print("Ошибка!")