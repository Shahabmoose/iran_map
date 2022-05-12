#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install folium


# In[54]:


pip install pandas


# In[6]:


import folium
iran_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)
iran_map


# In[71]:


import pandas as pd
ubaar = pd.read_csv("C:\\Users\\shahab\\Desktop\\ubaar-competition\\train.csv")
sample_ubaar = ubaar.head(1000)
ubaar.head()


# In[72]:


for lat, lng in zip(sample_ubaar.sourceLatitude,sample_ubaar.sourceLongitude):
    folium.CircleMarker(
        [lat, lng],
        radius=2,
        color='red',
        fill=True,
        fill_color='darkred',
        fill_opacity=0.5 ).add_to(iran_map)
iran_map


# In[75]:


for lat, lng in zip(sample_ubaar.destinationLatitude,sample_ubaar.destinationLongitude):
 folium.CircleMarker(
    [lat, lng],
    radius=2,
    color='blue',
    fill=True,
    fill_color='blue',
    fill_opacity=0.3 ).add_to(iran_map)
iran_map


# In[100]:


iran_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)


# In[101]:


for row in range(sample_ubaar.shape[0]):
    folium.CircleMarker(
         location=[sample_ubaar.iloc[row,:]['sourceLatitude'],
         sample_ubaar.iloc[row,:]['sourceLongitude']],
         radius=int(sample_ubaar.iloc[row,:]['price']),
         color='red',
         fill=True,
         fill_color='darkred',
         fill_opacity = 0.7
         ).add_to(iran_map)


# In[102]:


iran_map


# In[108]:


iran_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)


# In[109]:


for row in range(sample_ubaar.shape[0]):
    folium.CircleMarker(
        location=[sample_ubaar.iloc[row,:]['destinationLatitude'],
        sample_ubaar.iloc[row,:]['destinationLongitude']],
        radius=int(sample_ubaar.iloc[row,:]['price']),
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity = 0.1
        ).add_to(iran_map)
iran_map


# In[110]:


iran_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)


# In[111]:


iran_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)
from folium.plugins import HeatMap
iran_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)
iran_map


# In[112]:


ubaar['price_normalized'] = (ubaar['price'] - ubaar['price'].min())/ ubaar['price'].max()
HeatMap(
 data=list(zip(ubaar.head(20000)['sourceLatitude'],
 ubaar.head(20000)['sourceLongitude'],
 ubaar.head(20000)['price_normalized'])
 ) ,
 radius = 12
).add_to(iran_map)
iran_map


# In[ ]:




