USE MLB_SALES;

-- create query to roster players by team
SELECT team_name as "Team", name as 'Player Name'
FROM combined;

-- create a query of team sales ranked by highest sales
SELECT team_name as "Team", number_of_listings as "Number of EBAY Listings"
FROM team_sales
ORDER BY number_of_listings DESC;

-- create a query of individual ranked by highest sales
SELECT name as "Player Name", team_name as "Team", number_of_listings as "Number of EBAY Listings"
FROM players_sales
ORDER BY number_of_listings DESC;