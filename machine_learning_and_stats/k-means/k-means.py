# -*- coding: utf-8 -*-
"""
sklearnを使ったKmeans

Created on Fri Feb 24 21:41:18 2017
@author: S.OHSAWA
"""

import os
import pandas as pd
import pylab
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#　作業ディレクトリを変える（ワークスペースが変な場所にあるため）
os.chdir("practice\statistics_and_machine_learning\kmeans")

#　データフレーム作成
df = pd.read_csv( "dataset.csv",names=('x', 'y'))

#　データフレームのデータをプロットする
pylab.figure(figsize=(9, 6)) # サイズ変更
df.plot(kind='scatter', x='x', y='y') # 散布図でプロット
plt.savefig("imageData.png") # 保存する

#　Kmenasのメソッドに渡すためにデータフレームからArrayに変換する
array = df.as_matrix()

#　Kmenasで分類して，新しい列に追加する
df['cluster'] = KMeans(n_clusters=3).fit_predict(array)

#　各クラスターに属するデータの個数を表示する
print(df['cluster'].value_counts())

#　データを描画する
# No0のクラスターに属するデータを赤で表示
ax = df[df['cluster']==0].plot( kind='scatter', x='x', y='y', color='red' ) 
# No1のクラスターに属するデータを赤で表示
df[df['cluster']==1].plot( kind='scatter', x='x', y='y', color='seagreen', ax = ax )
# No3のクラスターに属するデータを赤で表示
df[df['cluster']==2].plot( kind='scatter', x='x', y='y', color='blue', ax = ax )

# プロットする
plt.savefig("imageResult.png")

# 結果をCSVファイルに書き出す
df.to_csv("result.csv")