# Rutgers ETL project – MLB Player Analysis for Potential Online Memorabilia and Apparel Store

## Summary
We provide a method that enables potential MLB online store owners for memorabilia and apparel to see what players/teams to have in inventory.  We used [baseball-reference.com](https://www.baseball-reference.com/players/) for MLB player information, [mlb.com](https://www.mlb.com/team) for a listing of team names, and [EBay.com](https://www.ebay.com/b/Sports-Memorabilia-Fan-Shop-Sports-Cards/64482/bn_1857919) for listings of memorabilia and apparel.  The results from these websites were loaded into a MySQL database for analysis. 


## Requirements
#### Programs
- Chromedriver.exe (For Windows: Ensure this is in the main directory.)
- MySQL Workbench
#### Dependencies
Run '''pip install -r requirements.txt''' in your virtual environment for these.
- Beautiful Soup 4
- pandas
- PyYAML
- Splinter


## Pipeline Usage
1. Ensure that all requirements are installed
2. Open a terminal session
3. Run ‘python player_cleaner.py’
4. Run ‘python team_scraper.py’
5. Run ‘python player_scraper.py’ (Note: This command will take close to an hour to execute. It is recommended to change the value in config.yaml to run approximately 10-15 players as a sample.)
6. Open MySQL Workbench and create local connection
7. Open "mlb_sale_create_database"
8. Import the following table data from .csv files using the Table Data Import Wizard (i.e. file_name.csv: existing_table_name)
	- Resources folder:
		-teams.csv: team_dim
	- Output folder:
		- hitters.csv: hitters
		- pitchers.csv: pitchers
		- player_listings.csv: ebay_items_player
		- team_listings.csv: ebay_items_team
9. Open "mlb_sales_data_query" and run queries as explained by comments

## Narrative/Motivation
We want to start an online baseball memorabilia/apparel store. In order to be successful, we would like to know what players and teams have items on the market and how hot the market is for each. We do not want to carry stock that will not sell and we only want to sell items from current teams and players.


## Final Schema / Data Model / How  to use the data
The final data model creates distinct FACT tables from each of the data sources extracted (pitchers, hitters, ebay team items, ebay player items) and a DIM table for team acronym/team name.  Separate Views were created for reporting purposes.
- “Combined” unions together pitchers and hitters, joins team name and eliminates unnecessary columns.
- “Player Sales” joins the “combined” with the ebay player items.
- “Team sales” joins the “combined” with the ebay team items.

Ultimately the data would be used to determine which team(s) and player(s) have the greatest number of items being sold throughout ebay which we would then stock on our ebay store.  A simple analysis would be to look at the player/team volume trends and stock those items.  Another analysis would be correlating player/team stats with ebay volume and stock/price items where statistics are trending upwards.

![Relationships between tables](/Resources/Relationships.PNG)

## Data Sources
We used baseball-reference.com for the current player and statistical information.  baseball-reference.com is recognized as a leader in baseball player statistics gathering and archiving.  The assumption of this data is that it is updated on a daily basis.  We would only run this process once per week, since significant statistical changes don’t happen daily.  We also scraped all team names in MLB from mlb.com. This keeps our program up to date whether teams become inactive or new teams are created/renamed, assuming the official MLB website is up to date. EBay.com was used to get the number items that are for sale at any given point.  EBay was chosen since there are numerous sellers that we can pull from.  Additionally, we were able to scrape the data we needed.

## Transformation Step
### Program								Step
player_cleaner.py	Split out name from name id

1. player_cleaner.py
	- Removes extraneous characters
	- Adds datetimestamp to hitters.csv and pitchers.csv
	- Drops NaN values
	- Removes duplicate players
	- Selects columns for output .csv files
2. team_scraper.py
	- Scrapes website for team list
	- Uses team list to scrape ebay for total number of listings for that team
	- Outputs .csv file with results
3. player_scraper.py
	- Uses .csv from player_cleaner.py
	- Scrapes ebay for each player in .csv
	- Outputs .csv with results
4. mlb_sale_create_database
	- Creates database
	- Creates views for analysis

## Future Steps
This pipeline provides a good starting point to begin an informed business the sports memorabilia market for current teams and players. To grow this model it would be useful to include past players and teams to see valuable collectible items. A new data source for historic MLB information would be a good place to find these rosters. We could gain further insight to the market by scraping ebay for sold item data to find average selling prices for different items by player, team, and type. This data would give us an idea of what to sell items for as well as how the past market has been for the item, potenially influencing how and when to sell certain hard to find items.
