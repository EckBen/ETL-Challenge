# Import dependencies
import os, time, datetime
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser

# Searches for player and calls for soup to be made
def finder(search_term):
    browser.fill('_nkw', search_term)
    browser.find_by_id('gh-btn').click()
    search_result_soup = souper()
    results_text = search_result_soup.find('h1', class_='srp-controls__count-heading').get_text()
    results_number = int(results_text.replace(' result','').replace('s','').replace(',',''))
    return results_number

# Makes soup
def souper():
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Pull current list of teams in MLB
def team_generator():
    teams_url = 'http://m.mlb.com/teams/'
    print('Visiting "http://m.mlb.com/teams/"...')
    browser.visit(teams_url)
    mlb_soup = souper()
    team_list = mlb_soup.find_all('h3')
    if team_list:
        print('Found list of MLB teams...')
    return team_list

# URL for ebay's sports memorabilia category
ebay_sm_url = 'https://www.ebay.com/b/Sports-Memorabilia-Fan-Shop-Sports-Cards/64482/bn_1857919'

# Read in lists of players
print('Reading in data from Output/players.csv')
players_df = pd.read_csv(os.path.join('Output','players.csv'))
player_results = []

# Get browser ready for work
browser = Browser("chrome", headless=True)
browser.visit(ebay_sm_url)
print('Visiting http://www.ebay.com/...')

# For each pitcher find the number of listings on ebay
for counter, player in enumerate(list(players_df['Name']), 1):
    if counter % 100 == 0:
        browser.quit()
        browser = Browser('chrome',headless=True)
        browser.visit(ebay_sm_url)
    
    print('--------------------------------------')
    print(f'Searching for {player} listings...')
    player_listings = finder(player)
    print(f'{player_listings} results found')
    results_dict = {
        'player_name':player,
        'number_of_listings':player_listings,
        'date_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    player_results.append(results_dict)

# Save results to csv file
print('--------------------------------------')
print('Saving results to Output/player_listings.csv')
df = pd.DataFrame(player_results)
df.to_csv(os.path.join('Output','player_listings.csv'))