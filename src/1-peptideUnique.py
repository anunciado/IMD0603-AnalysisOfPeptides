
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as p
import multiprocessing
from pandas import Series, DataFrame
from itertools import repeat
from multiprocessing import Pool, freeze_support
import operator
from IPython.display import display, HTML


# In[2]:


'''Ler o arquivo de peptidios e o salva em uma dataframe, retira colunas não importantes para o problema 
'''
peptides = pd.read_csv("../input/T4evidence.txt", sep='\t')
peptides.drop('Length', axis=1, inplace=True)
peptides.drop('Modifications', axis=1, inplace=True) 
peptides.drop('Acetyl (Protein N-term)', axis=1, inplace=True)
peptides.drop('Oxidation (M)', axis=1, inplace=True)
peptides.drop('Missed cleavages', axis=1, inplace=True)
peptides.drop('Raw file', axis=1, inplace=True)
peptides.drop('Fraction', axis=1, inplace=True)
peptides.drop('Experiment', axis=1, inplace=True) 
peptides.drop('Charge', axis=1, inplace=True)
peptides.drop('m/z', axis=1, inplace=True)
peptides.drop('Mass', axis=1, inplace=True)
peptides.drop('Mass Error [ppm]', axis=1, inplace=True)
peptides.drop('Mass Error [Da]', axis=1, inplace=True)
peptides.drop('PEP', axis=1, inplace=True)
peptides.drop('Score', axis=1, inplace=True)
peptides.drop('Intensity', axis=1, inplace=True)
proteins = pd.read_csv("../result/processData.csv", sep='\t')


# In[3]:


display (peptides.head())


# In[4]:


print (peptides.shape)


# In[5]:


print (proteins.head())


# In[6]:


print (proteins.shape)


# In[7]:


'''Retira-se a redudância de peptidios no banco lido no programa e adciona-se uma coluna
chamada 'Frequency' onde será disposto sua frequência, logo após o dataframe será convertido
para dicionário para ser mais rápido a execução futura de paralelismo.
'''
peptides['Frequency'] = peptides.groupby('Sequence')['Sequence'].transform('count')
peptides = peptides.drop_duplicates('Sequence').reset_index(drop=True)
peptides = Series(peptides.Frequency.values,index=peptides.Sequence).to_dict()
#Só pegar os cinquenta primeiros peptidios da amostra passada
#peptidesTest = dict(sorted(peptides.items(), key=operator.itemgetter(1), reverse=False)[:50])
proteins = Series(proteins['Protein ID'].values,index=proteins.Sequence).to_dict()
proteins = list(proteins.items())


# In[8]:


'''Função que dado uma proteina e um peptidio, se o peptidio estiver contido na proteina, será retornado
uma lista com id da proteina, sua posição inicial e final.
'''
def findPeptide(protein, peptide):
    sequenceProtein, idp = protein
    if peptide in sequenceProtein:
        return idp


# In[9]:


'''Loop onde para cada peptidio será buscado em quantas proteinas está contido usando paralelismo.
'''
for peptide, frequency in peptides.items():
    with multiprocessing.Pool(processes=20) as pool:
        results = pool.starmap(findPeptide, zip(proteins, repeat(peptide)))
        for i in range(results.count(None)): results.remove(None)
        peptides[peptide] = results
        results = []


# In[10]:


'''Será transformado o dicionário em dataframe, onde as colunas são: a sequência do peptídio, a posição de ínicio 
desse peptídio na proteina que a contem, a posição do fim desse peptídio na proteina que a contem e sua frequência
no arquivo de origem
'''
df = pd.DataFrame(columns=['Peptide', 'Protein ID'])
for peptide, proteins in peptides.items():
    if len(proteins) == 1:
        for protein in proteins:
            df = df.append({'Peptide': peptide, 'Protein ID': protein}, ignore_index=True)
    


# In[11]:


display (df)


# In[12]:


df.to_csv("../result/peptideUnique.csv", sep='\t', index=False)

