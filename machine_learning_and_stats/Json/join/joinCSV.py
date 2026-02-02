# -*- coding: utf-8 -*-
"""
　pandasによるデータ結合
"""
import pandas as pd

# データの読み込み
f1 = pd.read_csv('CSV_file1.csv', header=None)
f2 = pd.read_csv('CSVfile2.csv', header=None)

# 結合
data = pd.concat([f1, f2])

# 書き出し
data.to_csv('newData.csv', index=False)