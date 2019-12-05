import requests
from bs4 import BeautifulSoup


URL = "https://www.amazon.in/POCO-6GB-128GB-Rosso-RED/dp/B07JQBLTFM/ref=sr_1_3?keywords=poco&qid=1573995350&s=electronics&sr=1-3"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.92"}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

title = soup.find(id="productTitle").get_text()
print(type(title))
print(title.strip())

price = soup.find(id="priceblock_ourprice").get_text()
print(price)
