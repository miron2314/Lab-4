def find_info(k):
    if (1 <= k <= 180):
        a = (k + 1) // 2
        b = a + 9
        if k % 2 == 0:
            c = b % 10
        else:
            c= b // 10

    return a, b, c
k = int(input("Введите значение k: "))
a, b, c = find_info(k)
print(f"Номер пары цифр: {a}")
print(f"Двузначное число: {b}")
print(f"k-я цифра: {c}")
