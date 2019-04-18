def sort(a):
    if len(a) <= 1:
        return a

    middle = len(a) // 2
    left = sort(a[:middle])
    right = sort(a[middle:])

    return merge(left, right)


def merge(a, b):
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1

    return result


print(sort([4, 5, 1, 2, 9]))

