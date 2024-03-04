#!/usr/bin/env python
# coding: utf-8

# In[255]:


import re
from bs4 import BeautifulSoup, NavigableString
import requests
import pandas as pd
import time


# In[256]:


home_url = "http://joannanewsomlyrics.com"
try: 
    response = requests.get(home_url)
    response.raise_for_status()
except requests.exceptions.RequestException as e: 
    print(f"Error fetching {home_url}: {e}")
else: 
    soup = BeautifulSoup(response.content, 'html.parser')


# In[257]:


albums_divs = soup.find_all('div', class_='title')
print(f"Found {len(albums_divs)} album divs")

all_songs = []

for album_div in albums_divs:
    album_name = album_div.get_text(strip=True)
    print(f"Album Name: {album_name}")
    
    current_sibling = album_div.next_sibling
    
    while current_sibling:
        if isinstance(current_sibling, NavigableString): 
            current_sibling = current_sibling.next_sibling
        elif current_sibling.get('class') == ['track-list']:
            break
        else: 
            current_sibling = current_sibling.next_sibling
        
        if current_sibling:
            songs_ol = current_sibling.find('ol')
            if songs_ol:
                songs = songs_ol.find_all('a', href=True)
                print(f"Found {len(songs)} songs in album {album_name}")
                
                for song in songs: 
                    song_title = song.get_text(strip=True)
                    print(f"Song Title: {song_title}")
                    song_url = song['href']
                    if not song_url.startswith('http'):
                        song_url = home_url + song_url
                    try: 
                        song_response = requests.get(song_url)
                        song_soup = BeautifulSoup(song_response.content, 'html.parser')
                        lyrics_p = song_soup.find('p', class_='lyrics')
                        lyrics = lyrics_p.get_text(strip=True) if lyrics_p else 'Lyrics not found'
                    except requests.exceptions.RequestException as e: 
                        print(f"Error fetching {song_url}: {e}")
                        lyrics = "Error fetching lyrics"

                    all_songs.append({'Album': album_name, 'Song': song_title, 'Lyrics': lyrics})
                    time.sleep(1)


# In[258]:


print(all_songs)


# In[278]:


def transform_lyrics(text):
    if isinstance(text, str):
        text = re.sub(r"(\w)([A-Z])", r"\1 \2", text)
        text = re.sub(r"([;,.])(?!\s)", r"\1 ", text)
        return text


# In[279]:


df = pd.DataFrame(all_songs)


# In[280]:


df['Lyrics']=df['Lyrics'].apply(transform_lyrics)


# In[281]:


df.to_csv('joanna_newsom_lyrics.csv', index=False)


# In[282]:


for index, row in df.head(5).iterrows():
    print(f"Lyrics for Song {index + 1}:")
    print(row['Lyrics'])
    print("\n---\n")


# In[283]:


df = pd.DataFrame(all_songs)
df.to_csv('joanna_newsom_lyrics.csv', index=False)


# In[ ]:





# In[ ]:




