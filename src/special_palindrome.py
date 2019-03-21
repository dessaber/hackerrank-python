from itertools import combinations

a = "aaanaaa"#input()
d = dict()
for i in a:
    d[i] = d.get(i, 0) + 1

print(combinations(a, ))
