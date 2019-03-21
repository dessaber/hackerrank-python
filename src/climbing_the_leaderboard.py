#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    distinct_scores = [scores[0]]
    for i in range(1, len(scores)):
        if scores[i] != scores[i - 1]:
            distinct_scores.append(scores[i])


    return []


def bin_search(l, start, end, find):
    if start + 1 >= end:
        if l[1] <= find < l[0]:
            return 2
        elif l[0] <= find:
            return 1
        elif l[len(l) - 2] <= find < l[len(l) - 1]:
            return len(l)
        elif find < l[len(l) - 2]:
            return len(l) + 1

    middle = start + (end - start) // 2
    print("list = {}, start = {}, end = {}, middle = {}".format(l, start, end, middle))
    if l[middle] < find:
        return bin_search(l, start, middle - 1, find)
    elif l[middle] > find:
        return bin_search(l, middle + 1, end, find)
    else:
        return middle + 1

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    scores_count = int(input())
#
#    scores = list(map(int, input().rstrip().split()))
#
#    alice_count = int(input())
#
#    alice = list(map(int, input().rstrip().split()))
#
#    result = climbingLeaderboard(scores, alice)
#
#    fptr.write('\n'.join(map(str, result)))
#    fptr.write('\n')
#
#    fptr.close()
    print(bin_search([110, 80, 70, 30, 20, 3], 0, 5, 45))
