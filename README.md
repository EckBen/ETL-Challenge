# Rutgers ETL project – MLB Player Analysis for Potential Online Memorabilia and Apparel Store

## Summary
We provide a method that enables potential MLB online store owners for memorabilia and apparel to see what players/teams to have in inventory.  We used baseball-reference.com for MLB player information, mlb.com for a listing of team names, and EBay.com for listings of memorabilia and apparel.  The results from these websites were loaded into a MySQL database for analysis. 

## Requirements
•	pandas
•	Beautiful Soup 4
•	Splinter
•	Chromedriver.exe (For Windows: Ensure this is in the main directory.)
•	MySQL

## Pipeline Usage
1.	Ensure that all requirements are installed
2.	Open a terminal session
3.	Run ‘python Player_Cleaner.py’
4.	Run ‘python team_scraper.py’
5.	Run ‘python player_scraper.py’ (Note: This command will take close to an hour to execute. It is recommended to add a slice at 			line 42 to utilize approximately 10-15 players as a sample, instead.)
6.	Utilize MySQL:

## Narrative/Motivation
We want to start an online baseball memorabilia/apparel store. In order to be successful, we would like to know what players and teams have items on the market and how hot the market is for each. We do not want to carry stock that will not sell and we only want to sell items from current teams and players.


## Final Schema / Data Model / How  to use the data

## Data Sources
We used baseball-reference.com for the current player and statistical information.  baseball-reference.com is recognized as a leader in baseball player statistics gathering and archiving.  The assumption of this data is that it is updated on a daily basis.  We would only run this process once per week, since significant statistical changes don’t happen daily.  We also scraped all team names in MLB from mlb.com. This keeps our program up to date whether teams become inactive or new teams are created/renamed, assuming the official MLB website is up to date. EBay.com was used to get the number items that are for sale at any given point.  EBay was chosen since there are numerous sellers that we can pull from.  Additionally, we were able to scrape the data we needed.

## Transformation Step
### Program		### Step
Player_Cleaner.py	Split out name from name id
Player_Cleaner.py	Removed extraneous characters
Player_Cleaner.py	Added datetimestamp to hitters and pitchers.csv
Player_Cleaner.py	Dropped NaN
Player_Cleaner.py	Removed dupes
Player_Cleaner.py	Selected columns for output .csv files
	

 
