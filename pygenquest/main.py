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

# Решение Chat GPT:
# Числовой промежуток [a,b]: a = 0, b = 10^12
#  F(k, m, n) = n! * P(k - m, n - 1)
# m - количество цифр в числе a, n - количество цифр в числе b
# F(k, m, n) - количество чисел с суммой цифр k в диапазоне [a, b]
# P(k, n) - количество способов разложить число k в сумму n неотрицательных целых чисел
# P(k, n) = (k + n - 1)! / (k! * (n - 1)!)
# from math import factorial as fact
# s = int(input())
# # m = 1
# n = 12
# # pkn = fact(s + n - 1 - m) / (fact(s) * fact(n - 1))
# pkn = 1
# f = fact(n) * pkn
# print(f)

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
# ***********************************************************
#
# F(s, 1, 12) = 12! * P(s - 1, 11)
# P(s - 1, 11) = (s - 1)! / (11! * (s - 1 - 11))!)
# from math import factorial as fact
# s = int(input())
# p = fact(s - 1) / (fact(11) * fact(s - 12))
# qt = fact(12) * p
# print(qt)
#
# ***********************************************************
#
from math import factorial as fact
s = int(input()) # например n (у нас это s) = 10, при k = 3, результат должен быть 66
k = 12
qts = fact(s + k - 1) / (fact(k - 1) * fact(s))
# qt1 = fact(1 + k - 1) / (fact(k - 1) * fact(1))
# qt3 = fact(3 + k - 1) / (fact(k - 1) * fact(3))
# # qt9 = fact(9 + k - 1) / (fact(k - 1) * fact(9))
# qt10 = fact(10 + k - 1) / (fact(k - 1) * fact(10)) - qt1
# # qt13 = fact(13 + k - 1) / (fact(k - 1) * fact(13)) - qt1 * qt3
# d = s - 9
# qtd = fact(d - 1 + k - 1) / (fact(k - 1) * fact(d - 1))
# qt = qts - qt1 * qt10
print(qts)