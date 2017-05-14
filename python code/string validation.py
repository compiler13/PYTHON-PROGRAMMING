
s=input()

a=any(i.isalnum() for i in s)

print(a)

b=any(i.isalpha() for i in s)

print(b)

c=any(i.isdigit() for i in s)

print(c)

d=any(i.islower() for i in s)

print(d)

e=any(i.isupper() for i in s)

print(e)
