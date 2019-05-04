{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import datetime as dt\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#File Load\n",
    "hitters = os.path.join(\"Resources\",\"raw_hitters.csv\")\n",
    "pitchers = os.path.join(\"Resources\",\"raw_pitchers.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#File encoding\n",
    "hitters_df = pd.read_csv(hitters, encoding=\"ISO-8859-1\")\n",
    "pitchers_df = pd.read_csv(pitchers, encoding=\"ISO-8859-1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#deleting player with no significant stats NaNs\n",
    "hitters_df.dropna(inplace = True)\n",
    "#hitters_df.head()\n",
    "pitchers_df.dropna(inplace = True)\n",
    "# pitchers_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#cleaning players to pass to Ebay\n",
    "#getting name column\n",
    "#splitting name out from name id\n",
    "hitters_df[['Name', 'NameID']]= hitters_df['Name'].str.split(\"\\\\\", expand = True)\n",
    "pitchers_df[['Name', 'NameID']]= pitchers_df['Name'].str.split(\"\\\\\", expand = True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#remove  * and # from name\n",
    "hitters_df[['Name', 'Ind']]= hitters_df['Name'].str.split(\"*\", expand = True)\n",
    "hitters_df[['Name', 'Ind1']]= hitters_df['Name'].str.split(\"#\", expand = True)\n",
    "pitchers_df[['Name', 'Ind']]= pitchers_df['Name'].str.split(\"*\", expand = True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "#hitters for MySQL Load & EBay\n",
    "\n",
    "#add timestamp\n",
    "hitters_df['DateTime'] = dt.datetime.now() \n",
    "\n",
    "#columns to keep for stats\n",
    "hitters_final_df = hitters_df[['Name','Tm','R','H','2B','3B','HR','RBI','BA','OBP','SLG','OPS','DateTime']]\n",
    "\n",
    "#remove duplicates\n",
    "hitters_final_df = hitters_final_df.drop_duplicates(subset=['Name'], keep='last')\n",
    " \n",
    "hitters_final_df.to_csv('output/hitters.csv', index = False, date_format='%Y-%m-%d %H:%M:%S')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#pitchers for MySQL Load & EBay\n",
    "\n",
    "#add timestamp\n",
    "pitchers_df['DateTime'] = dt.datetime.now() \n",
    "#columns to keep for stats\n",
    "pitchers_final_df = pitchers_df[['Name','Tm','W','L','ERA','G','GS','SV','IP','H','R','ER','HR','BB','SO','FIP',\n",
    "                                 'WHIP','H9','BB','SO9','DateTime']]\n",
    "\n",
    "#remove duplicates\n",
    "pitchers_final_df = pitchers_final_df.drop_duplicates(subset=['Name'], keep='last')\n",
    " \n",
    "pitchers_final_df.to_csv('output/pitchers.csv', index = False, date_format='%Y-%m-%d %H:%M:%S')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
