
# coding: utf-8

# # 11-7-17 Feature Selection and Creation

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.style as style
#style.use('fivethirtyeight')
import seaborn as sb


# In[2]:


data = pd.read_csv("../data/post-cleanandeda.csv")
data.head()


# In[3]:


data.drop(data.columns[[0]], axis=1)
data.head()


# Creating two binary columns for the gender

# In[4]:


data['Male'] = data['Gender'].replace(['F','M'], [0,1])
data['Female'] = data['Gender'].replace(['F','M'], [1,0])
data.head()


# changing NoShow column to be binary

# In[5]:


data['NoShow'] = data['NoShow'].replace(['Yes','No'], [1,0])
data.head()


# dropping uneeded columns

# In[6]:


data = data[['PatientID','ScheduledDay','AppointmentDay', 'Age','Neighbourhood', 'Scholarship','Hypertension','Diabetes','Alcoholism','Handicap','SMS_received','NoShow','Male','Female']]
data.head()


# cleaning up dates

# In[7]:


data['ScheduledDay'] = pd.to_datetime(data['ScheduledDay'])
data['AppointmentDay'] = pd.to_datetime(data['AppointmentDay'])
data.head()


# In[8]:


data['ScheduledYear'], data['ScheduledMonth'], data['ScheduleDay'] = data['ScheduledDay'].dt.year, data['ScheduledDay'].dt.month, data['ScheduledDay'].dt.day
data['AppointmentYear'], data['AppointmentMonth'], data['AppointmentDayy'] = data['AppointmentDay'].dt.year, data['AppointmentDay'].dt.month, data['AppointmentDay'].dt.day
data.head()


# Probably have to get rid of Neighbourhood column given we don't have the specefic hospital for all these NoShows. If we did we could have used distance from hospital as a feature. 
creating a feature that calculates the wait time of a particular patient from when they schedule the appointment to when they actually have the appointment. I believe this will be a really great feature to have. One would assume that the longer the wait time the more likely people are to no show for their appointments
# In[12]:


data['WaitingTime'] = data['AppointmentDay'] - data['ScheduledDay']
data.head()


# Need to make one last clean dataset picking which features I will actually use in the model. 

# In[17]:


data = data[['NoShow','ScheduledDay','AppointmentDay','Age','Scholarship','Hypertension','Diabetes','Alcoholism','Handicap','SMS_received','Male','Female','ScheduledYear','ScheduleDay','AppointmentYear','AppointmentMonth','AppointmentDayy','WaitingTime']]
data.head()

exporting the data set with the correct features for the model. 
# In[19]:


data.to_csv("../data/post-featureselectionandcreation.csv")

