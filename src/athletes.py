#!/bin/python3

import math
import os
import random
import re
import sys


def ksort(array, key):
    return sorted(array, key=lambda x: x[key])


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    result = ksort(arr, k)

    for i in result:
        for j in i:
            print(j, end=" ")
        print()
