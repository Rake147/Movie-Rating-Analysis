#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd
movies = pd.read_csv('C:/Users/Rakesh/Datasets/movies.dat', delimiter='::')


# In[16]:


movies.head()


# In[17]:


movies.columns=['Id','Title','Genre']


# In[18]:


movies.head()


# In[19]:


ratings=pd.read_csv('C:/Users/Rakesh/Datasets/ratings.dat',delimiter='::')


# In[20]:


ratings.head()


# In[21]:


ratings.columns=['Users','Id','Rating','Timestamp']


# In[22]:


ratings.head()


# In[23]:


data=pd.merge(movies,ratings, on=['Id','Id'])


# In[24]:


data.head()


# In[25]:


ratings=data['Rating'].value_counts()
numbers=ratings.index
quantity=ratings.values

import plotly.express as px
fig = px.pie(data,values=quantity,names=numbers)
fig.show()


# In[27]:


data2 = data.query("Rating == 10")
print(data2["Title"].value_counts().head(10))


# In[ ]:




