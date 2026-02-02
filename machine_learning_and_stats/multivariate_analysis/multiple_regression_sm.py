'''
 multiple_regression_sm.py
 重回帰分析の試し
  Created on 2018/1/21
  @author: Shuichi OHSAWA
'''

import pandas as pd
import matplotlib.pyplot as plt
from normalization import normalize
import plot


def calc_regression(df):
    import statsmodels.formula.api as sm
    reg = "y ~ x1 + x2"
    model = sm.ols(formula=reg, data=df)

    # 回帰分析を実行する
    result = model.fit()

    print(result.summary())

    # 先程の結果から値を獲得
    b1,b2,b3= result.params
    print(f'b1 = {b1}, b2 = {b2}, b3 = {b3}')
    plot.plot_pred_3D(df,b1,b2,b3)

def main(file_path):
    # データの読み込み
    df = pd.read_csv(file_path)
    df = df.set_index('No.')
    df = normalize(df)
    print(df)

    plot.plot_3D(df)
    plot.show_correlation(df)

    # 重回帰分析
    calc_regression(df)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='this is reg') 
    parser.add_argument('csv_path', help='file path')
    args = parser.parse_args() 
    main(args.csv_path)
