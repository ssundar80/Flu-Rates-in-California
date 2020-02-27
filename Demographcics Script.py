#!/usr/bin/env python
# coding: utf-8

# In[401]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# # Import your bullshit

# In[402]:


import pandas as pd
import os
import csv
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import matplotlib.pyplot as plt


# # Google API Key
# from config import gkey


# In[403]:


# Set path for file

cities_pd = pd.read_csv("Untitled Folder/Flu Death Rate Data - csv.csv")
cities_pd.head(500)

cities_pd_df = pd.DataFrame(cities_pd)
# using apply function to create a new column 
cities_pd_df['Death Rate'] = cities_pd.apply(lambda row: row.Deaths / row.Population, axis=1)*100

cities_pd_df = cities_pd.rename(columns={"Ten-Year Age Groups Code": "Age"})
cities_pd_df = cities_pd.drop(columns=["Crude Rate", "Unnamed: 8", "Unnamed: 9","Ten-Year Age Groups Code.1"])
cities_pd_df


# # YEAR

# In[404]:


# Use GroupBy in order to separate the data by Year
grouped_years = cities_pd_df.groupby(['Year'])

#Calculate Total Death by Flu Rate for 2014 - 2018 by County
total_death_by_year = grouped_years["Deaths"].sum() / grouped_years["Population"].sum()
total_death_by_year = total_death_by_year * 100
total_death_by_year = round(total_death_by_year, 3)

total_death_by_year


# In[405]:


# visualize the gender data

fig8,ax8 = plt.subplots(figsize=[10,10])

death_year_graph = total_death_by_year
# death_year_graph.sort_values(by=0, inplace=True)
fig.tight_layout()
death_year_graph.plot(kind='line', ax=ax8)

labels9 = ['0.0','0.1%', '0.2%', '0.3%', '0.4%','0.5%', '0.6%','0.7%', '0.8%','0.9%', '1.0%']
ax8.set_yticklabels(labels9,fontname='Arial', fontsize='12')

labels10 =['2014','','2015','','2016','', '2017', '', '2018']
ax8.set_xticklabels(labels10, rotation = 'horizontal', fontname='Arial', fontsize='12')

ax8.set_ylabel('Death Rate', fontname='Arial', fontsize='16')
ax8.set_xlabel('Year',fontname='Arial', fontsize='16')

ax8.set_title('Percent Death Caused By Flu by Year',fontname='Arial', fontsize='20');
ax8.grid()


# # COUNTY

# In[406]:


total_death_by_year.mean()
print("Average Rate of Death by Influenza 2014 - 2018: " + str(total_death_by_year.mean()) + "%")


# In[407]:


# gather counts
county_death_counts = cities_pd_df.groupby(["County"])
total_death_by_county = county_death_counts["Deaths"].sum()
total_death_by_county


# In[469]:


fig16,ax16 = plt.subplots(figsize=[20,20])
county_counts_graph = total_death_by_county
fig.tight_layout()
county_counts_graph.plot(kind='bar', facecolor='red', ax=ax16, legend=False)
ax16.set_title("Numbers of Deaths by County from 2014-2018", fontname='Arial', fontsize='25');

labels18 = ["Alameda",
            "Amador",
            "Butte",
            "Calaveras",
            "Colusa",
            "Contra Costa",
            "Del Norte",
            "El Dorado",
            "Fresno",
            "Glenn",
            "Humboldt",
            "Imperial",
            "Inyo",
            "Kern",
            "Kings",
            "Lake",
            "Lassen",
            "Los Angeles",
            "Madera",
            "Marin",
            "Mariposa",
            "Mendocino",
            "Merced",
            "Modoc",
            "Mono",
            "Monterey",
            "Napa",
            "Nevada",
            "Orange",
            "Placer",
            "Plumas",
            "Riverside",
            "Sacramento",
            "San Benito",
            "San Bernardino",
            "San Diego",
            "San Francisco",
            "San Joaquin",
            "San Luis Obispo",
            "San Mateo",
            "Santa Barbara",
            "Santa Clara",
            "Santa Cruz",
            "Shasta",
            "Sierra",
            "Siskiyou",
            "Solano",
            "Sonoma",
            "Stanislaus",
            "Sutter",
            "Tehama",
            "Trinity",
            "Tulare",
            "Tuolumne",
            "Ventura",
            "Yolo",
            "Yuba"]
