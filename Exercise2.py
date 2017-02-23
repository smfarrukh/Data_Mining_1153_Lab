
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np


# In[3]:

euro12 = pd.read_csv("C:/Users/Farrukh/Desktop/Euro2012statsTEAM.csv")


# In[7]:

euro12["Goals"]


# In[9]:

euro12.shape[0]


# In[10]:

euro12.shape[1]


# In[15]:

discipline = euro12[["Team", "Yellow Cards", "Red Cards"]]


# In[20]:

discipline.sort_values(["Red Cards", "Yellow Cards"], ascending=False)


# In[22]:

discipline["Yellow Cards"].mean()


# In[28]:

euro12[euro12["Goals"]>6]


# In[32]:

euro12[euro12["Team"].str[:1]=='G']


# In[33]:

euro12.iloc[:,0:7]


# In[36]:

euro12.iloc[:,:-3]


# In[48]:

euro12["Shooting Accuracy"][euro12["Team"].isin(["England","Italy", "Russia"])]


# In[ ]:



