# Import dependencies
import time
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser

# Searches for player and calls for soup to be made
def finder(player_name):
    time.sleep(1)
    browser.fill('_nkw', player_name)
    browser.find_by_id('gh-btn').click()
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# URL for ebay's sports memorabilia category
ebay_sm_url = 'https://www.ebay.com/b/Sports-Memorabilia-Fan-Shop-Sports-Cards/64482/bn_1857919'
player_list = ['Aaron Judge', 'Jacob Degrom']
results = []

# Get browser ready for work
browser = Browser("chrome", headless=True)
browser.visit(ebay_sm_url)

# For each player find the number of listings on ebay
for player in player_list:
    soup = finder(player)
    results_text = soup.find('h1', class_='srp-controls__count-heading').get_text()
    results_number = int(results_text.replace(' results','').replace(',',''))
    
    results_dict = {
        'player_name':player,
        'number_of_listings':results_number,
        'date_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    results.append(results_dict)

# Save results to csv file
df = pd.DataFrame(results)
df.to_csv('PlayerListings.csv')