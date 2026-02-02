'''
 plot.py
 データの描画
  Created on 2022/2/23
  @author: Shuichi OHSAWA
'''

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 


def plot_3D(df):
    # データを３次元プロットしてみる
    fig = plt.figure()
    ax = Axes3D(fig)

    # 軸ラベルを設定する
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    # データをarrayに変換する
    xs = df.iloc[:,0].values
    ys = df.iloc[:,1].values
    zs = df.iloc[:,2].values

    # 表示範囲を指定する
    ax.set_xlim(min(xs)*0.95, max(xs)*1.05)
    ax.set_ylim(min(ys)*0.95, max(ys)*1.05)
    ax.set_zlim(min(zs)*0.95, max(zs)*1.05)

    # 描画
    ax.scatter3D(xs, ys, zs)
    plt.show()

def show_correlation(df):
    # 相関係数を表示
    df.corr()
    print(df.corr())

    # 散布図行列を描く
    #from pandas.tools.plotting import scatter_matrix
    #scatter_matrix(df.T)
    pd.plotting.scatter_matrix(df)
    plt.show()

def plot_pred_3D(df,b1,b2,b3):
    # もう一回描画する
    import numpy as np

    # データをarrayに変換する
    xs = df.iloc[:,0].values
    ys = df.iloc[:,1].values
    zs = df.iloc[:,2].values

    # 変数の区間の指定
    x = np.arange(min(xs)*0.95, max(xs)*1.05, (max(xs)*0.95 - min(xs)*1.05)/6)
    y = np.arange(min(ys)*0.95, max(ys)*1.05, (max(ys)*0.95 - min(ys)*1.05)/6)
    #x = np.arange(0, 10, 2)
    #y = np.arange(0, 10, 2 )
    # メッシュ表示
    X, Y = np.meshgrid(x, y)

    # 回帰式を代入する
    Z = b1 + b2*X +b3*Y

    # 初期化
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(X,Y,Z)

    # 軸名を設定する
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    # 表示範囲を指定する
    ax.set_xlim(min(xs)*0.95, max(xs)*1.05)
    ax.set_ylim(min(ys)*0.95, max(ys)*1.05)
    ax.set_zlim(min(zs)*0.95, max(zs)*1.05)

    # 描画
    ax.scatter3D(xs, ys, zs)
    plt.show()