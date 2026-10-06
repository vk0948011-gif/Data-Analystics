import pandas as pd 
df = pd.read_csv("D:\pandas_practice\ecommerce_analytics_training_dataset.csv")

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


# Find the total sales by city.
total_sales = df.groupby ('city')['sales'].sum()   #pirnt(df.groupby ('city')['sales'].sum())
print(total_sales)

#Find the average retail price by category.

average_price = df.groupby('category')['retail_price'].mean()    #print(df.groupby('category')['retail_price'].mean())
print(average_price)

#Find the number of orders by city

Orders_city = df.groupby('city').size()                 #print(df.groupby('city').size())
print(Orders_city)

#Find the average product rating by category.

Rating = df.groupby('category')['rating'].mean()            #print(df.groupby('category')['rating'].mean())
print(Rating)

#Find the maximum retail price in each category.

maximum = df.groupby('category')['rating'].max()                #print(df.groupby('category')['rating'].max()      )
print(maximum)

#Find the minimum retail price in each category.

minimum = df.groupby('category')['rating'].min()                  #print(df.groupby('category')['rating'].min())
print(minimum)

#Find the total sales by region — output should be East, West, North, South.

total_sales = df.groupby('region')['sales'].size()             # print(df.groupby('region')['sales'].size())
print(total_sales)

#Find the number of products available in each category.   

number_of_products = df.groupby('category')['product'].count()   #print(df.groupby('category')['product'].count())
print(number_of_products)

#Find the average rating by region

print(df.groupby("region")["rating"].mean())


#Multiple Groupby 

#Find total sales by region and category.

print(df.groupby(["region", "category"])["sales"].sum())

#Find average retail price by region and category.

print(df.groupby(["region", "category"])["retail_price"].mean())

#Find total quantity sold by city and category.

print(df.groupby(["city", "category"])["quantity"].sum())

#Find number of orders by region and city.

print(df.groupby(["city", "region"]).size())

#Find average rating by category and region.

print(df.groupby(["region", "category"])["rating"].mean())

#Find the top 5 cities based on total sales.

print(df.groupby("city")["sales"].sum().nlargest(5))

#Find the category with the highest average rating.

print(df.groupby("category")["rating"].mean().nlargest(5))

#Find the region generating the highest revenue

print(df.groupby("region")["sales"].sum().idxmax())

print(df.groupby("region")["sales"].sum().nlargest(5))

#Find the category with the highest quantity sold in each region.

print(df.groupby("category")["quantity"].sum().idxmax())

#Find the top 10 products based on total sales.

print(df.groupby("product")["sales"].sum().nlargest(10))

#Extract Year from order_date

"""df["Year"] = pd.to_datetime(df["order_date"]).dt.year

df["order_date"] = pd.to_datetime(df["order_date"])
df["Year"] = df["order_date"].dt.year
print(df)
"""

# concat () means concatenate. 
# Concat () is used to combine two or more Pandas DataFrames into one DataFrame.

