"""
 複数の正規分布を足したデータを生成する
 Created on 2018/1/14
 @author: Shuichi OHSAWA
"""

import numpy as np
import matplotlib.pyplot as plt

def multi():

    nd1 = np.random.normal(10, 3, (250))
    nd2 = np.random.normal(20, 3, (250))

    data = np.concatenate([nd1, nd2])
    print(data)

    np.savetxt('test_data.csv', data)

    plt.hist(data, bins=40)
    plt.show()

if __name__ == '__main__':
    multi()