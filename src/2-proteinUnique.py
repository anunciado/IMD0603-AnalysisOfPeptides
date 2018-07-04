
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display, HTML


# In[2]:


df = pd.read_csv("../result/intersectEvidence.csv", sep='\t')
display (df)


# In[3]:


'''Será buscado as proteinas únicas do dado inserido e será salva em um arquivo
'''
df = df['Protein ID'].unique()


# In[4]:


print (df)


# In[5]:


np.savetxt('../result/proteinsUnique.txt', df, header='Proteins', fmt="%s")


# In[6]:


print (len(df))

