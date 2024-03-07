#!/usr/bin/env python
# coding: utf-8

# In[123]:


import pandas as pd
import string


# In[124]:


df = pd.read_csv('joanna_newsom_lyrics_cleaned.csv') 


# In[125]:


pd.options.display.max_colwidth = 50000


# In[126]:


df.head()


# In[127]:


len(songs)


# In[11]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[12]:


import nltk
from nltk.corpus import stopwords


# In[13]:


stop_words = stopwords.words('english')


# In[15]:


vectorizer = TfidfVectorizer(stop_words = stop_words, min_df = 0.02875)


# In[18]:


tfidf = vectorizer.fit_transform(songs['Lyrics'])


# In[19]:


from sklearn.decomposition import NMF


# In[31]:


nmf = NMF(n_components = 5)


# In[32]:


topic_values = nmf.fit_transform(tfidf)


# In[33]:


for topic_num, topic in enumerate(nmf.components_):
    message = "Topic #{}: ".format(topic_num + 1)
    message += " ".join([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[:-11 :-1]])
    print(message)


# In[ ]:


topic_labels = ['Romantic Musings', 'Comtemplative Imagery and Philosophical Inquiry', "Morning and Mysticism, Awakening, Revelation", 'Metamorphosis and Vision', 'Solitude, Longing, Quiet Introspection']

