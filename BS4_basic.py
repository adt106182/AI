
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
html_doc="""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>莊惟恩</title>
</head>

<body>
<h2>莊惟恩</h2>
<p>ADT106182</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
</body>
</html>"""

soup=BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())


# In[2]:


title_tag=soup.title
print(title_tag)


# In[7]:


a_tags=soup.find_all('a')
for tag in a_tags:
    print('連結:'+tag.string+'=>'+'連結網址:'+tag.get('href'))

