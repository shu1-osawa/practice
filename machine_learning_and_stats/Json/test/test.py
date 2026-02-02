# -*- coding: utf-8 -*-
"""
 データ読み込み
 Created on 2017/1/12
"""
import pandas as pd
import glob #　パターンを解析するためのモジュール
import pandas.tseries.offsets as offsets
import matplotlib.pyplot as plt
import numpy as np
import csv
import numpy as np

### Beacon Listの読み込み ###
beacon_df = pd.read_csv('beaconList_DPS.csv', index_col=[0])
beacon_list = []
print(beacon_df)
# ビーコンリスト作成
for a in beacon_df.index:
    for b in beacon_df.columns:
        beacon_list.append(beacon_df.ix[a,b])

# リストを作ってからマルチインデックス化する
beacon_df = beacon_df.stack()

### データファイルの読み込み ###
df = pd.read_csv('result1222_111222.csv', header=None) 

### 重複を消して新しいデータフレームを作る ###
d1 = df.drop_duplicates(subset=[1])
d_dt = pd.DataFrame(d1[1]) #　判定用のデータフレーム作成
d_dt = d_dt.reset_index(drop=True)
d_dt.columns =  ['time']

# データファイルからテーブルを作成
df2 = pd.DataFrame(([-105] * len(beacon_list) for i in d_dt.index), columns=beacon_list)
tab = pd.concat([d_dt, df2], axis=1)

#　データの格納
count = 0

for i in range(len(df)): # 元データを1行づつ読んでいく．
    # テーブルとデータファイルの時間が一致する列を探す
    while pd.to_datetime(tab.ix[count,0]) != pd.to_datetime(df.ix[i,1]):
        count=count+1
    # ビーコンリストの中を検索して一致したらテーブルに書き込む    
    for j in range(len(beacon_list)):
        if beacon_list[j] == df.loc[i,3]:
            tab.loc[count,df.loc[i,3]] = df.loc[i,4]
            
tab.to_csv('table.csv') 

### 区間識別 ###
# 結果用のデータフレームを作る
result = pd.DataFrame(index=range(len(d_dt)), columns=['time','MinNo','RSSI','Location','Details'])

for i in range(len(tab)):
    result['time'][i] = tab.ix[i,0]    # Indexに時間を入れる
    maxList = tab[i:i+1].describe().loc['max'].T
    maxRSSI = maxList.max()
    
    if  maxRSSI > -60:
        name = list(beacon_df[beacon_df == maxRSSI].index)
        minNo =  maxList.argmax()
        name = list(beacon_df[beacon_df == minNo].index)
        result['Location'][i] = name[0][0]# argmaxだけだと駄目だった
        result['MinNo'][i] =  minNo
        result['RSSI'][i] = maxRSSI
        result['Details'][i] = name[0][1]
    elif maxRSSI < -90:
        name = list(beacon_df[beacon_df == maxRSSI].index)
        minNo =  maxList.argmax()
        name = list(beacon_df[beacon_df == minNo].index)
        result['Location'][i] = 'somewhere'
        result['MinNo'][i] =  minNo
        result['RSSI'][i] = maxRSSI
        result['Details'][i] = 'No'
    else :    
        if len(tab[i-2:i+3]) < 5: # データの端を読み込んで５ステップ分ない場合
            dd1 = tab[i:i+1].describe().loc['50%'].T
        #    print(dd1)
        else :
            dd1 = tab[i-2:i+3].describe().loc['50%'].T # 一行だけ抜き出すと何故がひっくり返るので転地した
        buff = dd1.argmax()    
        result['MinNo'][i] = buff    # 中央値の中で最大の電波強度を出力するビーコンを検出する
        
        result['RSSI'][i] = dd1.max()        # 中央値を並べた中での電波強度を取り出す
    
        # リストから該当する列名を呼び出す
        name = list(beacon_df[beacon_df == buff].index)
        result['Location'][i] = name[0][0]
        result['Details'][i] = name[0][1]
        #　所属する場所を検索する

        if i == 0:
            dff1 = pd.DataFrame(dd1).T
            dff1.index = [tab.ix[i,0]] # インデックスに時間を入れる
            
        else:
            dff2 = pd.DataFrame(dd1).T
            dff2.index = [tab.ix[i,0]] # インデックスに時間を入れる
            dff1 = pd.concat([dff1, dff2]) 

dff1 = dff1.fillna(-105) # NaNを-105に置換
#print(result)
#print(dff1)

dff1.to_csv('RssiData.csv')
result.to_csv('result.csv')


# プロット
#x = result['time']
#y = result['Location']
#
#fig = plt.figure()
#
#ax = fig.add_subplot(1,1,1)
#
#ax.scatter(x,y)
#
#ax.set_title('first scatter plot')
#ax.set_xlabel('time')
#ax.set_ylabel('Zone')
#
#fig.show()


#for i in range(len(df1)):
#    #print(df1.ix[i,0])
#    #print(pd.to_datetime(df1.ix[i,0]) + offsets.Second(3))
#    while pd.to_datetime(df1.ix[i,0]) != pd.to_datetime(df.ix[count,0]):
#        ++count
#    while pd.to_datetime(df.ix[pivotB,0]) > pd.to_datetime(df.ix[count,0]- offsets.Second(2.5)):
#        --pivotB
#    while pd.to_datetime(df.ix[pivotB,0]) > pd.to_datetime(df.ix[count,0]- offsets.Second(2.5)):
#        --pivotF
#    for j in count + pivotB + pivotF:
#      ++j  
        
# 時間データに変換
#d3 = d1[d1[5] == 50]


#　Plotする
#plt.plot(dt,d3[6])
#plt.show()