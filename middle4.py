!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

plt.rc('font', family='NanumBarunGothic')
plt.rc('axes', unicode_minus = False)
x = ['1월', '2월', '3월', '4월', '5월']
y = [7, 10, 17, 20, 23]
plt.plot(x,y)
plt.show()

x = ['1월', '2월', '3월', '4월', '5월']
y = [7, 10, 17, 20, 23]
plt.plot(x,y, color="blue", marker = 'o', linestyle = ':')
plt.title('월별 평균 온도', fontsize=15)
plt.ylabel('온도(도)')
plt.grid(linestyle = ':')
plt.show()

aVal = np.random.standard_normal(40)
aVal
type(aVal)
index = range(len(aVal))
plt.plot(index, aVal)
plt.xlim(0, 20)
plt.ylim(np.min(aVal) -1, np.max(aVal) + 1)
plt.show()
type(index)
plt.figure(figsize=(7,4))
plt.plot(aVal.cumsum(), 'b', lw= 1.5)
plt.plot(aVal.cumsum(), 'ro')
plt.xlabel('index')
plt.ylabel('aVal')
plt.title('Line Plot')
plt.show()
value = np.random.standard_normal((30, 2))
value
value[0]
plt.figure(figsize=(10,4))
plt.plot(value[:,0], lw= 1.5)
plt.plot(value[:,1], lw= 1.5)
plt.plot(value, 'ro')
plt.grid(True)

plt.xlabel('index')
plt.ylabel('value')
plt.title('Line Plot')

plt.figure(figsize=(10,5))
plt.subplot(211)
plt.plot(value[:,0], lw = 1.5, label = '1st')
plt.plot(value[:,0], 'ro')
plt.grid(True)
plt.legend(loc = 0)
plt.ylabel("value")
plt.title('Line Plot 3')

plt.subplot(212)
plt.plot(value[:,1], 'g', lw = 1.5, label = '2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

plt.figure(figsize=(13,5))
plt.subplot(231)
plt.plot(value[:,0], lw= 1.5, label = '1st')
plt.plot(value[:,0], 'co')
plt.grid(True)
plt.legend(loc=0)
plt.ylabel('value')
plt.title('Line Plot 3')

plt.subplot(232)
plt.plot(value[:,0], 'g-.', lw=1.5, label='1st')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

plt.subplot(233)
plt.plot(value[:,0], 'g', lw=1.5, label='1st')
plt.plot(value[:,0], 'bD')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

plt.subplot(234)
plt.plot(value[:,1], '*', lw=1.5, label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

plt.subplot(235)
plt.plot(value[:,1], 'b', lw=1.5, label='2nd')
plt.plot(value[:,1], 'ms')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

plt.subplot(236)
plt.plot(value[:,1], 'r--', lw=1.5, label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

x = ['1월', '2월', '3월', '4월', '5월']
y = [7, 10, 17, 20, 23]

plt.bar(x,y)
plt.show()

x = ['1월', '2월', '3월', '4월', '5월']
y = [7, 10, 17, 20, 23]

plt.barh(x,y)
plt.show()

x = ['1월', '2월', '3월', '4월', '5월']
y = [7, 10, 17, 20, 23]

plt.bar(x,y, color="orange", width = 0.5, edgecolor = 'black', hatch = '/')
plt.title('월별 평균 온도', fontsize=15)
plt.ylabel('온도(도)')
plt.grid(linestyle = ':', axis = 'y')
plt.show()

import pandas as pd

df = pd.read_csv('scores.csv', encoding='cp949')
df
x = df['이름']
y_kor = df['국어']

plt.bar(x, y_kor)
plt.show()

x = df['이름']
y_kor = df['국어']
y_eng = df['영어']

plt.bar(x, y_kor, width = -0.4, align = 'edge', label = '국어')
plt.bar(x, y_eng, width = 0.4, align = 'edge', label = '영어')
plt.title('국어/영어 점수 비교', fontsize = 15)
plt.ylabel('점수')

plt.legend() 
plt.show()


value = np.random.standard_normal((500,2))
plt.plot(value[:,0], value[:,1], 'ro')
plt.grid(False)
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 1')
plt.figure(figsize=(7,5))
plt.scatter(value[:,0], value[:,1], marker='o')
plt.grid(True)
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 2')

color = np.random.randint(0,10,len(value))

plt.figure(figsize=(10,5))
plt.scatter(value[:,0], value[:,1], c=color, marker = 'o')
plt.colorbar()
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 3')

import seaborn as sns
df = sns.load_dataset('tips')
df
df.head()
df.describe()
df.info()
x = df['total_bill']
y = df['tip']
sns.scatterplot(x,y)
sns.boxplot(x="day", y = "tip", hue="sex", data=df, palette="muted")