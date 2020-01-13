# -*- coding: UTF-8 -*-



days = 7
total_balance = 0

ls_incomes = []
ls_outcomes = []
dict_balances = {}


for i in range(days):
    ls_incomes.append(int(input("请输入第 {0} 天的收入：".format(i+1))))
for i in range(days):
    ls_outcomes.append(int(input("请输入第 {0} 天的支出：".format(i+1))))


dict_balances = {"第 {0} 天结余：".format(i+1):ls_incomes[i]-ls_outcomes[i] for i in range(days)}
total_balance = sum(dict_balances.values())


print("7天的收入(list)：", ls_incomes)
print("7天的支出(list)：", ls_outcomes)
print("每天的结余(dict)：", dict_balances)
print("最终的结余：", total_balance)


