import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn import manifold

n = 1000    # データの数

# データを生成する
data = np.array(3*np.pi*np.random.random(n))

# 三次元のデータを生成する
x = np.vstack((data*np.sin(data), 10*np.random.random(n), data*np.cos(data)))

# スイスロールの描画
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(
    x[0,:],x[1,:],x[2,:],
    c=data)
plt.show()


# ラプラス固有写像の設定
obj_SE = manifold.SpectralEmbedding(
    eigen_solver="arpack",  # 固有値のソルバ
    n_components=2,        # 射影した後の次元
    n_neighbors =20,       # グラフの近傍の数
    )

# 次元圧縮を実行する
xe = obj_SE.fit_transform(x.T)

# 次元圧縮後のデータを描画する
plt.scatter(xe[:,0],xe[:,1], c=data)
plt.show()