import requests
from bs4 import BeautifulSoup
 
baseUrl = 'https://www.gusta.com.tw/'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.06'
}



r = requests.get('https://www.gusta.com.tw/categories/%E6%9C%AC%E9%80%B1%E6%96%B0%E5%93%81')
soup = BeautifulSoup(r.content, 'lxml')


for ultag in soup.find_all('ul', class_ = 'boxify-container'):
    for litag in ultag.find_all('li'):
        # print(litag.text)
        pass

print(123)
        

