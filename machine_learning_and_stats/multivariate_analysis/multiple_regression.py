'''
 multiple_regression.py
 Stanとstatsmodelsで重回帰
  Created on 2022/2/23
  @author: Shuichi OHSAWA
'''

import os
import pandas as pd

import stan_support as ss

from normalization import normalize
import plot


def summarize_data(df):
    plot.plot_3D(df)
    plot.show_correlation(df)

def read_data(file_path):
    df = pd.read_csv(file_path)
    df = df.set_index('No.')
    df = normalize(df)
    print(df)

    return df

def main(file_path):
    # データの読み込み
    df = read_data(file_path)
    summarize_data(df)


    # 重回帰分析
    data = {
        'N': len(df) ,
        'x1': df['x1'].values.tolist() ,
        'x2':df['x2'].values.tolist(), 
        'y':df['y'].values.tolist(),
        }

    model_path = "model_multi_reg.stan"
    s_model = ss.Stan_model(model_path)
    s_model.fit(data)
    s_model.post()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='this is reg') 
    parser.add_argument('csv_path', help='file path')
    args = parser.parse_args() 
    main(args.csv_path)