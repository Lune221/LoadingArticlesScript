#################################
##    Author: ALIOUNE SARR     ##
##    Date: 11 / 01 / 2021     ##
#################################

import selenium
from selenium import webdriver
import time
import requests
import os
import io
import hashlib

# This is the path I use
DRIVER_PATH_WINDOWS = r'chromedriver.exe'

# Use this path if your operating system is MACOS
DRIVER_PATH_MACOS = r'chromedriver'


def scroll_to_end(wd, sleep_between_interactions):
    """
    Function for scrolling to the end of the page for loading all the data.
    
    """
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(sleep_between_interactions)


def fetch_article(url: str, max_pages: int, sleep_between_interactions: int = 4):
    wd = webdriver.Chrome(executable_path=DRIVER_PATH_WINDOWS)
    # load the page
    wd.get(url)

    page = 1
    while page <= max_pages: # Loop for every page in order to get the articles

        button = wd.find_elements_by_css_selector("span.pagination-next")[0]

        articles = wd.find_elements_by_css_selector("div.doc-snippet")
        number_articles = len(articles)

        print(f"Found: {number_articles} on this page. ")

        i = 1 # i for storing the number of the orticle in the page
        for article in articles:

            content = article.text
            # print(content)
            if not os.path.exists('articles/page_{0}'.format(page)):
                os.makedirs('articles/page_{0}'.format(page))
                
            f = open(
                file="articles/page_{0}/article_{1}.txt".format(page, i), mode="w")
            i += 1
            f.write(content)
            f.close()
            

        button.click()
        time.sleep(sleep_between_interactions) # Waitin some seconds for waiting the page to reload (depends on the speed of the connexion)
        
        page += 1

    wd.close()
    return None


# VERY IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# You will ajust the sleep between interaction interval depending on the speed of your internet connexion

fetch_article(url="http://bibliome.jouy.inra.fr/demo/wheat/alvisir/webapi/search?q=wheat+or+disease+or+plant&n=50&s=0#", 
    max_pages=2, sleep_between_interactions=3)
