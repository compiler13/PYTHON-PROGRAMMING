

s,s1=input(),input()


cnt=0

while s1 in s:
    
    cnt+=1
    s=s[s.find(s1)+1:]
    
    
    
print(cnt)    
