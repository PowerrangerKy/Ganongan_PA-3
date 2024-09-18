#!/usr/bin/env python
# coding: utf-8

# ## Problem 1

# In[50]:


import pandas as pd

#Input the cars.csv file here in jupyter
cars = pd.read_csv('cars.csv')
cars


# In[52]:


#it prints the first 5 rows
cars.head()


# In[54]:


#it prints the last 5 rows
cars.tail()

