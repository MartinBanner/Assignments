# -*- coding: UTF-8 -*-



# 设斐波那契数列的第0项为0，第1项为1，其余各项为前两项之和，即：
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...


# 生成包含前n项的斐波那契数列的列表（包括第0项）。
def ls_fib_gener(n):
    if n == 0:
        return [0]

    count = 1
    ls_fib = [0, 1]

    while count < n:
        ls_fib += [ls_fib[count-1] + ls_fib[count]]
        count += 1

    return ls_fib


# 给定一个数值n，将前n项的波那契数列打印出来（包括第0项）。
def print_fib(n):
    ls_fib = []

    ls_fib = ls_fib_gener(n)

    for i in range(len(ls_fib)):
        print('第{0}项:\t{1}'.format(i, ls_fib[i]))



n = 100

print_fib(n)
