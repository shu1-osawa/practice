'''
 normalization.py
 標準化する（N(0,1)に収める）
  Created on 2022/2/23
  @author: Shuichi OHSAWA
'''

import pandas as pd
from scipy import stats

def normalize(df):
    return df.apply(stats.zscore, axis=0)
