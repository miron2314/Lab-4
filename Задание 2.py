import random as rd
a2=rd.randint(1,9)
a1=rd.randint(0,9)
b2=rd.randint(1,9)
b1=rd.randint(0,9)
c1 = (a1 + b1) % 10
c2 = (a2 + b2) + 1
print(f"Цифры результата: {c2}{c1}")