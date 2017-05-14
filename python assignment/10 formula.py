
import math
s=input()

s=s.replace(","," ")

print(s)

s=s.split(" ")
li=[]

print(s)

c=50
h=30

for i in range(len(s)):

    n=int(s[i])


    a=math.sqrt((2*c)*(n/h))

    li.append(str(int(a)))    



print(",".join(li))
