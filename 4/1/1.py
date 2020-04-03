#  数据实现 SVM 和决策树的回归算法


# -*- coding: UTF-8 -*-


import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor


# 数据预处理
ccpp_df = pd.read_csv("data.csv")

ccpp_df = ccpp_df.drop_duplicates()
ccpp_df = ccpp_df.reset_index(drop=True)

ccpp_df = ccpp_df.dropna()
ccpp_df = ccpp_df.reset_index(drop=True)

# x 代表样本特征集，y 代表样本标签集
x = ccpp_df.iloc[:, :4]
y = ccpp_df.iloc[:, -1:]

# 将数据转换为 array
x = np.array(x)
y = np.array(y)

# 扁平化
y = np.ravel(y)

# 标准化
sc = StandardScaler()
x = sc.fit_transform(x)


# 分割数据
# 数据量较小（一万以下），将训练集和测试集划分为 7:3，即 test_size=0.3
# 指定随机数种子 random_state 为 1，保证重复运行程序时，每次得到的训练集和测试集都一致
# x_train 代表训练样本特征集，y_train 代表训练样本标签集
# x_test 代表测试样本特征集，y_test 代表测试样本标签集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)


# 定义 SVM
svr = SVR()
svr.fit(x_train, y_train)

score_svr = svr.score(x_test, y_test)
print("SVM:", score_svr)


# 定义决策树
dtr = DecisionTreeRegressor(criterion="mse", max_depth=100, random_state=1)
dtr.fit(x_train, y_train)

score_dtr = dtr.score(x_test, y_test)
print("决策树：", score_dtr)
