
from itertools import combinations

s,n=input().split()

n=int(n)

for i in range(1,n+1):

    [print( ''.join(k)) for k in list(combinations(sorted(s),i))]