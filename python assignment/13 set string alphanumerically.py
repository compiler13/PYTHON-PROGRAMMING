
s=input()

s=s.split(" ")  #s is converted in to list

print(s)

s=set(s)       #remove duplicated word

print(s)

s=sorted(s)    # sort alphanumerically

print(" ".join(s))
