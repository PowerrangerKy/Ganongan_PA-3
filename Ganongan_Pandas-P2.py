#!/usr/bin/env python
# coding: utf-8

# ## Problem 1

# In[56]:


#it Prints data frame with odd-numbered columns that contains the first five rows
odd = cars.iloc[:5,::2]
odd


# In[58]:


#it Prints the row for the model "Mazda RW4 Wag
cars.loc[[1]] 


# In[60]:


#it Prints the cyl value for the model "Camaro Z28" 
cars.loc[[23],['cyl']]


# In[62]:


#it Prints the cyl and gear of the mazda, honda, and ford
cars.loc[[1,18,28],['Model','cyl','gear']] 

