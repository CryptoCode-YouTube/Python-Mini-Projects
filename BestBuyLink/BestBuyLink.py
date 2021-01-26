# BestBuyLink

# Search the price of a specific product daily in (amazon.in) and save it in a file.
# If the price is low when compared to the yesterday's price then send a buy link as a msg to the user in discord.
# If the price is high then ignore and wait for the right moment to buy the product.

import selenium
from selenium import webdriver as wb
import time as t
import os

def scrapping():
    try:
        app = wb.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
        url = "https://www.amazon.in/OnePlus-Nord-Marble-128GB-Storage/dp/B086977J3K/ref=sr_1_1?crid=T7O4GSZ3VSP8&dchild=1&keywords=oneplus+nord&qid=1607338329&sprefix=oneplus%2Caps%2C333&sr=8-1"
        app.get(url)

        os.system('cls')
        product_name = app.find_element_by_xpath("//*[@id='productTitle']")
        print(product_name.text)
        price = app.find_element_by_xpath("//*[@id='priceblock_dealprice']")
        print(price.text)


        t.sleep(50)
        app.quit()

    except Exception as e:
        print("Error --->", e)

def main():
    scrapping()


if __name__ == '__main__':
    main()

