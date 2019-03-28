#!/bin/python3

import os
from src.frequency_queries.query_processor_builder import QueryProcessorBuilder


# Complete the freq_query function below.
def freq_query(queries):
    result = []
    builder = QueryProcessorBuilder()
    for query in queries:
        query_result = builder.create_processor(query[0], query[1]).execute()
        if query_result is not None:
            result.append(query_result)

    return result


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
