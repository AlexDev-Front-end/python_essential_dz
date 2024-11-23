""" 
Завдання 1

Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
"""

def generator_rev(list:list):
    for i in list[::-1]:
        yield i


list_num = [1, 2, 3, 4, 5]
for item in generator_rev(list_num):
    print(item)
    
    
""" 
Завдання 2

Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл
"""

def generator(list:list):
    for i in list:
        if i % 2 == 0:
            yield i**2

list_sq = [1, 2, 3, 4, 5]
res = list(generator(list_sq))
print(res)


squares = []
for x in list_sq:
    if x % 2 == 0:
        squares.append(x**2)

print(squares)


""" 
Завдання 3

Напишіть функцію-генератор для отримання n перших простих чисел.
"""

def generator(n:int):
    count = 0
    num = 2
    
    while count < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1

for prime in generator(5):
    print(prime)