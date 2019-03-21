from itertools import groupby

s = input()
for k, v in groupby(s):
    print("({}, {})".format(len(list(v)), k), end=" ")
