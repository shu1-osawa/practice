# -*- coding: utf-8 -*-
"""
データ読み込み
"""
# jsonのモジュールをインポートする
import json

# jsonファイルを読み込む
file = open("test.json")

# 読み込んだファイルオブジェクトからPythonデータを生成する
data = json.load(file)

# ファイルを閉じる
file.close()
 
# 表示する
print(json.dumps(data, sort_keys=True,indent=4))