import pandas as pd
import csv

df = pd.read_csv("dwarf_stars.csv")
print(df.head())

df = df[df['Distance'].notna()]

df = df[df['Mass'].notna()]

df = df[df['Radius'].notna()]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"]
df["Radius"] = 0.102763*df["Radius"]

print(df.dtypes)


df.columns
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.head()
df.columns

df.reset_index(drop=True,inplace=True)

df.to_csv('stars_converted.csv')


