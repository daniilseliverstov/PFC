import requests
from bs4 import BeautifulSoup

url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"
}
req = requests.get(url, headers=headers)

src = req.text

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(src)
