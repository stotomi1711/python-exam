strText = input("아무 문장이나 입력하세요 : ")
print(strText)
flVal = [1.0, 2.0, 3.14, 4.2, 5.1]  
arVal = [flVal, flVal, flVal]
arVal
arVal[0]
arVal[1]
arVal[1][2]
arVal[0] = 'python'
arVal
arVal[0][2]
arVal[0] = 'python programming'
arVal

import numpy as np
arData = np.array([1.0, 2.0, 3.14, 4.2, 5.1])
arData
arData.sum()
arVal.sum()
print(type(arVal))
print(type(arData))
arData.std()
arData.cumsum()
arData * 2
arData ** 2
np.sqrt(arData)
arVal = np.array([arData, arData ** 2])
arVal
arVal.sum(axis=0)
arVal.sum(axis=1)
np.array([[0,0,0],[0,0,0]])
arZero = np.zeros((2,3), dtype = 'i') 
arZero


import pandas as pd
pandas_series = pd.Series([30, 20, 10], index=['국어', '영어', '수학'])
print(type(pandas_series))
pandas_series
pandas_series[1:]
pandas_series[0]
pandas_series[0][1]

df = pd.DataFrame([30,20,10], columns=['score'], index=['국어', '영어', '수학'])
df
df.index
df.columns
df.loc['국어'] 
df.sum()
df.score ** 2
df['score2'] = (50, 50, 50)
df
df['score2'] = pd.DataFrame([90,90,90], index=['국어', '영어', '수학'])
df
del df['score']
df['score2'] = (90, 90, 90, 100)
df['score2'] = pd.DataFrame([90, 90, 90, 100], index=['국어', '영어', '수학', '윤리'])
df
df1 = pd.DataFrame([1, 2, 3], columns = ['A'])
df2 = pd.DataFrame([10, 11, 12, 13], columns = ['B'])
df = df1.join(df2, how='outer')
df
df_inner = df1.join(df2, how='inner')
df_inner
df = pd.DataFrame(np.random.randn(5,5))
df.columns = ['A', 'B', 'C', 'D', 'E']
df
df.max()
df.min()    
df.mean()
df.std()
df.cumsum()
df.describe()
df['division'] = ['X', 'Y', 'X', 'Y', 'Z']
df
df.groupby(['division']).mean()