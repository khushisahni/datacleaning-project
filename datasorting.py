import csv
import pandas as pd
import numpy as np
df = pd.read_csv('dwarf_stars.csv')

df.dropna()
df['Mass'][351]= np.nan
df['Radius'] = 0.102763*df['Radius']
df['Mass'] = df['Mass'].apply(lambda x:str(x).replace('$', '').replace(',', ',')).astype('float')
df['Mass'] = 0.000954588*df['Mass']

df.head()
df.columns
df.drop(['Unnamed: 0'],axis = 1, inplace=True)

df.head()
df.reset_index(drop=True, inplace=True)

df.to_csv('unit_converted_stars.csv')