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
import time
# def get_j(n):
#     res = 0
#     for j in range(2 * n):
#         res += j
#     return res

# n = int(input())
# t_start = time.time()
# result = 0
# j = get_j(n)
# for i in range(n):
#     result += j + 2 * n * i
# t_stop = time.time()
# t = t_stop - t_start
# print(result)
# print(t)

# n = int(input())

# t1 = time.time()
# # s = 0
# # for i in range(n):
# #     s += i
# s = sum(range(n))
# t2 = time.time()
# print(s)
# print(t2 - t1)

n = int(input())
tb = time.time()
i = sum(range(n))
j = i + sum(range(n, 2 * n))
result = n * (j + 2 * i)
te = time.time()
print(result)
print(te - tb)