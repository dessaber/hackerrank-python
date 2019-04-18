def insertion_sort(a):
    for i in range(1, len(a)):
        current = a[i]
        j = i
        while j > 0 and a[j - 1] > current:
            a[j] = a[j - 1]
            j -= 1
        a[j] = current

    return a


if __name__ == "__main__":
    input_str = list(map(int, input().split(" ")))
    print(insertion_sort(input_str))
