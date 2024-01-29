#!/usr/bin/env python
# coding: utf-8

# In[1]:


import statistics as st
import pandas as pd


# In[2]:


dataset = pd.read_csv("Housing.csv")
print(dataset)


# In[3]:


price = dataset['price']
print("The average price of house is",st.mean(price))


# In[4]:


print("The mode price of house is",st.mode(price))


# In[5]:


print("The median value of all the prices is",st.median(price))


# In[6]:


print("The harmonic mean of the prices is", st.harmonic_mean(price))


# In[7]:


print("The median low of the price is", st.median_low(price))


# In[8]:


print("The median high of the price is",st.median_high(price))


# In[9]:


print("The grouped median of the house price is", st.median_grouped(price))


# In[15]:


bedrooms = dataset['bedrooms']
print("The variance of the no. of bedrooms is ", st.variance(bedrooms))


# In[11]:


print("The pvariance of the no. of bedrooms is", st.pvariance(bedrooms))


# In[12]:


print("The standard deviation of house prices is", st.stdev(price))


# In[13]:


numDataset = dataset.iloc[:,0:4]
print("The mean of the dataset are:-\n",numDataset.mean())
print("The mode of the dataset are:-\n",numDataset.mode())
print("The symmetry of the dataset are:-\n",numDataset.skew())


# In[ ]:





# In[ ]:





# In[ ]:




