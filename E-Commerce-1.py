import pandas as pd

df = pd.read_csv("D:\pandas_practice\E-Commerce-1.csv")
"""
print(df.head(10))"""

print(df.tail(10))
print(df.shape)

print(df.info())
print(df.describe()) 

print(df.columns)

print(df.loc[[1]])
"""
print(df.iloc[0,1])"""   #print(df.iloc[:,1])

df["Mobile_number"] = 93619699367
print(df)
 
df["Customer_uniq_id"]
print(df)

print(df.drop(8904))

print(df.drop([8901, 8902, 8903, 8905]))





