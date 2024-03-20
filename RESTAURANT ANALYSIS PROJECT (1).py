#!/usr/bin/env python
# coding: utf-8

# # IMPORTING LIBRARIES

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mlp


# # GETTING DATASET

# In[2]:


df = pd.read_csv("Downloads/dataset.csv")


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.shape


# # DATASET CLEANING

# In[7]:


df.isnull().sum()


# In[8]:


df.info()


# # NO OF RESTAURANT 

# In[9]:


len(df['Restaurant Name'])


# # COUNTRIES WITH CODE

# In[10]:


c_code = df.groupby('City')['Country Code'].unique()
c_code


# # CITY WISE COUNT OF RESTAURANT

# In[11]:


count_by_city = df['City'].value_counts()
count_by_city


# # CUISINES COMBINATION

# In[12]:


cuisines_combo = df['Cuisines'].str.split(",").explode()
cuisines_combo_count  = cuisines_combo.value_counts()
cuisines_combo_count


# # AVERAGE OF CUISINES WITH AGGREGATE RATING

# In[13]:


avg_rating = df.groupby('Cuisines')['Aggregate rating'].mean()
avg_rating


# # HIGHEST AVERAGE COST FOR TWO

# In[14]:


high_cost = df.groupby('Cuisines')['Average Cost for two'].value_counts().sort_values(ascending=False)
high_cost


# # TOTAL CURRENCY OF AVERAGE COST FOR TWO

# In[15]:


curr = df.groupby('Currency')['Average Cost for two'].sum().sort_values(ascending=False)
curr


# # TABLE BOOKING COUNT BY CITY

# In[16]:


tab_book = df.groupby('City')['Has Table booking'].value_counts().sort_values(ascending=False)
tab_book


# # COUNT OF RATING COLOUR BY ID

# In[17]:


sns.barplot(x='Rating color',y='Restaurant ID',data=df).set(title='Count of Rating colour by id')


# # COUNT OF RATING TEXT BY ID

# In[18]:


sns.boxplot(x='Rating text',y='Restaurant ID',data=df).set(title='Count of Rating text by id')


# # TABLE BOOKING

# In[19]:


cit=df.groupby('City')
tab_book=df['Has Table booking'].value_counts()
cit
tab_book


# # ONLINE DELIVERY

# In[20]:


on_deli=df['Has Online delivery'].value_counts()
on_deli


# In[21]:


deli_or_not=df['Is delivering now'].value_counts()
deli_or_not


# # HIGHEST VOTING BY CUISINES

# In[22]:


high_vote = df.groupby('Cuisines')['Votes'].sum().sort_values(ascending=False)
high_vote


# # HIGHEST VOTING BY CITY

# In[23]:


high_vote_city = df.groupby('City')['Votes'].sum().sort_values(ascending=False)
high_vote_city


# # TABLE BOOKING BY CURRENCY

# In[24]:


curr_book=df.groupby('Currency')['Has Table booking'].value_counts().sort_values(ascending=False) 
curr_book


# In[ ]:





# In[26]:


get_ipython().system('pip install folium')


# In[28]:


import folium
import plotly.express as px


# In[31]:


map=folium.Map(location=[df["Longitude"].iloc[0],df["Latitude"].iloc[0]],zoom_start=14)


# In[35]:


for index,row in df.iterrows():
    latitude = row['Latitude']
    longitude = row['Longitude']
    name=row['Restaurant Name']
    folium.Marker(location=[latitude,longitude],popup=name).add_to(map)
map


# In[ ]:




