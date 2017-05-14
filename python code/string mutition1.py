
s=input()
a,s1=input().split()

a=int(a)

s=list(s)

s[a]=s1
s=''.join(s)

print(s)






s=input()
a,s1=input().split()

a=int(a)

s=s[:a]+s1+s[a+1:]



print(s)
