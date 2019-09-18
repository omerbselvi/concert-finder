from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import optparse
from selenium.webdriver.chrome.options import Options

parser = optparse.OptionParser()
url = "http://www.biletix.com/search/TURKIYE/tr#!subcat_sb:{}$MUSIC"
categories = ["alternatif", "blues", "dans_elektronik", "dunya_muzik", "heavy_metal", "jazz", "klasik", "latin_tango",
              "newage", "party", "pop", "rap_hiphop", "rock", "turksanat_halkmuzik", "other"]
events = []
concert_name = []


def get_website_data(url):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        parse_page(soup)
        pages = [page.text for page in soup.findAll("li", {"class": "spages"})]
        if len(pages) >= 2:
            pages = pages[:len(pages) // 2]
            for page in pages:
                js = "javascript:gotoPage(" + page + ")"
                driver.execute_script(js)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                parse_page(soup)
        driver.quit()
        return soup
    except:
        print("failed to connect")


def parse_page(soup):
    day_of_week = [div.text for div in soup.select(".searchMobileDateDayName")][1:]
    day_of_month = [div.text for div in soup.select(".searchMobileDateDayNumber")][1:]
    month = [div.text for div in soup.select(".searchMobileDateMonth")][1:]
    event_name = [div.text for div in soup.select(".searchResultEventName")][1:]
    event_city = [div.text for div in soup.select(".searchResultCity")][1:]
    event_place = [div.text for div in soup.select(".searchResultPlace")][1:]

    if len(day_of_week) == len(day_of_month) and len(day_of_month) == len(month) and len(month) == len(event_city) \
            and len(event_city) == len(event_place):
        for i in range(0, len(day_of_week)):
            events.append(day_of_month[i] + "/" + month[i] + "/" + day_of_week[i] + " - " + event_name[i] + " - " +
                          event_city[i] + " - " + event_place[i])
    else:
        print("theres a bug, fix it")
    # print(date)
    # for i in range(0, len(day_of_week)):
    #    print(da)
    # print(data)
    return soup


parser.add_option('-c', '--category',
                  action="store", dest="category",
                  help="Select a category: " + str(categories), default="heavy_metal")
options, args = parser.parse_args()
category = options.category
url = url.format(category)
soup = get_website_data(url)
for event in events:
    print(event)
