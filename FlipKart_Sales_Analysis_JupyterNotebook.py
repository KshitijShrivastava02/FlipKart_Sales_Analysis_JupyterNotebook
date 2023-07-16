#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[5]:


df = pd.read_csv(r'C:\Users\91982\Desktop\Data Analysis Poject\FlipKart_sales_Analysis\Diwali Sales Data.csv.csv', encoding = 'unicode_escape') 


# In[6]:


df.shape


# In[7]:


df.head()
#This will give the 5 rows by defalut , and if some value
#is passed then it will give that much rows


# In[8]:


df.info()


# In[9]:


#Now Start DATA CLEANING PROCESS
#First ye 2 blank column delete ker rha 
df.drop(['Status' , 'unnamed1'], axis=1, inplace = True)


# In[10]:


df.info()


# In[11]:


pd.isnull(df).sum()
#ye apne ko bta rha ki in colums me sare non null values he
#but Amount me 12 null values he 


# In[12]:


#so avi ROWS kitne he 
df.shape


# In[13]:


df.dropna(inplace = True)
#ye esse humne direct NULL values jisme vo Row hi delete kr di


# In[14]:


df.shape


# In[16]:


df.shape


# In[17]:


df.info()


# In[18]:


#Now Amount ka data type change krna he so 
df['Amount'] = df['Amount'].astype('int')


# In[19]:


df.info()


# In[20]:


df['Amount'].dtypes


# In[22]:


df.columns


# In[26]:


#Now if we have to change the column name so we use this function
df.rename(columns={'Marital_Status': 'Status_Of_Marriage'},inplace=True)
#ye inplace = True likhna pdega tab hi save hoga nhe to nhe 


# In[27]:


df.shape


# In[28]:


df.columns


# In[30]:


df.describe()
# ye sare numeric columns ki mean meadian bgera de deta  


# In[31]:


df[['Age', 'Orders', 'Amount']].describe()
#Ye perticular columns ka mean median bgera de dedega


# In[32]:


df.columns


# In[33]:


ax=sns.countplot(x='Gender', data=df)


# In[36]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount' , ascending=False)


# In[37]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount' , ascending=False)
sns.barplot(x='Gender' ,y='Amount' , data=sales_gen)


# In[39]:


df.columns


# In[40]:


#AGE


# In[41]:


ax=sns.countplot(data=df,x='Age Group', hue='Gender')


# In[42]:


ax=sns.countplot(data=df,x='Age Group', hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[43]:


#SO FROM GRAPH HUMKO PTA CHALA KI MOST BUYERS 26-35 AGE KE HAI 


# In[44]:


sales_gen=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount' , ascending=False)
sns.barplot(x='Age Group' ,y='Amount' , data=sales_gen)


# In[45]:


#STATE Analysis


# In[46]:


df.columns


# In[47]:


#Total Number of Orders from top 10 states


# In[61]:


sales_state = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders' , ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,4)})
sns.barplot(data= sales_state, x='State' ,y='Orders')


# In[58]:


df.columns


# In[64]:


sales_state = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount' , ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,4)})
sns.barplot(data= sales_state, x='State' ,y='Amount')


# In[77]:


ax=sns.countplot(data=df,x='Status_Of_Marriage')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[78]:


#NOW OCCUPATION ANALYSIS


# In[81]:


ax=sns.countplot(data=df,x='Occupation')

sns.set(rc={'figure.figsize':(20,10)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[84]:


df.columns


# In[83]:


ax=sns.countplot(data=df,x='Product_Category')

sns.set(rc={'figure.figsize':(20,10)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[85]:


#The Above is PRODUCT CATEGORY ANALYSIS


# In[86]:


sales_Products = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_Products, x = 'Product_ID',y= 'Orders')


# In[89]:


#The Above one is Produt_ID which is sold most


# In[ ]:


#                                   CONCLUSION 


#Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, 
#Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

