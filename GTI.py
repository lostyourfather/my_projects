import math
print(math.log(3))
r1 = float(input("Введите r1: "))
r2 = float(input("Введите r2: "))
r3 = float(input("Введите r3: "))
c1 = float(input("Введите c1: "))
f = 0
f = 1/((2*c1*r2)*math.log(1+((2*r1)/r3)))
print('f0: ', f)