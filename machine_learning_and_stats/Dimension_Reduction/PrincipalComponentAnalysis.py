import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA


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
obj_PCA = PCA(n_components=2)

# Isomapの計算
x_pca = obj_PCA.fit_transform(x.T)

# 次元圧縮後のデータを描画する
plt.scatter(x_pca[:,0],x_pca[:,1], c=data)
plt.show()