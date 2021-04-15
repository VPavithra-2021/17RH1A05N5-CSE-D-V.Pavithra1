#!/usr/bin/env python
# coding: utf-8

# In[36]:


#1.fill null values of a  data frame using median and mode
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
df = pd.DataFrame({
'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
'purch_amt':[150.5,np.nan,65.26,110.5,948.5,np.nan,5760,1983.43,np.nan,250.45, 75.29,3045.6],
'sale_amt':[10.5,20.65,np.nan,11.5,98.5,np.nan,57,19.43,np.nan,25.45, 75.29,35.6]})
print(df)


# In[40]:


df['purch_amt'].fillna(df['purch_amt'].median(), inplace=True)
print(df)


# In[20]:


#2.what is the difference between merging and joining in dataframe

Both join and merge can be used to combines two dataframes but the join method combines two dataframes on the basis of their indexes whereas the merge method is more versatile and allows us to specify columns beside the index to join on for both dataframes.
Merge:=
    The pd. merge() function recognizes that each DataFrame has an "employee" column, and automatically joins using this column as a key. The result of the merge is a new DataFrame that combines the information from the two inputs.
Join:=
    Join columns with other DataFrame either on index or on a key column. Efficiently join multiple DataFrame objects by index at once by passing a list.


# In[29]:


#3.create a numpy array and a dataframe and concatenate them
array = np.arange(9)
array
array1 = array.reshape((3,3))
array1

 


# In[30]:


array2 = np.arange(10,19).reshape(3,3)
array2


# In[31]:


np.concatenate((array1, array2))


# In[55]:


#4.create a data frame and add a column. add names in it and use apply function to return names whose length is greater than 5 
data = {
     'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
              'Manchester', 'Cairo', 'Osaka'],

}
row_labels = [101, 102, 103, 104, 105, 106, 107]


# In[56]:


data


# In[57]:


df = pd.DataFrame(data=data, index=row_labels)
df


# In[58]:


df.city


# In[59]:


df['Length']=df['city'].str.len()
print(df)


# In[60]:


df[df["Length"]>5]

