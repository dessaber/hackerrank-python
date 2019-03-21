# Enter your code here. Read input from STDIN. Print output to STDOUT


def count_happiness(first, second, array):
    res = 0
    for i in array:
        if i in first:
            res += 1
        elif i in second:
            res -= 1
    return res


def str_to_set(str):
    return set(map(int, str.split(" ")))


if __name__ == "__main__":
    _, _ = map(int, input().split(" "))
    input_array = map(int, input().split(" "))
    first_set, second_set = str_to_set(input()), str_to_set(input())
    print(count_happiness(first_set, second_set, input_array))
