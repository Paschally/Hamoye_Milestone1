#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# check filepath

import os
os.getcwd()


# In[3]:


# import the dataset

df = pd.read_csv("FoodBalanceSheets_E_Africa_NOFLAG.csv", encoding = 'latin-1')


# In[4]:


# check a sample of dataset 

df.sample()


# In[5]:


# List out all column titles

df.columns


# In[6]:


# Use the 5 point summary to check the datset

df.describe()


# In[7]:


# Select columns ‘Y2017’ and ‘Area’, Perform a groupby operation on ‘Area’.  Which of these Areas had the highest sum in 2017?

df.groupby('Area')[ 'Y2017'].sum()


# In[8]:


# Perform a groupby operation on ‘Element’.  What is the total number of the sum of Processing in 2017?

df.groupby('Element')[ 'Y2017'].sum()


# In[9]:


# Answer the following questions based on the African food production dataset provided by the FAO website already provided
# What is the total sum of Wine produced in 2015 and 2018 respectively?

a_wine = df.groupby('Item')[ 'Y2015'].sum()
a = a_wine['Wine']

b_wine = df.groupby('Item')[ 'Y2018'].sum()
b = b_wine['Wine']

print(f'The totatl sum of wine produced in 2015 and 2018 is {a} and {b} respectively ')


# In[10]:


#. Which year had the least correlation with ‘Element Code’?

df.corr()


# In[11]:


#. What is the mean and standard deviation across the whole dataset for the year 2017 to 2 decimal places?

df['Y2017'].mean()
df['Y2017'].std()


# In[12]:


#. Select columns ‘Y2017’ and ‘Area’, Perform a groupby operation on ‘Area’.  Which of these Areas had the 7th lowest sum in 2017?

area_df = df.groupby('Area')[ 'Y2017'].sum()
sorted_df = area_df.sort_values()
sorted_df.head(7)


# In[13]:


# Perform a groupby operation on ‘Element’.  What year has the highest sum of Stock Variation?

area_df = df.groupby('Element').sum()
area_df


# In[14]:


# Question 17.  What is the total Protein supply quantity in Madagascar in 2015?

df_madagascar = df[df['Area'] == 'Madagascar']
df_madagascar.groupby('Element')['Y2015'].sum()


# In[15]:


# Question 18.. What is the total number and percentage of missing data in 2014 to 3 decimal places?

df_Y2014_null = df['Y2014'].isnull().sum()
missing = (df_Y2014_null/len(df))*100

print(f'The total number of missing data in 2014 is {df_Y2014_null} which is {missing:.3f} % of data in the year')


# In[16]:


# Question 19 How would you check for the number of rows and columns in a pandas DataFrame named df?

df.shape


# In[17]:


# Question 20.. What is the total number of unique countries in the dataset?

df.Area.nunique()


# In[ ]:




