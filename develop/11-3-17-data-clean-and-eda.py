
# coding: utf-8

# # 11-3-17 Data Clean and EDA

# import dependencies 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.style as style
#style.use('fivethirtyeight')
import seaborn as sb


# In[3]:


data = pd.read_csv("../data/KaggleV2-May-2016.csv")
data.head()


# correcting misspelled columns

# In[4]:


data.rename(columns = {'Hipertension':'Hypertension',
                       'PatientId': 'PatientID',
                       'Handcap': 'Handicap',
                       'No-show': 'NoShow',
                       'Alcoholism':'Alcoholism'
                         }, inplace = True)
data.head()


# Now trying to understand the data set. It's distributions and unique values. Also attempting to find funky and incorrect data points. I want to understand and check the integrity of the dataset

# In[5]:


data.PatientID.value_counts()


# making sure there arent duplicate appointment IDs

# In[6]:


data.AppointmentID.value_counts()


# In[7]:


data.Gender.unique()


# In[8]:


data.Gender.value_counts()


# trying to understand my timeline

# In[9]:


#UNCOMMENT FOR FINAL RUN THROUGH
#scheduledday = data.ScheduledDay.unique()
#for i in scheduledday:
    #print(i)


# In[10]:


data.AppointmentDay.unique()


# In[11]:


data.Age.value_counts()


# need to get rid of negative value. It is impossible for someone to be -1.  

# In[12]:


data['Age'][data['Age'] < 0] = 1


# In[13]:


data.Age.value_counts()


# In[14]:


data.Scholarship.value_counts()


# In[15]:


data.Hypertension.value_counts()


# In[16]:


data.Diabetes.value_counts()


# In[17]:


data.Handicap.value_counts()


# In[18]:


data.SMS_received.value_counts()


# In[19]:


data.NoShow.value_counts()


# making sure there aren't any values missing in the dataset

# In[20]:


data.isnull().sum()


# In[21]:


print('Age:',sorted(data.Age.unique()))
print('Gender:',data.Gender.unique())
#print('DayOfTheWeek:',data.DayOfTheWeek.unique())
#print('Status:',data.Status.unique())
print('Diabetes:',data.Diabetes.unique())
print('Alchoholism:',data.Alcoholism.unique())
print('Hypertension:',data.Hypertension.unique())
print('Handicap:',data.Handicap.unique())
#print('Smokes:',data.Smokes.unique())
print('Scholarship:',data.Scholarship.unique())
#print('Tuberculosis:',data.Tuberculosis.unique())
print('SMS_received:',data.SMS_received.unique())
#print('AwaitingTime:',sorted(data.AwaitingTime.unique()))
#print('HourOfTheDay:', sorted(data.HourOfTheDay.unique()))


# In[22]:


data.head()


# In[24]:


data.to_csv("../data/post-cleanandeda.csv")

