#!/usr/bin/env python
# coding: utf-8

# In[71]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[72]:


home_url = "http://joannanewsomlyrics.com"
response = requests.get(home_url)
soup = BeautifulSoup(response.content, 'html.parser')


# In[76]:


album_divs = soup.find_all('div', class_='title')


# In[84]:


all_songs = []


# In[85]:


for album_div in albums_divs:
    album_name = album_div.get_text(strip=True)
    track_list_div = album_div.find_next_sibling('div', class_='track-list')
    
    if track_list_div: 
        songs_ol = track_list_div.find('ol')


# In[60]:


print(lyrics_dict)


# In[ ]:




