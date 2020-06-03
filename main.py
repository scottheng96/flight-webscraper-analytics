from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd
import time

print("Beginning Google Flights WebScraping")

# setting the variables (date, location, etc)

# Visits the web page
url = "https://www.google.com/flights?hl=en#flt=x/m/013hxv./m/02_286.2020-07-01;c:USD;e:1;sd:1;t:f;tt:o"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)
print("visited the webpage successfully")

# clicks expansion button to find ALL other flights
driver.find_element_by_css_selector('.gws-flights-results__dominated-toggle').click()

time.sleep(5)
print("showing all other flights successfully")

# finds all web elements of all the flights
mylist = driver.find_elements_by_css_selector('.gws-flights-results__result-list')

results_list = mylist[1].find_elements_by_css_selector('.gws-flights-results__result-item')

print(len(results_list))
print(results_list[0].text)

driver.quit()

print("Ending Google Flights WebScraping")


