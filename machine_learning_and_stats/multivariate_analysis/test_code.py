import pandas as pd

df = pd.DataFrame({ 'A' : [1,2,3,4,5],
                    'B' : [6,7,8,9,0],
                   })

print(df[['A','B']].values.tolist())
print(df.loc[:,['A','B']].values.tolist())

