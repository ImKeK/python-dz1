# Задача 2: Найдите сумму цифр трехзначного числа.

# print("Введите трёхзначное число")
# n = int(input())
#
# i = n % 100
#
# a = n // 100
# b = i // 10
# c = i % 10
# sum = a + b + c
# print(sum)

# ЗАДАЧА 4:

# S = int(input("Введите общее количество журавликов: "))
#
# if S // 6:
#      x = S // 6
#      print(f'Катя: {(x+x)*2 } ')
#      print(f'Сережа: {x} ')
#      print(f'Петя: {x}')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# a = int(input("Введите шестизначный билет"))
# b = a // 1000
# one = b // 100
# two = b % 11
# three = b % 10
# c = a % 1000
# four = c // 100
# five = c % 11
# six = c % 10
#
# if (one+two+three) == (four+five+six):
#     print('Счастливый')
# else:
#     print('Обычный')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input('В 1-ю сторону: '))
m = int(input('Во 2-ю сторону: '))
k = int(input('кол-во долек: '))
if k%n == 0 or k%m == 0:
    print('Yes')
else:
    print('No')