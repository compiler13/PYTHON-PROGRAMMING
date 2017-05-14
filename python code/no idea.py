

n,m=input().split()

ar=input().split()

A=set(input().split())

B=set(input().split())

cnt=0

for i in ar:

    if i in A:
        cnt+=1
        

    if i in B:
        cnt-=1

    

print(cnt)
        
