import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH='/usr/local/bin/chromedriver'
url = "http://www.biletix.com/search/TURKIYE/tr#!subcat_sb:heavy_metal$MUSIC"
cookies = {'BXID': 'AAAAAAUDpsi+gvKdkPFQNmwQ3lasGIIK4FcYGw6kybGnlMrlvw==',
           'path': '/',
           'domain': 'biletix.com'
           }


def get_website(url):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        print(soup)
        return soup
    except:
        print("failed to connect")


soup = get_website(url)
