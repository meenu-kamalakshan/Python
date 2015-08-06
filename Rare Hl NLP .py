
# coding: utf-8

# In[182]:

import pyodbc
import numpy
import pandas
import sqlite3
import nltk


# In[183]:

data = pandas.read_csv("/Users/mkamalakshan/Desktop/Apryl/Facebook.csv",header=0, delimiter=",",encoding='latin-1')


# In[184]:

list(data)


# In[185]:

data = data [['Post','Link Clicks','Time']]


# In[186]:

data.head()


# In[191]:

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

#input_list = ['all', 'this', 'happened', 'more', 'or', 'less']
#print (list(find_ngrams(input_list, 1)))
#print (list(find_ngrams(input_list, 2)))
#print (list(find_ngrams(input_list, 3)))
#print (list(find_ngrams(input_list, 4)))


# In[192]:

data.shape[0]


# In[193]:

import re


# In[203]:

posted1 =[]
posted2 =[]
posted3 =[]
posted4 =[]

for i in range (0,data.shape[0]):
    post=((data['Post'][i]).lower())
    post = post.replace('...','')
    post = post.replace('_','')
    post = re.sub(';','',post)
    post = re.sub(',','',post)
    post = re.sub('\d','X',post)
    post = re.sub('--','',post)
    post = post.split()
    posted1.append(list(find_ngrams(post, 1)))
    posted2.append(list(find_ngrams(post, 2)))
    posted3.append(list(find_ngrams(post, 3)))
    posted4.append(list(find_ngrams(post, 4)))

    
print(posted1[0])
print(posted2[0])
print(posted3[0])
posted4[0]


# In[220]:

df1 = pandas.DataFrame(posted1)
df2 = pandas.DataFrame(posted2)
df3 = pandas.DataFrame(posted3)
df4 = pandas.DataFrame(posted4)


# In[221]:

newdata1=data.join(df1)
newdata2=data.join(df2)
newdata3=data.join(df3)
newdata4=data.join(df4)


# In[238]:

ndata1= pandas.melt(newdata1, id_vars = ['Post', 'Link Clicks','Time'])
ndata2= pandas.melt(newdata2, id_vars = ['Post', 'Link Clicks','Time'])
ndata3= pandas.melt(newdata3, id_vars = ['Post', 'Link Clicks','Time'])
ndata4= pandas.melt(newdata4, id_vars = ['Post', 'Link Clicks','Time'])


# In[239]:

print(ndata1.shape)
print(ndata2.shape)
print(ndata3.shape)
print(ndata4.shape)


# In[240]:

ndata1 = ndata1[ndata1['value'].notnull()]
ndata2 = ndata2[ndata2['value'].notnull()]
ndata3 = ndata3[ndata3['value'].notnull()]
ndata4 = ndata4[ndata4['value'].notnull()]


# In[241]:

print(ndata1.shape)
print(ndata2.shape)
print(ndata3.shape)
print(ndata4.shape)


# In[251]:

ndata1['variable'] = 'unigram'
ndata1.head()


# In[257]:

ndata2['variable'] = 'bigram'
ndata2.head()


# In[258]:

ndata3['variable'] = 'trigram'
ndata3.head()


# In[259]:

ndata4['variable']= 'fourgram'
ndata4.head()


# In[263]:

ndata = pandas.concat([ndata1,ndata2],axis=0,ignore_index=True)
ndata = pandas.concat([ndata,ndata3],axis=0,ignore_index=True)
ndata = pandas.concat([ndata,ndata4],axis=0,ignore_index=True)


# In[264]:

ndata.shape


# In[266]:

ndata.to_csv("/Users/mkamalakshan/Desktop/Apryl/output.csv", sep='\t', encoding='utf-8')


# In[ ]:



