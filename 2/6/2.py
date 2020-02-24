# -*- coding: UTF-8 -*-



import codecs
import pandas as pd



dataset = \
"""色泽 根蒂 敲声 纹理 脐部 触感 密度 含糖率 好瓜
青绿 蜷缩 浊响 清晰 凹陷 硬滑 0.697 0.460 是
乌黑 蜷缩 沉闷 清晰 凹陷 硬滑 0.774 0.376 是
乌黑 蜷缩 浊响 清晰 凹陷 硬滑 0.634 0.264 是
青绿 蜷缩 沉闷 清晰 凹陷 硬滑 0.608 0.318 是
浅白 蜷缩 浊响 清晰 凹陷 硬滑 0.556 0.215 是
青绿 稍蜷 浊响 清晰 稍凹 软粘 0.403 0.237 是
乌黑 稍蜷 浊响 稍糊 稍凹 软粘 0.481 0.149 是
乌黑 稍蜷 浊响 清晰 稍凹 硬滑 0.437 0.211 是
乌黑 稍蜷 沉闷 稍糊 稍凹 硬滑 0.666 0.091 否
青绿 硬挺 清脆 清晰 平坦 软粘 0.243 0.267 否
浅白 硬挺 清脆 模糊 平坦 硬滑 0.245 0.057 否
浅白 蜷缩 浊响 模糊 平坦 软粘 0.343 0.099 否
青绿 稍蜷 浊响 稍糊 凹陷 硬滑 0.639 0.161 否
浅白 稍蜷 沉闷 稍糊 凹陷 硬滑 0.657 0.198 否
乌黑 稍蜷 浊响 清晰 稍凹 软粘 0.360 0.370 否
浅白 蜷缩 浊响 模糊 平坦 硬滑 0.593 0.042 否
青绿 蜷缩 沉闷 稍糊 稍凹 硬滑 0.719 0.103 否"""



# 添加编号列
s = ""

for i in range(len(dataset.split("\n"))):
    if i == 0:
        s += "编号," + ",".join(dataset.split("\n")[i].split(" ")) + "\n"
    else:
        s += str(i) + "," + ",".join(dataset.split("\n")[i].split(" ")) + "\n"

s = s[:-1]



# 将数据写入csv文件
# your code here
file = r'machine_learning.csv' # 文件名称，学员可修改或不修改

with codecs.open(file, 'w', encoding='utf-8') as f:
    f.write(s)



# 向csv文件中加入一条新的数据（数据已给出）
# your code here
# 注意每一行数据的间隔符号是什么
inser_data = '18 青绿 硬挺 浊响 稍糊 平坦 硬滑 0.666 0.111 是'

inser_data = "\n" + ",".join(inser_data.split(" "))

with codecs.open(file, 'a', encoding='utf-8') as f:
    f.write(inser_data)



# 查看全体数据
df = pd.read_csv(file)
print(df.head())


# 读取文件存储的数据
# your code here
# columns是指列标签
# datalist指全体数据内容，每一行数据应为一个列表
columns = []
datalist = []

with codecs.open(file, 'r', encoding='utf-8') as f:
    columns.extend(f.readline()[:-1].split(","))

    for line in f.readlines():
            datalist.append("".join(list(filter(lambda str: str!="\n", line))).split(","))


# 验证数据信息是否相符
print(columns==['编号', '色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖率', '好瓜'])
print(datalist[-1]==['18', '青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '是'])



# 第二种方法获得列标签和全体数据内容
df1 = pd.read_csv(file, dtype=object)

columns_df1 = []
datalist_df1 = []

columns_df1 = list(df1.columns)

datalist_df1 = df1.values.tolist()

# 验证数据信息是否相符
print(columns_df1==['编号', '色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖率', '好瓜'])
print(datalist_df1[-1]==['18', '青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '是'])



# 在所有数据中过滤出色泽='浅白'的数据
# 在所有数据中过滤出密度大于0.5的数据
# your code here

# 色泽='浅白'
COLOR = 1

datalist_filtrate_color = list(filter(lambda ls: ls[COLOR]=='浅白', datalist))


# 密度大于0.5
DENSITY = 7

datalist_filtrate_density = list(filter(lambda ls: float(ls[DENSITY])>0.5, datalist))


print(datalist_filtrate_color)
print("**********")
print(datalist_filtrate_density)
