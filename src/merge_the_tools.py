def merge_the_tools(string, k):
    result = []
    for i in range(len(string) // k):
        unique = set()
        actual_piece = []
        start = i * k
        for j in range(start, start + k):
            if string[j] not in unique:
                unique.add(string[j])
                actual_piece.append(string[j])
        result.append("".join(actual_piece))
    return result


if __name__ == '__main__':
    source, size = input().split(" ")
    result = merge_the_tools(source, int(size))
    for i in result:
        print(i)
