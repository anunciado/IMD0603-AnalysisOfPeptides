
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as p
from pandas import Series, DataFrame
from IPython.display import display, HTML


# In[2]:


'''Ler o arquivo de entrada do banco de proteinas e salva em um .csv onde a primeira coluna
é os ID das Proteinas dos bancos de proteinas e a segunda coluna é as sequências propriamente
ditas.
'''
def readDatabase():
    database = dict()
    labelData = ''
    labelData2 = ''
    with open("../input/uniprot-human.fasta", 'r') as infile:
        sequenceData = '' 
        for line in infile:
            if(line[0]=='>'):
                labelData2 = line[1:].split('|')[1]
                if(sequenceData):
                    database[labelData] = sequenceData
                sequenceData = ''
                labelData = labelData2
            else:
                sequenceData += line.strip('\n')
    return database


# In[3]:


database = readDatabase()
print (database)


# In[4]:


sf = Series(database,index=database.keys())
df = pd.DataFrame({'Protein ID':sf.index, 'Sequence':sf.values})
display(df)


# In[5]:


df.to_csv("../result/processData.csv", sep='\t', index=False)

