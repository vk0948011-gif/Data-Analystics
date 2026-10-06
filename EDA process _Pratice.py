import pandas as pd

df = pd.read_csv("D:\pandas_practice\SuperMarket Analysis.csv")

print(df.head(5))

print(df.tail(5))

print(df.info())

print(df.sample(5))

print(df.shape)

print(df.columns)

"""print(df.to_string())"""  #Display complete information about the dataset.

# To find the dullicate values 

i= df["Product line"].duplicated()
print(i)

#Display all unique city 
print(df["City"].unique())

#Display how many invoice id 

print(df["Invoice ID"].count ())

#Which city has the most purchase?

k=df.groupby("City").size() # Which city has the most purchase in supermarket sales?
print(k)

#which one of  city is highest purchase in the supermarket ?

k=df.groupby("City").size().idxmax()
print(k)

#Descrpitive Analytics
#Shop Rating 

h=df["Rating"].mean()
print(h)

g=df.groupby('Product line')['Rating'].idxmax()  # how many members rating in product line ?
print(g)

# Greater Than Rating 7.0

Rating =df[df["Rating"] > 7.0] 
print(Rating)

# Maximum Rating in this dataset.

Product = df["Rating"].max()
print(Product)

# Average Unit Price

print(df["Unit price"].mean)

Product = df["Unit price"].max()
print(Product)

# Average Gross Income

print(df["gross income"].mean)

Product = df["gross income"].max()
print(Product)

# Sum discount price
# print(df["discount_price"].sum())

# Which is most method of payment?
k=df.groupby("Payment").size().idxmax()
print(k)

k=df.groupby("Payment").size()
print(k)

#How to calculate Total Gross Income 

print(df["gross income"].sum())

# How to calculate Total Unit Price 

print(df["Unit price"].sum())

# Filtering ....

# Display all product sales greater than > 80.22


result = df[df["Sales"] > 80.22]
print(result)

# Display all product sales less than < 80.22
result = df[df["Sales"] < 80.22]
print(result)

# Display all product equal to equal == 80.22

result = df[df["Sales"] == 80.22]
print(result)

#Display all orders from Yangon

dk = df[df["City"] == "Yangon"]
print(dk)

gh = df[df["City"] == "Naypyitaw"]
print(gh)

ka = df[df["City"] == "Mandalay"]
print(ka)

print((df["City"] == "Mandalay").sum())

print((df["City"] == "Naypyitaw").sum())

print((df["City"] == "Yangon").sum())

# Sorting:

print(df.sort_values("Unit price", ascending = False))

print(df.sort_values("Product line", ascending = False).head(10))

# Using Condition statement with User define fucntion 

def check_price(Sales):
    if Sales > 80.22:
        return "High Price"
    else:
        return "Low Price"

df["Price_Status"] = df["Sales"].apply(check_price)

# Display only high-price records
high_price = df[df["Price_Status"] == "High Price"]

print(high_price)

"""result = check_price(100.2)
print(result)"""






