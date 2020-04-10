# -*- coding: utf-8 -*-
"""covid19 Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bEZvSoPd1Q26Z2RXDMfU6pnzTxcb8jO3
"""

# initilizing pckages

import pandas as pd
import geopandas as gpd
import descartes
import matplotlib.pyplot as plt
import requests

# Saving the links in variables

confirmed_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
recovered_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
death_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

# reading the csv files from the links

df_confirmed = pd.read_csv(confirmed_cases_url)
df_recovered = pd.read_csv(recovered_cases_url)
df_deaths = pd.read_csv(death_cases_url)

# viewing the first five lines

df_confirmed.head()

# To check the shape(no of rows and columns) of data

df_confirmed.shape

# checking the name of columes here 80 columns

df_confirmed.columns

# melting the additonal columns except (state,country,lat,long) in to one column

df_confirmed.melt(id_vars=['Province/State','Country/Region','Lat','Long'])

# changing the "variable" column to Date and there value to confirm, death and recovered according to respective dataset

confirm_df = df_confirmed.melt(id_vars=['Province/State','Country/Region','Lat','Long'])
confirm_df.rename(columns={'variable':'Date','value':'Confirmed'},inplace=True)

recovered_df = df_recovered.melt(id_vars=['Province/State','Country/Region','Lat','Long'])
recovered_df.rename(columns={'variable':'Date','value':'Recovered'},inplace=True)

deaths_df = df_deaths.melt(id_vars=['Province/State','Country/Region','Lat','Long'])
deaths_df.rename(columns={'variable':'Date','value':'Deaths'},inplace=True)

# Viewing the last five rows

confirm_df.tail()

# creating a function for melting

def get_n_melt_data(data_url,case_type):
  df = pd.read_csv(data_url)
  melted_df = df.melt(id_vars=['Province/State','Country/Region','Lat','Long'])
  melted_df.rename(columns={'variable':'Date','value':'Deaths'},inplace=True)
  return melted.df

# viewing first five rows of recovered dataset to see changes got effective or not

recovered_df.head()

deaths_df.head()

confirm_df.head()

# joining all three dataset in to one

final_df = confirm_df.join(recovered_df["Recovered"]).join(deaths_df["Deaths"])

final_df.tail()

# plotting the points according to country long and lat

gdf01 =gpd.GeoDataFrame(final_df,geometry = gpd.points_from_xy(final_df['Long'],final_df['Lat']))

gdf01.plot(figsize=(20,10))

# loading the world map form geopandas  

world = gpd.read_file(
    gpd.datasets.get_path('naturalearth_lowres'))

ax = world.plot(figsize=(20,10))

# removing the axis... 

ax.axis('off')

# merging the points into worldmap

fig,ax =plt.subplots(figsize=(50,20))
gdf01.plot(cmap='Purples',ax=ax)
world.geometry.boundary.plot(color=None,edgecolor='k',linewidth=1,ax=ax)
ax.axis('off')

