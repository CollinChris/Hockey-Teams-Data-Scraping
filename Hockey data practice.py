#!/usr/bin/env python
# coding: utf-8

# In[273]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[275]:


hockey_data = []

def scrape_page(page):
    url = f'https://www.scrapethissite.com/pages/forms/?page_num={page}'
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    team_stats = soup.find_all('tr', class_='team')
    
    for team in team_stats:
        team_name = team.find('td', class_='name').get_text(strip=True)
        year = team.find('td', class_='year').get_text(strip=True)
        wins = team.find('td', class_='wins').get_text(strip=True)
        losses = team.find('td', class_='losses').get_text(strip=True)
    
        hockey_data.append({'team':team_name, 'year':year,'wins':wins, 'losses':losses})


# In[277]:


for page in range(24):
    print("running")
    scrape_page(page+1)


# In[279]:


df = pd.DataFrame(hockey_data)


# In[281]:


df


# In[285]:


df.to_csv('Hockey_data.csv', index=0)


# In[ ]:





# In[ ]:





# In[171]:





# In[189]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




