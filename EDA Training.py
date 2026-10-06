import pandas as pd 
df = pd.read_csv("D:\pandas_practice\ecommerce_analytics_training_dataset.csv")

df.isnull().sum()
print(df.isnull().sum())

print(df.duplicated().sum()) # To verify duplicate is there or not and sum them
 
print(df.dropna()) # Remove missing values 

print(df.shape)

"""print(df.fillna({"city":["chennai"]})) """ # fill missing values 

print(df.drop_duplicates())

# Data Transformation 

# To Change column names 

df.rename(columns ={
    "retail_price":"Retail_Price",
    "customer_name" : "Customer_Name"}
    ,inplace = True)

print(df.columns)

print(df.head())

# create a new column 

# calculate total sales:

df['Total_Sales'] = df['Retail_Price'] * df['quantity']

print(df[['Retail_Price','quantity', 'Total_Sales']].head())

# Text Transform # Uppercase 

df['product'] = df['product'].str.upper()

print(df['product'].head())

#Lower case all products

df['product'] = df['product'].str.lower()

print(df['product'])

df["region"] = df["region"].replace({
    "East" : "E",
     "West" : "W",
     "North" : "N",
    "South" : "S"
})

print(df["region"])

#Create a price_category column based on retail_price
df['price_category'] = pd.cut(df['retail_price'], bins=[0, 500, 1000, float("inf")], labels=["Low", "Medium", "High"])
print(df['price_category'])
