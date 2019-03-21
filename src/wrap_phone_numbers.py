def wrapper(f):
    def fun(phone_numbers):
        res = []
        for number in phone_numbers:
            str_num = str(number)
            if len(str_num) == 10:
                res.append("+91 " + str_num[0:5] + " " + str_num[5:])
            elif len(str_num) == 11:
                res.append("+91 " + str_num[1:6] + " " + str_num[6:])
            elif len(str_num) == 12:
                res.append("+" + str_num[0:2] + " " + str_num[2:7] + " " + str_num[7:])
            else:
                res.append(str_num[0:3] + " " + str_num[3:8] + " " + str_num[8:])
        return f(res)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


