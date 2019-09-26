# -*- coding:UTF-8 -*-
import os

import pandas as pd
import numpy as np


def handle_data():
    origin_data = pd.read_excel(os.path.join(os.path.dirname(__file__), "data.xls"), sheet_name="资金对账表")
    origin_data = origin_data.fillna(value=0)  # 填充空数据
    excel_headers = [item.strip() for item in origin_data.columns.to_list()]
    origin_data = pd.DataFrame(origin_data.values, columns=excel_headers)
    origin_data = origin_data[~origin_data['投资者代码'].isin([0])]
    origin_data.to_excel("handle_data.xls")

    print(origin_data.to_dict())


if __name__ == '__main__':
    # handle_data()

    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df1 = pd.DataFrame(a, index=['row0', 'row1', 'row2'], columns=list('ABC'))
    # 取A列的数据
    print("A列的数据\r\n", df1["A"])
    print("A, B两列的数据\r\n", df1.loc[:, ["A", "B"]])
    print("A, C两列的数据\r\n", df1.loc[["A", "C"]])
    print("前两列的数据\r\n", df1.iloc[:, [0, 1]])

    print("指定行列名的数据\r\n", df1.at["row0", "A"])
    print("指定位置的数据\r\n", df1.iat[0, 0])

    print("选取df1中A列包含数字1, 4的行\r\n", df1[df1['A'].isin([1, 4])])
    print("选取df1中A列包含数字1的行\r\n", df1[df1['A'] == 1])
    print("选取df1中A列不包含数字1的行\r\n", df1[~df1['A'].isin([1])])

    df2 = df1.copy()
    print("删除A列数据\r\n", df2.drop(["A"], axis=1))
    print("删除 row0 行数据\r\n", df2.drop(["row0"], axis=0))

    # 赋值
    df2.loc["row0", ["A"]] = 2
    df2.iloc[0, 1] = 3
    print("赋值\r\n", df2)

