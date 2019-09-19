from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import optparse
from selenium.webdriver.chrome.options import Options

parser = optparse.OptionParser()
category_url = "http://www.biletix.com/search/TURKIYE/tr#!subcat_sb:{}$MUSIC"
search_url = "http://www.biletix.com/search/TURKIYE/tr&searchq={}#{}"
categories = ["alternatif", "blues", "dans_elektronik", "dunya_muzik", "heavy_metal", "jazz", "klasik", "latin_tango",
              "newage", "party", "pop", "rap_hiphop", "rock", "turksanat_halkmuzik", "other"]
events = []
concert_name = []
CHARMAP = {
    "to_lower": {
        u"I": u"ı",
        u"İ": u"i",
    }
}


def get_website_data(url):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get(url)
        print("Searching by category: " + category)
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
    return soup


def lower(string):
    for key, value in CHARMAP.get("to_lower").items():
        string = string.replace(key, value)
    return string.lower()


def find_concerts(category, search):
    if len(category):
        global category_url
        category_url = category_url.format(category)
        get_website_data(category_url)
    elif len(search):
        global search_url
        search_url = search_url.format(search, search)
        get_website_data(search_url)


parser.add_option('-c', '--category',
                  action="store", dest="category",
                  help="Select a category: " + str(categories), default="")
parser.add_option('-s', '--search',
                  action="store", dest="search",
                  help="Search events on biletix", default="")
parser.add_option('--city',
                  action="store", dest="city",
                  help="Search by selected city", default="")
options, args = parser.parse_args()
category = options.category
search = options.search
city = options.city
if len(category) and len(search):
    print("invalid args")
    exit()

find_concerts(category, search)

count = 0
hit_count = 0
for event in events:
    if len(city):
        if lower(city) in lower(event):
            print(event)
            hit_count += 1
            count = hit_count
        else:
            continue
    else:
        count = len(events)
        print(event)
print(str(count) + " concerts found based on your selected category/query: " + category + search + " - " + city)
