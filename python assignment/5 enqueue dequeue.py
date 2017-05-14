

from collections import deque


li=[1,2,3,4,5]


print(li)

d=deque(li)   #Declear deque

d.append(7)   #Add value in list

print(d)

d.pop()       #Delet right  value from list

print(d)

d.appendleft(7)

print(d)

d.popleft()

print(d)


