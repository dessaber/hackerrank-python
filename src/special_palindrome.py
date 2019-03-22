#!/bin/python3

import os


# Complete the substrCount function below.
def substrCount(n, input_string):
    compressed_string = []
    current_symbol = None
    current_count = 0
    for i in input_string:
        if current_symbol is None:
            current_symbol = i
        if current_symbol == i:
            current_count += 1
        else:
            compressed_string.append((current_symbol, current_count))
            current_symbol = i
            current_count = 1

    compressed_string.append((current_symbol, current_count))
    amount = 0
    # L * (L + 1) / 2 - amount of all possible palindromes based on length stored in a tuple
    for i in range(0, len(compressed_string)):
        amount += compressed_string[i][1] * (compressed_string[i][1] + 1) // 2

        # if [...(A, Na') (B, 1) (A, Na'')...]
        if 0 < i < len(compressed_string) - 1 \
                and compressed_string[i - 1][0] == compressed_string[i + 1][0] \
                and compressed_string[i][0] != compressed_string[i - 1][0] \
                and compressed_string[i][1] == 1:

            amount += min(compressed_string[i - 1][1], compressed_string[i + 1][1])

    return amount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
