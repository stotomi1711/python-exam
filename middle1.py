strVal = 'data science'
nVal = 12345
fVal = 1.2
lVal =  ['data', 'science']
dVal = {'lecture' : 'data science'}
bVal = True
strVal
nVal
fVal
lVal
dVal
bVal
print('strVal : ', strVal)
print('nVal : ', nVal)
print('fVal : ', fVal)
print('lVal : ', lVal)
print('dVal : ', dVal)
print('bVal : ', bVal)
print('strVal : ', type(strVal))
print('nVal : ', type(nVal))
print('fVal : ', type(fVal))
print('lVal : ', type(lVal))
print('dVal : ', type(dVal))
print('bVal : ', type(bVal))

nVal = 16
fVal = 3.14
print('10진수 표현 : ', nVal)
print('2진수 표현 : ', bin(nVal))
print('8진수 표현 : ', oct(nVal))
print('16진수 표현 : ', hex(nVal))
btVal = True
bfVal = False
btVal = TRUE
bfVal = FALSE
btVal = true
bfVal = False

10 == 11
10 != 11
10 >= 11
10 <= 11
10 > 11
10 < 11
nBig = 100
nSmall = 10
print(nBig == nSmall)
print(nBig != nSmall)
print(nBig >= nSmall)
print(nBig <= nSmall)
print(nBig > nSmall)
print(nBig < nSmall)
print(nBig =< nSmall)
print(nBig => nSmall)

strData = 'data'               
strSci = "Science"   
strLecture = strData + strSci
strLecture
strLecture = strData +" "+ strSci
strLecture
strLecture.split()
lSeperate = strLecture.split()
type(lSeperate)

strHello = "안녕하세요. 반갑습니다."
strHello.find("반갑") 
strHello.find("hello")  
"반갑" in strHello 
strHello.replace('.', '?')
strHello.replace('.', '?')                  
strHello.replace("하세요", "하셔유")
strHello  
strNewHello = strHello.replace('.', '?')                      
strNewHello = strNewHello.replace("하세요", "하셔유")     
strNewHello
strHello.strip('반갑습니다.')
strHello 


lnData = [1,2,3,4,5]    
print(lnData)
print('type : ', type(lnData))
print(lnData[0])   
print(lnData[3])
lnData[0] = lnData[4]  
print(lnData)  
print(lnData[2:4]) 
lnData = [1,2,3,4,5]
lstrData=['a', 'b', 'c']
lnData + lstrData
lnData.append(10)   
lnData
lnData.insert(0, 'python')  
lnData
lnData.remove('python')     
lnData
del lnData[5]             
lnData
lnData
lnData.pop(0)     
lnData
lnData.pop()   
lnData
lnData.clear() 
lnData

tVal = ("사과", "딸기", "바나나", "토마토", "키위")

print(tVal)
print(type(tVal))
tVal[0] = "포도"
tData = ( 1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 7)
tData.count(1)
len(tVal)
len(tData)
print(tData[2:5])
tTuple = tVal+ tData
print(tTuple)
tData * 2
tData
tData2 = tData * 2
print(tData2)
print("tVal memory = ", hex(id(tVal)))
tVal = tVal * 2
print("tVal memory = ", hex(id(tVal)))
print(tVal)
print("tVal memory = ", hex(id(tVal)))
tVal = tVal + tVal
print("tVal memory = ", hex(id(tVal)))
print(tVal)

sVal = {1, 2, 3, 4, 5}
print(sVal)
print(type(sVal))
sVal[1:2]
sVal.add(100)
print(sVal)
sVal.update([200, 300])
print(sVal)
sVal.remove(200)
print(sVal)
sVal.clear()
print(sVal)
sVal = {100, 200, 300, 400, 500}
sData = {"a", "b", "c", "c", 100, 300}
print(sVal)
print(sData)
sVal.intersection(sData)
sVal.difference(sData)
sVal - sData
sVal.union(sData)
sVal + sData
sVal.symmetric_difference(sData)

dVal = {
    'name' : '이컴공',
    'email' : 'computer@hoseo.edu',
    'address' : '충남 아산시'
}
print(dVal)
print(type(dVal))
dData = {
    "사과" : 300, 
    "포도" : 200, 
    "배" : 500,
    "키위" : 100
}
print(dData["배"])
dData.get("배")
dData["딸기"] = 100
print(dData)
dData.pop("사과")
dData
dData.pop()
sorted(dData)
sorted(dData.values())
dData

def f(x):
  return x + 10
f(2)