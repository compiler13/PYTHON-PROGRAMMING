

from collections import deque

n=int(input())

for i in range(n):

    p=int(input())

    d=deque(map(int,input().split()))

    q=deque()
    for j in range(p):

        
            
        
        

        if d[0]>=d[-1]:

            q.appendleft(d[0])
            d.popleft()

        else:

            q.appendleft(d[-1])
            d.pop()

         
        
    if sorted(q)==list(q):

        print("Yes")
    else:
            print("No")
