def edit_distance(a, b):
    matrix = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif a[i - 1] == b[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])
            print(matrix[i][j], end=" ")
        print()


if __name__ == "__main__":
    a = input()
    b = input()
    edit_distance(a, b)
