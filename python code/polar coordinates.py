from collections import OrderedDict
dct = OrderedDict()

for i in range(int(input())):
    s = input()
    dct[s] = dct.get(s, 0) + 1
    
print(len(dct))
for j in dct.values():
    print(j, end=' ')
