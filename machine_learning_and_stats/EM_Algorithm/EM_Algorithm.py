"""
　EMアルゴリズム
 Created on 2018/1/14
 @author: Shuichi OHSAWA
"""
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# ガウス分布の計算（データ，平均，分散）
def gaussian(x, mean, vari):
    return math.exp(- pow(x - mean, 2) / (2 *vari)) / math.sqrt(2 * math.pi *vari)

# Eステップの計算
def e_step(xs, ms, vs, p):
    burden_rates = []
    for x in xs:
        # 負担率の分母と分子の計算
        d = (1-p)*gaussian(x, ms[0], vs[0]) + p*gaussian(x, ms[1], vs[1])
        n = p*gaussian(x, ms[1], vs[1])

        # 負担率の計算
        burden_rate = n/d
        burden_rates.append(burden_rate)
    return burden_rates


# Mステップ
def m_step(xs, burden_rates):
    # 負担率を使って平均と分散を更新する
    # 正規分布１
    d = sum([1-r for r in burden_rates])
    n = sum([(1-r)*x for x, r in zip(xs, burden_rates)])
    mu1 = n/d

    n = sum([(1-r)*pow(x - mu1, 2) for x, r in zip(xs, burden_rates)])
    var1 = n/d

    # 正規分布２
    d = sum(burden_rates)
    n = sum([r*x for x, r in zip(xs, burden_rates)])
    mu2 = n/d

    n = sum(r*pow(x - mu2, 2) for x, r in zip(xs, burden_rates))
    var2 = n/d

    # piの更新
    N = len(xs)
    p = sum(burden_rates) / N

    return [mu1, mu2], [var1, var2], p


# 対数尤度関数の計算
def calc_log_likelihood(x_s, m_s, v_s, p_s):
    buff = 0
    for x in x_s:
        buff += math.log((1-p_s)*gaussian(x, m_s[0], v_s[0])
                      +p_s*gaussian(x, m_s[1], v_s[1]))
    return buff


# EMアルゴリズムの計算
def calc_EM(data):

    p_s = 0.5
    m_s = [random.choice(data), random.choice(data)]
    v_s = [np.var(data), np.var(data)]

    # EMアルゴリズム
    for t in range(100):
        # Eステップで負担率を計算する
        burden_rates = e_step(data, m_s, v_s, p_s)

        # MEステップでパラメータを更新する
        m_s, v_s, p_s = m_step(data, burden_rates)

    print('mean_1={0}, mean_2={1}, variance_1={2}, variance_2={3}, pi={4}'.format(
        m_s[0], m_s[1], v_s[0], v_s[1], p_s))


if __name__ == '__main__':

    data = np.loadtxt('test_data.csv', delimiter=",")
    calc_EM(data)