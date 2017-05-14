n, p = input().split()

n=int(n)
p=int(p)

s = []

for i in range(n):
    s.append([int(x) for x in input().split()][1:])




from itertools import product

pcomb=list(product(*s))

def func(nums):
    return sum(x*x for x in nums) % p


print(max(list(map(func, pcomb))))