ax16.set_xticklabels(labels18)
labels2 =['0','10000','25000','50000','100000','200000','300000']
ax16.set_yticklabels(labels2)
ax16.set_ylabel('Number Dead by Flu 0 - 400,000 ', fontname='Arial', fontsize='20')
ax16.set_xlabel('California Counties', fontname='Arial', fontsize='16');
ax16.grid(axis='y')


# In[ ]:





# In[409]:


grouped_counties = cities_pd_df.groupby(['County'])

#Calculate Total Death by Flu Rate for 2014 - 2018 by County
total_death_by_county = grouped_counties["Deaths"].sum() / grouped_counties["Population"].sum()
total_death_by_county = total_death_by_county * 100
total_death_by_county = round(total_death_by_county, 3)

total_death_by_county.head()


# In[449]:


# Create a scatter plot by county

fig,ax = plt.subplots(figsize=[16,12])

county_death_graph = total_death_by_county.reset_index().copy()
county_death_graph.sort_values(by=0, inplace=True);
fig.tight_layout()
county_death_graph.plot(kind="bar", facecolor="salmon", ax=ax, legend= False)
rot= .5

ax.set_ylabel('Death Rate by Flu', fontname='Arial', fontsize='16')
ax.set_xlabel('Counties in California',fontname='Arial', fontsize='16')

ax.set_title('Death Rate by California County',fontname='Arial', fontsize='20');



labels = ["Alameda County","Amador County","Butte County","Calaveras County","Colusa County","Contra Costa County","Del Norte County","El Dorado County","Fresno County","Glenn County","Humboldt County","Imperial County","Inyo County","Kern County","Kings County","Lake County","Lassen County","Los Angeles County","Madera County","Marin County","Mariposa County","Mendocino County","Merced County","Modoc County","Monterey County","Napa County","Nevada County","Orange County","Placer County","Plumas County"
,"Riverside County"
,"Sacramento County"
,"San Benito County"
,"San Bernardino County"
,"San Diego County"
,"San Francisco County"
,"San Joaquin County"
,"San Luis Obispo County"
,"San Mateo County"
,"Santa Barbara County"
,"Santa Clara County"
,"Santa Cruz County"
,"Shasta County"
,"Siskiyou County"
,"Solano County"
,"Sonoma County"
,"Stanislaus County"
,"Sutter County"
,"Tehama County"
,"Trinity County"
,"Tulare County"
,"Tuolumne County"
,"Ventura County"
,"Yolo County"
,"Yuba County"
,"Mono County"
,"Sierra County"]
ax.set_xticklabels(labels,rotation="vertical", fontname='Arial', fontsize='14', minor=False);
ax.grid(axis='y')
labels4 =['0%', '2%', '4%', '6%', '8%', '10%','12%','14%']
ax.set_yticklabels(labels4);

plt.show();
plt.savefig("../../../Desktop/Death Rate by California County.png");


# In[411]:


# Use GroupBy in order to separate the data by Gender

grouped_gender = cities_pd_df.groupby(['Gender'])

total_death_by_gender = grouped_gender["Deaths"].sum() / grouped_gender["Population"].sum()
total_death_by_gender = total_death_by_gender * 100
total_death_by_gender = round(total_death_by_gender, 3)
total_death_by_gender.head()


# In[421]:


# gather counts
gender_death_counts = cities_pd_df.groupby(["Gender"])
gender_death_counts = gender_death_counts["Deaths"].sum()
gender_death_counts




# In[425]:


#set up bool
positive = gender_death_graph['Gender']=='Male'
positive


# In[446]:


fig25,ax25 = plt.subplots(figsize=[10,10])
gender_counts_death_graph = gender_death_counts.reset_index().copy()

gender_counts_death_graph

fig.tight_layout()

gender_counts_death_graph.plot(kind="bar", color=[positive.map({True:'lightblue',False:'pink'})]
                        , ax=ax25, legend=False)
ax25.set_title("Total Number of Deaths by Gender", fontname='Arial', fontsize='25');
labels1=["Female","Male"]
ax25.set_xticklabels(labels1);

