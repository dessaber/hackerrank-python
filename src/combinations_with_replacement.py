from itertools import combinations_with_replacement

word, size = input().split(" ")
combs = sorted(map(lambda x: "".join(x), combinations_with_replacement(sorted(word), int(size))))
for c in combs:
    print(c)
