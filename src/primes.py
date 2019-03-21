import itertools


def primes():
    a = 2
    fact = 1
    while True:
        if (fact + 1) % a == 0:
            yield a
        fact = fact * a
        a += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))


