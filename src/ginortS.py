symbols = input()
odds = []
evens = []
uppers = []
lowers = []

for i in symbols:
    if i.isdigit():
        digit = int(i)
        if digit % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    elif i.isupper():
        uppers.append(i)
    elif i.islower():
        lowers.append(i)

print("".join(sorted(lowers) + sorted(uppers) + sorted(odds) + sorted(evens)))
