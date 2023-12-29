#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install matplotlib


# In[2]:


#Bar Chart to compare COVID cases in various states in May-2020 and June-2020

import matplotlib.pyplot as plt


# In[3]:


# Data
states = ['Maharashtra', 'Rajasthan', 'Uttar Pradesh', 'Kerala', 'Panjab', 'Jharkhand', 'Haryana', 'Orisha']
may_cases = [28078, 17067, 12670, 19765, 18566, 5700, 3450, 2300]
june_cases = [39678, 13456, 19654, 10879, 12009, 9100, 8700, 7800]


# In[4]:


# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(states, may_cases, alpha=0.7, label='May-2020')
plt.bar(states, june_cases, alpha=0.7, label='June-2020')
plt.xlabel('States')
plt.ylabel('Number of Cases')
plt.title('Comparison of COVID Cases in May-2020 and June-2020')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# In[5]:


#2. Pie Chart to represent the share of states in positive cases in May-2020

# Data
may_cases = [28078, 17067, 12670, 19765, 18566, 5700, 3450, 2300]
states = ['Maharashtra', 'Rajasthan', 'Uttar Pradesh', 'Kerala', 'Panjab', 'Jharkhand', 'Haryana', 'Orisha']


# In[6]:


# Pie chart
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # Explode the state with the highest share
plt.figure(figsize=(8, 8))
plt.pie(may_cases, labels=states, explode=explode, autopct='%1.1f%%')
plt.title('Share of States in Positive Cases - May-2020')
plt.legend()
plt.show()


# In[7]:


#3. Line Chart to compare cases of all states in May-2020 and June-2020
# Data
months = ['May-2020', 'June-2020']
maharashtra = [28078, 39678]
rajasthan = [17067, 13456]
# ... Repeat the same for other states


# In[8]:


plt.figure(figsize=(10, 6))
for state_data in [maharashtra, rajasthan]:  # Add other states similarly
    plt.plot(months, state_data, marker='o')

plt.xlabel('Months')
plt.ylabel('Number of Cases')
plt.title('Comparison of COVID Cases in May-2020 and June-2020 for Different States')
plt.legend(states)  # Make sure states are in the same order as the data
plt.grid(True)
plt.tight_layout()
plt.show()


# In[9]:


#4. Subplot with Line, Pie, and Bar Charts for June-2020 cases

# Bar chart for June-2020 cases
plt.figure(figsize=(10, 8))


# In[11]:


# Subplot 1: Bar Chart
plt.subplot(2, 2, 1)
plt.bar(states, june_cases, alpha=0.7)
plt.xlabel('States')
plt.ylabel('Number of Cases')
plt.title('COVID Cases in June-2020')
plt.xticks(rotation=45)


# In[12]:


# Subplot 2: Line Chart
plt.subplot(2, 2, 2)
for state_data in [maharashtra, rajasthan]:  # Add other states similarly
    plt.plot(months, state_data, marker='o')
plt.xlabel('Months')
plt.ylabel('Number of Cases')
plt.title('Comparison of COVID Cases in June-2020 for Different States')
plt.legend(states)
plt.grid(True)


# In[13]:


# Subplot 3: Pie Chart
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)
plt.subplot(2, 2, 3)
plt.pie(june_cases, labels=states, explode=explode, autopct='%1.1f%%')
plt.title('Share of States in Positive Cases - June-2020')
plt.legend()

plt.tight_layout()
plt.show()


# In[15]:


#Pie Chart showing the share of cases of top 4 states and cases of all remaining states as 'Other'


# Data
top_states = ['Maharashtra', 'Rajasthan', 'Uttar Pradesh', 'Kerala']
top_cases = [39678, 13456, 19654, 10879]
other_cases = sum(june_cases) - sum(top_cases)


# In[16]:


# Pie chart
plt.figure(figsize=(8, 8))
cases = top_cases + [other_cases]
labels = top_states + ['Other']
plt.pie(cases, labels=labels, autopct='%1.1f%%')
plt.title('Share of Cases - Top 4 States vs Other States - June-2020')
plt.legend()
plt.show()


# In[ ]:




