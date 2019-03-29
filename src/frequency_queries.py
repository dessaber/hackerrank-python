import os
from collections import Counter


def freq_query(queries):

    freq = Counter()
    cnt = Counter()

    arr = []

    for q in queries:
        if q[0] == 1:
            cnt[freq[q[1]]] -= 1
            freq[q[1]] += 1
            cnt[freq[q[1]]] += 1

        elif q[0] == 2:
            if freq[q[1]] > 0:
                cnt[freq[q[1]]] -= 1
                freq[q[1]] -= 1
                cnt[freq[q[1]]] += 1

        else:
            if cnt[q[1]] > 0:
                arr.append(1)
            else:
                arr.append(0)

    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freq_query(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
