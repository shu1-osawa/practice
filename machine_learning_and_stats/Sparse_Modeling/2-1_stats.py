# coding:utf-8
#### データの読み込み
import pandas as pd


file = 'data/1_test_reg.csv'
df = pd.read_csv(file)


### 各データの相関を調べる
print (df)
print(df.corr())

# 各相関を描画する
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
scatter_matrix(df)
plt.show()


### 回帰分析
import statsmodels.api as sm

# 変数の定義
X = df.loc[:,['MaxTemp','MinTemp','Humi','Wind','Sun']]
Y = df['Earn']

# モデルの生成
model = sm.OLS(Y, sm.add_constant(X))

# アルファの値を振ってみる
import math
alpha_list = [10 ** (i / 5.0) for i in range(40)]
b = pd.DataFrame() # 回帰係数を格納するデータフレーム

# 解パス図を作成するためにアルファの値を振りながら回帰係数を求める
for alpha_v in alpha_list:

    result = model.fit_regularized(
                        method='elastic_net',
                        alpha=alpha_v,
                        L1_wt=1.0,
                        start_params=None,
                        profile_scale=False,
                        refit=False
                        )

    # 回帰分析を実行する
    b=pd.concat([b,result.params.T],axis=1)

### 描画
plt.style.use('ggplot') # ggplotを使う
font = {'family' : 'meiryo'} # フォントをメイリオにする

b.columns=[math.log10(i) for i in alpha_list] # 列名を変える
b.T.plot()
plt.legend()
plt.xlabel("Alpha [log10]")
plt.xlabel("Regression coefficient")

plt.show()

print(b.T.loc[:,['MaxTemp','MinTemp','Humi','Wind','Sun']])
