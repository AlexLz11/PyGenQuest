# Task 1.1.3
# nums = sorted(map(int, input().split()))
# cd = nums.pop()
# ab = nums.pop(0) * nums.pop(0)
# nums.remove(ab)
# c = nums.pop(0)
# d = list(filter(lambda x: x * c == cd, nums))[0]
# print(d)

# Task 1.1.4
# a, b = int(input()), int(input())
# nums = b - a + 1
# pairs = nums // 2
# diff = [-1, 1][a % 2] * pairs + [1, -1][b % 2] * (nums % 2) * b
# print(diff)

# Task 1.1.6
# code = ['X', 'X', 'X', 'X', 'X']
# n = 179
# i = 0
# print(n)
# n -= 1
# while n > 0:
#     sn = n % 3
#     code[i] = ['X', 'Y', 'Z'][sn]
#     i += 1
#     n //= 3
# print(''.join(code[::-1]))

# Task 1.1.7
# dc = {'0': 1229, '1': 2338, '2': 2240, '3': 2240, '4': 1438, '5': 1240, '6': 1240, '7': 1240, '8': 1239, '9': 1237}
# count = 0
# while sum(dc.values()) > 0:
#     count += 1
#     for i in str(count):
#         dc[i] -= 1
# print(count)

# Task 1.1.9
# Для отрезка от a до b включительно формула:(a + b) * (b - a + 1) // 2
# Work solution!!!!
# n = int(input())
# i = (n - 1) * n // 2
# j = (2 * n - 1) * n
# result = n * (j + 2 * i)
# print(result)

# Task 1.1.10

# РЕШЕНИЕ № 1. Рабочее, но работает медленно
# import time

# s = int(input())
# tb = time.time()
# num = [0] * 12
# if s < 10:
#     brd = s
#     num[0] = brd
# else:
#     brd = 9
#     n = '9' * (s // brd) + str(s % brd)
#     num[:len(n)] = [int(i) for i in n]
# count = 1
# while True:
#     for i in range(1, 12):
#         if num[i] < brd and any(num[:i]):
#             num[i] += 1
#             num[:i] = sorted(num[:i], reverse=True)
#             for i in range(i - 1, -1, -1):
#                 if num[i] > 0:
#                     num[i] -= 1
#                     break
#             count += 1
#             break
#     else:
#         break
# te = time.time()
# print(count)
# print(te - tb)

# ************************************************************************************
# ТЕОРИЯ ИЗ КОМБИНАТОРИКИ:
# Формула сочетаний гласит: C(n + k — 1, k — 1), где n — сумма цифр, k — количество слагаемых.
# Например, мы хотим найти количество трехзначных чисел с суммой цифр, равной 10
# C(a, b) = a! / (b! * (a - b)!), где a = n + k - 1; b = k - 1
# В нашем примере количество чисел будет равно C(10 + 3 — 1, 3 — 1) = C(12, 2) = 66.
# 
# from math import factorial as fact
# s = int(input()) # например n (у нас это s) = 10, при k = 3, результат должен быть 66
# k = 12
# qt = fact(s + k - 1) / (fact(k - 1) * fact(s))
# print(qt)
#
# ************************************************************************************
#
# РЕШЕНИЕ № 2. Рабочее, быстрое (немного не доработан алгоритм, начиня со 100 дает не врный ответ, поэтому имеется костыль)
# from math import factorial as fact

# def qts(s):
#     k = 12
#     lvs = s // 10
#     qti = int(fact(s + k - 1) / (fact(k - 1) * fact(s)))
#     if lvs == 0:
#         return qti
#     qtm = 0
#     for i in range(1, lvs + 1):
#         s -= 10
#         qtm += qts(i) * qts(s)
#     return qti - qtm

# s = int(input())
# if s > 108:
#     qt = 0
# else:
#     s = 108 - s if s > 99 else s
#     qt = qts(s)
# print(qt)

# Task 1.1.12
from math import lcm

n = int(input())
qt2 = n // 2
qt3 = n // 3
qt5 = n // 5
qt23 = n // lcm(2, 3)
qt25 = n // lcm(2, 5)
qt35 = n // lcm(3, 5)
qt235 = n // lcm(2, 3, 5)
qt23_nc = qt23 - qt235
qt25_nc = qt25 - qt235
qt35_nc = qt35 - qt235
qt2_nc = qt2 - qt23_nc - qt25_nc - qt235
qt3_nc = qt3 - qt23_nc - qt35_nc - qt235
qt5_nc = qt5 - qt25_nc - qt35_nc - qt235
result = n - qt2_nc - qt3_nc - qt5_nc - qt23_nc - qt25_nc - qt35_nc - qt235
print(result)