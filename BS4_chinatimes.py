
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup
url = 'https://www.chinatimes.com/'
r = requests.get(url)

if r.status_code == requests.codes.ok:
  soup = BeautifulSoup(r.text, 'html.parser')

  titles = soup.find_all('h4', class_='title', limit=7)
  for title in titles:
        print(title.select_one("a").text)
        print('網址: '+ title.select_one("a").get("href")+'\n')

