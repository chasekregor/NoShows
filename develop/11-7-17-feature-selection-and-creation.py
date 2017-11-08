
# coding: utf-8

# # 11-7-17 Feature Selection and Creation

# In[122]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.style as style
#style.use('fivethirtyeight')
import seaborn as sb


# In[123]:


data = pd.read_csv("../data/post-cleanandeda.csv")
data.head()


# In[124]:


data.drop(data.columns[[0]], axis=1)
data.head()


# Creating two binary columns for the gender

# In[125]:


data['Male'] = data['Gender'].replace(['F','M'], [0,1])
data['Female'] = data['Gender'].replace(['F','M'], [1,0])
data.head()


# changing NoShow column to be binary

# In[126]:


data['NoShow'] = data['NoShow'].replace(['Yes','No'], [1,0])
data.head()


# dropping uneeded columns

# In[127]:


data = data[['PatientID','ScheduledDay','AppointmentDay', 'Age','Neighbourhood', 'Scholarship','Hypertension','Diabetes','Alcoholism','Handicap','SMS_received','NoShow','Male','Female']]
data.head()


# cleaning up dates

# In[128]:


data['ScheduledDay'] = pd.to_datetime(data['ScheduledDay'])
data['AppointmentDay'] = pd.to_datetime(data['AppointmentDay'])
data.head()


# In[129]:


data['ScheduledYear'], data['ScheduledMonth'], data['ScheduleDay'] = data['ScheduledDay'].dt.year, data['ScheduledDay'].dt.month, data['ScheduledDay'].dt.day
data['AppointmentYear'], data['AppointmentMonth'], data['AppointmentDayy'] = data['AppointmentDay'].dt.year, data['AppointmentDay'].dt.month, data['AppointmentDay'].dt.day
data.head()


# Probably have to get rid of Neighbourhood column given we don't have the specefic hospital for all these NoShows. If we did we could have used distance from hospital as a feature. 
