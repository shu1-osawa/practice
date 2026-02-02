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


# Isomapのオブジェクト作成
obj_isomap = manifold.Isomap(
    n_neighbors=20,
    n_components=2
    )

# Isomapの計算
x_iso = obj_isomap.fit_transform(x.T)

# 次元圧縮後のデータを描画する
plt.scatter(x_iso[:,0],x_iso[:,1], c=data)
plt.show()