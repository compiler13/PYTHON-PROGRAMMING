from collections import Counter
c = Counter()
for s in input():
    c[s] += 1
for s in sorted(c.most_common(), key = lambda x: (-x[1], x[0]))[:3]:
    print(s[0], s[1])