plt.savefig("../../../Desktop/Total Deaths by Gender.png")


# # GENDER

# In[413]:



#set up bool
positive = gender_death_graph['Gender']=='Male'
positive


# In[439]:


fig5,ax5 = plt.subplots(figsize=[10,10])
gender_death_graph = total_death_by_gender.reset_index().copy()
gender_death_graph.sort_values(by=0, inplace=True)


gender_death_graph.plot(kind="bar", color=[positive.map({True:'salmon',False:'lightblue'})]
                        , ax=ax5, legend=False,)
ax5.set_yticklabels(labels5,fontname='Arial', fontsize='12')
labels5 =['0.00','0.01%', '0.02%', '0.03%', '0.04%','0.05%', '0.06%','0.07%', '0.08%','0.09%', '0.10%',]

labels6 =['Female','Male']
ax5.set_xticklabels(labels6, rotation = 'horizontal', fontname='Arial', fontsize='12')

ax5.set_ylabel('Death Rate', fontname='Arial', fontsize='16')
ax5.set_xlabel('Gender',fontname='Arial', fontsize='16')

ax5.set_title('Death Rate by Gender',fontname='Arial', fontsize='20')


fig.tight_layout()
rot= .75


# fig5

plt.savefig("../../../Desktop/18-final-plot.png")


# In[ ]:





# # RACE

# In[352]:


# Use GroupBy in order to separate the data by Race
grouped_race = cities_pd.groupby(["Race"])
total_death_by_race = grouped_race['Deaths'].sum() / grouped_race['Population'].sum()
total_death_by_race = total_death_by_race * 100
total_death_by_race = round(total_death_by_race, 3)
total_death_by_race.head()


# In[357]:


# gather counts
race_death_counts = cities_pd_df.groupby(["Race"])
race_death_counts = race_death_counts["Deaths"].sum()
race_death_counts


# In[432]:


fig15,ax15 = plt.subplots(figsize=[10,10])
race_counts_graph = race_death_counts.reset_index().copy()
fig.tight_layout()
race_counts_death_graph.plot(kind='bar', facecolor='yellow', ax=ax15, legend=False)
ax15.set_title('Race Counts');

labels15 = ['American Indian or Alaska Native','Asian or Pacific Islander','Black','White']
ax15.set_xticklabels(labels15,rotation='vertical');
labels2 =['0', '200000', '300000', '400000', '500000', '1000000']
ax15.set_yticklabels(labels2);


# In[433]:


fig10,ax10 = plt.subplots()
race_death_graph = total_death_by_race.reset_index().copy()
race_death_graph.sort_values(by=0,inplace=True)
fig.tight_layout()
race_death_graph.plot(kind='bar', facecolor='brown', ax=ax10, legend=False);
ax10.set_title('Death Rate by Race')
labels = ['Asian or Pacific Islander','American Indian or Alaska Native','White','Black']
ax10.set_xticklabels(labels,rotation='vertical');
labels2 =['0%', '0.2%', '0.4%', '0.6%', '0.8%', '1.0%']
ax10.set_yticklabels(labels2);


# In[434]:


# Use GroupBy in order to separate the data by Age
grouped_age = cities_pd.groupby(["Ten-Year Age Groups Code"])
total_death_by_age = grouped_age['Deaths'].sum() / grouped_age['Population'].sum()
total_death_by_age = total_death_by_age * 100
total_death_by_age = round(total_death_by_age, 3)
total_death_by_age


# In[435]:


fig13,ax13 = plt.subplots(figsize=[10,10])
age_death_rate = total_death_by_age.reset_index()
age_death_rate['sort'] = [0,1,3,4,5,6,2,7,8,9,10]
age_death_rate.sort_values(by=0, inplace=True)

age_death_rate

# visualize the age group data

age_death_rate[['Ten-Year Age Groups Code', 0]].plot(kind='bar', facecolor='green', ax=ax13, legend=False)
ax.set_xticks(range(0, 11))
ax.set_xticklabels(age_death_rate['Ten-Year Age Groups Code'])
ax.ylim = [0,20]

ax13.set_title('Death Rate by Age Group')


# In[ ]:





# In[ ]:




