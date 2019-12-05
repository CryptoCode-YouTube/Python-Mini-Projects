import requests
from bs4 import BeautifulSoup


URL = "https://www.amazon.in/Apple-iPhone-11-64GB-Black/dp/B07XVMDRZY/ref=sr_1_3?crid=2Q8LMDA1TV6W2&keywords=iphone+11&qid=1573652260&sprefix=ip%2Caps%2C-1&sr=8-3"

headers = {"User-Agent " : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.92"}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
title = soup.find(id="productTitle").get_text()
# print(type(title))
print(title.strip())

price = soup.find(id="priceblock_ourprice").get_text()
print(price)    