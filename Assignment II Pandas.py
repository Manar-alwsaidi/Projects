#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd 
import numpy as np 


# In[68]:


path = r'hour.csv'
data = pd.read_csv(path)


# 1- Look at the DataFrame shape

# In[69]:


data.shape


# 2- head 

# In[70]:


data.head()


# 3-tail

# In[71]:


data.tail()


# 4- describe

# In[72]:


data.describe()


# In[ ]:


5- mean


# In[73]:


data.mean()


# 6- median

# In[74]:


data.median()


# In[75]:


data.mode


# In[76]:


data.std()


# In[77]:


data.sum()


# In[78]:


data.count()


# In[79]:


data.isna().sum()


# 13- value_counts for all categorical columns
# 
# The data is all numerical 

# 14 - Subset your DataFrame based on oneconditions

# In[80]:


filtered_values = np.where((data['hr']==4))
print(filtered_values)
display(data.loc[filtered_values])


# 15- Subset your DataFrame based on two different conditions

# In[81]:


filtered_values = np.where((data['hr']==1) & (data['mnth']==8))
print(filtered_values)
display(data.loc[filtered_values])


# 16- Subset your DataFrame based on three different conditions

# In[82]:


filtered_values = np.where((data['hr']==1) & (data['mnth']<8) & (data['season']==3))                            
print(filtered_values)
display(data.loc[filtered_values])


# 17- Use loc to slice your DataFrame for the 2 columns that returned the largest sum

# In[123]:


sumValues = data.loc[:].sum()
sumValues


# In[91]:


maxValues = data[['registered', 'cnt']].sum()
 
print("Maximum value in column 'registered' & 'cnt': ")
print(maxValues)


# 18- Use iloc to slice your DataFrame for the 2 columns that returned the largest mean

# In[104]:


MeanTheValues = data.iloc[:].mean()
MeanTheValues


# In[105]:


MeanTheValues = data[['registered', 'cnt']].mean()
 
print("Maximum mean in column 'registered' & 'cnt': ")
print(maxValues)


# 19 - Find 2 pandas DataFrame methods we did not cover and use them on your own data. Explain what they do by writing a description in the markdown

# In[107]:


data.keys()


# In[110]:


data.min()


# In[ ]:




