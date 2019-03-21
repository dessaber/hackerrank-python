#!/bin/python3

import math
import os
import random
import re
import sys
from multiprocessing.dummy import Pool

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arrays = []
    pool = Pool(4)
    for q in queries:
        start, end, addend = q[0], q[1], q[2]
        arrays.append(produce_array(n, start, end, addend))
    return max(pool.starmap(sum, zip(*arrays)))


def produce_array(n, start, end, value):
    head = [0 for _ in range(0, start - 1)]
    middle = [value for _ in range(start - 1, end)]
    tail = [0 for _ in range(end, n)]
    return head + middle + tail


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
