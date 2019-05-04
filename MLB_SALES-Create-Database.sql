-- Creation of database for MLB roster and EBAY sales 11:09 AM
-- DROP DATABASE MLB_SALES;
CREATE DATABASE MLB_SALES;
USE MLB_SALES;

-- Create team table
CREATE TABLE teams_dim (
    team_abbr VARCHAR(30),
    team_name VARCHAR(30),
    id INT AUTO_INCREMENT NOT NULL,
    PRIMARY KEY (id)
);

-- Creation of Pitchers Tables
-- Name	Tm	R	H	2B	3B	HR	RBI	BA	OBP	SLG	OPS	DateTime
CREATE TABLE hitters (
	name VARCHAR(30),
    team VARCHAR(10),
    R INT,
	H INT,
	2B	INT,
    3B	INT,
    HR	INT,
    RBI	INT,
    BA	FLOAT(5,4),
    OBP	FLOAT(5,4),
    SLG	FLOAT(5,4),
    OPS FLOAT(5,4),
    date VARCHAR(20),
    id INT AUTO_INCREMENT NOT NULL,
  PRIMARY KEY (id)
);
-- Creation of Pitchers Tables
-- Name	Tm	W	L	ERA	G	GS	SV	IP	H	R	ER	HR	BB	SO	FIP	WHIP	H9	BB	SO9	DateTime
CREATE TABLE pitchers (
	name VARCHAR(30),
    team VARCHAR(10),
    W	INT,
    L	INT,
    ERA_G	INT,
    G INT,
    GS	INT,
    SV	INT,
    IP	INT,
    H	INT,
    R	INT,
    ER	INT,
    HR	INT,
    BB	INT,
    SO	INT,
    FIP	INT,
    WHIP	INT,
    H9	INT,
    BB9	INT,
    SO9 INT,
    date VARCHAR(20),
    id INT AUTO_INCREMENT NOT NULL,
  PRIMARY KEY (id)
);
-- Create table for ebay items by player
CREATE TABLE ebay_items_player (
	id INT NOT NULL,
    date_time VARCHAR(20),
    player_name VARCHAR(30),
    number_of_listings INT,
    PRIMARY KEY (id)
);

-- Create table for ebay items by team
CREATE TABLE ebay_items_team (
	id INT NOT NULL,
    date_time VARCHAR(20),
    team_name VARCHAR(30),
    number_of_listings INT,
    
    PRIMARY KEY (id)
);

-- Create a View Unioning Pitchers and Hitters
-- DROP VIEW Combined;
CREATE VIEW MLB_SALES.Combined
AS 
select * from (select name, date, team 
from pitchers 
union all
select name, date, team from hitters) as c 
LEFT JOIN teams_dim t
ON c.team = t.team_abbr;

select * from MLB_SALES.Combined;

-- Join Combined with ebay
CREATE VIEW MLB_SALES.players_sales
AS
SELECT c.name, c.team, c.team_name, e.number_of_listings, c.date 
FROM Combined c
LEFT JOIN ebay_items_player e
ON c.name = e.player_name
GROUP BY c.name, c.date, c.team;

select * from players_sales;
--  +++++++++++++++++++++++++++++++++++++++++

-- Summarize by Team and Combine with EBAY
CREATE VIEW MLB_SALES.team_sales
AS
SELECT c.team, c.team_name, e.number_of_listings, c.date 
FROM Combined c
LEFT JOIN ebay_items_team e
ON c.team_name = e.team_name
GROUP BY c.date, c.team, c.team_name;

select * from MLB_SALES.team_sales;