import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[1,2,3],'B':[10,20,30]})
def plus_10(x):
    return x + 10
df['B_ap'] = df['B'].apply(plus_10)
df.apply(plus_10)
print(df.apply(plus_10))

#=============================

df = pd.DataFrame({'a':[0,1,""],'b':["",None,3]})
print("-------- The DataFrame--------------------")
print(df)
print("------------------------------------------")
print(df.isna())

#===============================

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack','Lee','David','Gasper','Bestina','Andress']),'Ages':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df = pd.DataFrame(d)
print(df.describe(include='all'))
print(df)