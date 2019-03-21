#!/bin/python3

if __name__ == '__main__':
    s = input()

    letters = dict()
    for i in s:
        letters[i] = letters.get(i, 0) + 1

    output = sorted([(k, v) for k, v in letters.items()], key=lambda x: (-x[1], x[0]))
    for i in range(0, min(len(output), 3)):
        print(output[i][0] + " " + str(output[i][1]))

