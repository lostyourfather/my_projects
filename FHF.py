from math import sqrt
f = float(input())*1000
c2 = float(input())
c2 = c2*0.000000001
def koef(f,c2):
    k = 0
    k = f*c2*6.28
    return k
def res1(k):
    r1 = 0
    r1 = 2 / (3*k)
    return r1
def res2(k):
    r3 = 0
    r3 = 2 / (sqrt(2)*k)
    return r3

f1 = 0
k = koef(f,c2)
r1 = res1(k)
r3 = res2(k)
print('k: ', k)
print('r1: ', r1)
print('r3: ', r3)
f1 = 1/(6.28*sqrt(c2*c2*r1*r3))
print('f1: ', f1)
f1Prob = 0
r1Prob = float(input('r1 табличное: '))
r3Prob = float(input('r3 табличное: '))
c1Prob = float(input('c1 табличное: '))
c2Prob = float(input('c2: '))
f1Prob = 1/(6.28*sqrt(r1Prob*r3Prob*(c1Prob *0.000000001)*(c2Prob*0.000000001)))
print(f1Prob)