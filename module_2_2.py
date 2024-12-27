n = int(input('Введите число первой вставки от 3 до 20: '))
if n > 21 or n < 3:
    n = int(input('"Вы ввели не верное число. Введите число от 3 до 20: '))
result = str('')
i = 1
while i < 20:
    j = i + 1
    while j < 20:
        if i != j and i != n and j != n:
            if n % (i + j) == 0:
                result = result + str(i) + str(j)
        j = j +1
    i = i + 1
print("Нужный пароль :", result)
