import numpy as np

# D type

a = np.array([51, 56, 65, 87, 90])
print(a.dtype)

a = [51, 56, 65, 87, 90]
a = np.array(a, dtype = np.int16)
print(a.dtype)

# Float 
a = np.array([51.5, 56.7, 65.2, 87.9, 90.1], dtype = np.float32)
print(a.dtype)

b = [51.1, 56.2, 65.4, 87.5, 90.6]
b = np.array(b, dtype = np.float32)  # There is no float8, float16 in python, so it will convert to float32
print(b.dtype)
print(b)

b=[150,128,30,0.10]
b = np.array(b,dtype=np.float64)
np.set_printoptions(suppress = True)
print(b.dtype)
print(b)

c= ["karthik", "vignesh", "sathish"]
c=np.array(c)
print(c.dtype)
print(c)

d= [True, False, True, False]
d = np.array(d)
print(d.dtype)

d=[True, False]
d=np.array(d, dtype = np.bool_)
print(d.dtype)

# Object
e=["Karthik", 10, 20.5, True]
e= np.array(e, dtype =object)
print(e.dtype)

# Data Conversion
# Data type conversion is the process of converting one data type to another. In NumPy, you can convert the data type of an array using the astype() method.

# Data type conversion using astype() method.

import matplotlib.pyplot as plt


plt.plot('product', 'retail_price')

import pandas as pd 

df = pd.read_csv("D:\pandas_practice\ecommerce_analytics_training_dataset.csv")

print(df.head())

print(df.info())

df["retail_price"] = df["retail_price"].astype(float)
print(df["retail_price"])
print(df.info())

