# Task 1.1.3
# nums = sorted(map(int, input().split()))
# cd = nums.pop()
# ab = nums.pop(0) * nums.pop(0)
# nums.remove(ab)
# c = nums.pop(0)
# d = list(filter(lambda x: x * c == cd, nums))[0]
# print(d)

# Task 1.1.4
a, b = int(input()), int(input())
nums = b - a + 1
pairs = nums // 2
diff = [-1, 1][a % 2] * pairs + [1, -1][b % 2] * (nums % 2) * b
print(diff)