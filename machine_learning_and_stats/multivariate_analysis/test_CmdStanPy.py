'''
 CmdStanPyの動作確認
'''
from cmdstanpy import  CmdStanModel
#import numpy as np
from matplotlib import pyplot as plt
import arviz as az
import os
import cmdstanpy
cmdstanpy.install_cmdstan()
### Stanファイルを読み込んでオブジェクトを生成する
stan_file_path = 'sample_model.stan'
model = CmdStanModel(stan_file=stan_file_path)

# データの作成
front_and_back_list = [1,0,1,0,0,0,0,0,1,0]
data = {
    "N" : len(front_and_back_list),
    "y" : front_and_back_list
    }
# 実行
fit_sm = model.sample(data=data)

### 診断
la = fit_sm.stan_variables()
plt.figure(figsize=(10,3))
bins=15
for i, k in enumerate(la.keys()):
    boxplot_list =[]
    for j in range(chains):
        x = la[k][j*iter_sampling:(j+1)*iter_sampling]
        hist, bin_edges = np.histogram(x, bins=bins) # 度数分布に変換
        #print(len(hist),len(bin_edges))
        plt.subplot(len(la.keys()), 3, 3*i+1) 
        plt.plot(bin_edges[:bins], hist, alpha=0.6, lw=0.6)
        plt.subplot(len(la.keys()), 3, 3*i+2) 
        plt.plot(x, alpha=0.5, lw=0.8)
        boxplot_list.append(x)
    plt.subplot(len(la.keys()), 3, 3*i+3) 
    plt.boxplot(boxplot_list)
plt.show()

### 結果を解釈する
samples = az.from_cmdstanpy(posterior = fit_sm)
print(az.summary(samples))