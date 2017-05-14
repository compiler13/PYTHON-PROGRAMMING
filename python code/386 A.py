

a=int(input())

b=int(input())

c=int(input())

if (a<1 or b<2 or c<4):

    print(0)
else:

    b1=b//2
    c1=c//4
    mn=min(b1,c1,a)
    ans=mn*1+mn*2+mn*4

    print(ans)

    
