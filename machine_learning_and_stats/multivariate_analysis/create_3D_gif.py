"""
create_3D_gif.py
3Dプロットのgif動画を作成する
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import os,glob
from PIL import Image

def create_rotate_3D_gif(csv_path):
    df = pd.read_csv(csv_path)
    df = df.set_index('No.')
    print(df)

    # データを３次元プロットしてみる
    fig = plt.figure(figsize=(15,10))
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

    ax.scatter(xs, ys, zs)

    dir_name = 'figures'

    if not os.path.exists(dir_name):
        os.makedirs(dir_name )

    # for angle in range(0, 360, 3):
    #     
    #     

    # fig_list = glob.glob('figs/*.png')
    # fig_list[0].save('figs/rotate_3D.gif',
    #            save_all=True, append_images=fig_list[1:], optimize=False, duration=40, loop=0)
    figs =[]
    for angle in range(0, 360, 2):
        ax.view_init(10, angle)
        plt.savefig(dir_name+"/{0}_{1:03d}.png".format('fig', angle))
        fig_name = dir_name+"/{0}_{1:03d}.png".format('fig', angle)
        figs.append(Image.open(fig_name))
    figs[0].save('rotate_anime.gif',save_all=True, append_images=figs[1:],
            optimize=False, duration=100, loop=0)

def plot_rotate_3D(csv_path):
    df = pd.read_csv(csv_path)

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
    for angle in range(0, 360):
        ax.view_init(30, angle)
        plt.draw()
        #plt.pause(.001)
    #plt.show()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='3D') 
    parser.add_argument('csv_path', help='file path')
    args = parser.parse_args() 
    plot_rotate_3D(args.csv_path)
    create_rotate_3D_gif(args.csv_path)