#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
x=os.getcwd()
y=os.listdir(x)
os.chdir('/Users/nick/Documents/Python Scripts')
x


# In[9]:


import pandas as pd
import numpy as np
from pandas import DataFrame as df
import requests
import urllib.request
from bs4 import BeautifulSoup


# In[10]:


# input the url to scrap data from 
# response with the value <200> means that the request was successful
url="https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2"
response=requests.get(url)
response


# In[11]:


# identify the data you are intersted in..i choose product,price and ratings and initialize them on an empty list
product_name=[]#list the name of the product
price=[]#lists the price of the product
ratings=[]#lists the ratings  of the product



# In[46]:


# parse the data with Beautifulsoup so we can have nice nested beautfulsoup data structures

soup=BeautifulSoup(response.text,"html.parser")


# we iterate items in the response text to find all items in the "a" tags since we found out the information we
# are looking for are nested in the "div" tags
for a in soup.findAll('a',href=True,attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34'})
product_name.append(name.text)
price.append(price.text)
ratings.append(rating.text) 
    


# In[50]:


# creating a dataframe to store the scrapped data.
# store the datafram in a csv file "flipkart_dataset"
df=pd.DataFrame({"Product_name":{product_name},"Price":{price},"Ratings":{ratings}})
df
df.to_csv("Flipkart_dataset", encoding='utf-8')
df

