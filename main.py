import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
url = "http://www.biletix.com/search/TURKIYE/tr#!subcat_sb:alternatif$MUSIC"
categories = ["alternatif", "blues", "dans_elektronik", "dunya_muzik", "heavy_metal", "jazz", "klasik", "latin_tango",
              "newage", "party", "pop", "rap_hiphop", "rock", "turksanat_halkmuzik", "other"]
date = []
concert_name = []


def get_website_data(url):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # todo parse data for first page
        parse_page(soup)
        pages = [page.text for page in soup.findAll("li", {"class": "spages"})]
        if len(pages) > 2:
            pages = pages[:len(pages) // 2]
            print(pages)
            for page in pages:
                js = "javascript:gotoPage(" + page + ")"
                driver.execute_script(js)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                print(soup)
                parse_page(soup)
                # todo parse data for each page
        # implement pages here
        # js = "javascript:gotoPage(25)"
        # driver.execute_script(js)
        # soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        # print(soup)
        return soup
    except:
        print("failed to connect")


def parse_page(soup):
    # todo implement this
    return soup


soup = get_website_data(url)
