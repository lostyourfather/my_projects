from math import sqrt
f = float(input())*1000
c1 = float(input())
c1 = c1*0.000000001
def koef(f,c1):
    k = 0
    k = f*c1*6.28
    return k
def res1(k):
    r1 = 0
    r1 = 2 / k
    return r1
def res2(k):
    r2 = 0
    r2 = 2 / (3*k)
    return r2
def res3(k):
    return 4/k
def con2(c1):
    return c1*0.5
f1 = 0
k = koef(f,c1)
r1 = res1(k)
r2 = res2(k)
r3 = res3(k)
c2 = con2(c1)
print('k: ', k)
print('r1: ', r1)
print('r2: ', r2)
print('r3 ', r3)
print('c2 ', c2)
f1 = (1/6.28)*(sqrt((r1+r2)/(r1*r2*r3*c1*c2)))
print('f1: ', f1)
f1Prob = 0
r1Prob = float(input('r1 табличное: '))
r2Prob = float(input('r2 табличное: '))
r3Prob = float(input('r3 табличное: '))
c1Prob = float(input('c1 табличное: '))
c2Prob = float(input('c2 табличное: '))
f1Prob = (1/6.28)*(sqrt((r1Prob+r2Prob)/(r1Prob*r2Prob*r3Prob*(c1Prob*0.000000001)*(c2Prob*0.000000001))))
print(f1Prob)