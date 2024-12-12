import random as rd
a2=rd.randint(1,9)
a1=rd.randint(0,9)
b=rd.randint(0,9)
aa=a2*10+a1
s=a2*10+a1+b
c1=(a1+b)%10
c2=a2+((a1+b)//10)
print(aa)
print(b)
print(s)
print("Первая цифра ",c2)
print("Вторая цифра ",c1)