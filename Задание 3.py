import random as rd
a3=rd.randint(1,9)
a2=rd.randint(0,9)
a1=rd.randint(0,9)
b2=rd.randint(1,9)
b1=rd.randint(0,9)
e=(a1+b1)%10
d=(a2+b2)+((a1+b1)//10)
s=a3+((a2+b2)//10)
c1=e
c2=d%10
c3=s%10
print(f"Цифры результата: {c3}{c2}{c1}")