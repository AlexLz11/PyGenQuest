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
import time
s = int(input())
tb = time.time()
count = 0
for i in range(1000000000000):
    pass
te = time.time()
print(count)
print(te - tb)