# -*- coding: UTF-8 -*-



import datetime



def interface():
    print(
'''
************************
    欢迎使用 ATM 机
请输入相应的数字执行操作
************************
      1 --- 查询
      2 --- 存款
      3 --- 取款
      4 --- 退出

                  0-明细
------------------------
''')


def sum_record(tup, index=1):
    bank_balance = 0

    for i in range(len(tup)):
        bank_balance += tup[i][index]

    return bank_balance


def query(tup):
    print("您的账户余额为：{0} 元。".format(sum_record(tup)))


def deposit(tup, bank_balance_limit=1000000000):
    depo = 0
    bank_balance = 0
    tup_tmp = tup
    try:
        depo = int(input("请输入您要存款的数额："))
        if depo > 0:
            tup += ((str(datetime.datetime.now()), depo),)
            bank_balance = sum_record(tup)
            if bank_balance <= bank_balance_limit:
                print("操作成功，您现在的账户余额为：{0} 元。".format(bank_balance))
                return tup
            else:
                print("超过存款上限 10 亿元，请重新输入。")
                return tup_tmp
        else:
            print("请输入一个正整数。")
            return tup_tmp
    except:
        print("请输入一个正整数。")
        return tup_tmp


def withdraw(tup, bank_balance_limit=0):
    draw = 0
    bank_balance = 0
    tup_tmp = tup
    try:
        draw = -int(input("请输入您要取款的数额："))
        if draw < 0:
            tup += ((str(datetime.datetime.now()), draw),)
            bank_balance = sum_record(tup)
            if bank_balance >= bank_balance_limit:
                print("操作成功，您现在的账户余额为：{0} 元。".format(bank_balance))
                return tup
            else:
                print("对不起，您的账户余额不足。")
                return tup_tmp
        else:
            print("请输入一个正整数。")
            return tup_tmp
    except:
        print("请输入一个正整数。")
        return tup_tmp


def history(tup):
    print("*********************交易明细**********************")
    print("{:20s}{:10s}{:10s}".format("交易日期", "交易金额（元）","余额（元）"))

    for i in range(len(tup)):
        print("{:24s}{:17s}{:10s}".format(str(tup[i][0][0:19]), str(tup[i][1]), str(sum_record(tup[0:i+1]))))

    print("***************************************************")



tup_record = (("2020-01-01 12:00:00.000000", 100),)


interface()


while True:
    op = input("请输入您要执行的操作：")

    if op == "1":
        query(tup_record)
    elif op == "2":
        tup_record = deposit(tup_record)
    elif op == "3":
        tup_record = withdraw(tup_record)
    elif op == "4":
        print("欢迎再次使用 ATM 机，再见。")
        break
    elif op == "0":
        history(tup_record)
    else:
        print("无此项操作，请重新输入。")
