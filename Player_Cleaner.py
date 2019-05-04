import pandas as pd
import datetime as dt
import os
#File Load
hitters = os.path.join("Resources","raw_hitters.csv")
pitchers = os.path.join("Resources","raw_pitchers.csv")
#File encoding
hitters_df = pd.read_csv(hitters, encoding="ISO-8859-1")
pitchers_df = pd.read_csv(pitchers, encoding="ISO-8859-1")
#deleting player with no significant stats NaNs
hitters_df.dropna(inplace = True)
#hitters_df.head()
pitchers_df.dropna(inplace = True)
# pitchers_df.head()
#cleaning players to pass to Ebay
#getting name column
#splitting name out from name id
hitters_df[['Name', 'NameID']]= hitters_df['Name'].str.split("\\", expand = True)
pitchers_df[['Name', 'NameID']]= pitchers_df['Name'].str.split("\\", expand = True)
#remove  * and # from name
hitters_df[['Name', 'Ind']]= hitters_df['Name'].str.split("*", expand = True)
hitters_df[['Name', 'Ind1']]= hitters_df['Name'].str.split("#", expand = True)
pitchers_df[['Name', 'Ind']]= pitchers_df['Name'].str.split("*", expand = True)

#player name file generation for EBay load 
hitters_name_df = hitters_df['Name']
pitchers_name_df = pitchers_df['Name']
players_df = pd.concat([hitters_name_df,pitchers_name_df])
players_df = players_df.drop_duplicates()
players_df.to_csv(os.path.join("Output","players.csv"), index = False, header = True)

#hitters for MySQL Load 
#add timestamp
hitters_df['DateTime'] = dt.datetime.now() 

#columns to keep for stats
hitters_final_df = hitters_df[['Name','Tm','R','H','2B','3B','HR','RBI','BA','OBP','SLG','OPS','DateTime']]

#remove duplicates
hitters_final_df = hitters_final_df.drop_duplicates(subset=['Name'], keep='last')
 
hitters_final_df.to_csv(os.path.join("Output","hitters.csv"), index = False, date_format='%Y-%m-%d %H:%M:%S')
#pitchers for MySQL Load

#add timestamp
pitchers_df['DateTime'] = dt.datetime.now() 
#columns to keep for stats
pitchers_final_df = pitchers_df[['Name','Tm','W','L','ERA','G','GS','SV','IP','H','R','ER','HR','BB','SO','FIP',
                                 'WHIP','H9','BB','SO9','DateTime']]

#remove duplicates
pitchers_final_df = pitchers_final_df.drop_duplicates(subset=['Name'], keep='last')
 
pitchers_final_df.to_csv(os.path.join("Output","pitchers.csv"), index = False, date_format='%Y-%m-%d %H:%M:%S')
print ("Processing Complete")
