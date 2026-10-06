#PART A — PANDAS

# 1. Load the Dataset
#Load the given e-commerce CSV file into a Pandas DataFrame and display the first 10 records


import pandas as pd 

df = pd.read_csv("D:\pandas_practice\ecommerce_analytics_training_dataset.csv")

#2. Dataset Information
#Display:
#Number of rows, Number of columns, Column names,  Data types

print(df.head(10))

print(df.shape)

print(df.info())

print(df.columns)

#3. Select Columns
#Display only:

#product_name
#category
#retail_price
#rating

print(df["product"])
print(df["category"])
print(df["retail_price"])
print(df["rating"])

#4. Filter Products
#Find all products whose retail_price is greater than ₹5,000.

print(df[df["retail_price"] > 5000][["product", "retail_price"]])

#5. Multiple Conditions
#Find products where:

#retail_price > 5000
#AND
#rating >= 4
    
print(df[(df["rating"] > 4.0) & (df["retail_price"] > 5000)][["product", "retail_price", "rating"]])

#6. Create a New Column
#Create a column called discount_amount using:

#retail_price × discount / 100
df["Total_discount"] = df["retail_price"] * df["discount_pct"] / 100
print(df["Total_discount"])

#7. Calculate Final Price
#Create a new column:

#final_price = retail_price - discount_amount
df["Final_price"] = df["retail_price"] - df["discount_amount"]
print(df["Final_price"])    

#8. Sort the Data
#Display the 10 most expensive products based on retail_price.

print(df.groupby("product")["retail_price"].nlargest(10))

#9. Find Missing Values
#Find the number of missing values in each column

df.isnull().sum()
print(df.isnull().sum())

#10. Remove Duplicates
#Check for duplicate records and remove them. Display the number of records before and after removing duplicates    

print(df.shape)
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(df.shape)

#11. Category Analysis
#Find how many products are available in each category.

print(df["category"].value_counts())

#12. GroupBy Analysis
#Find the average retail price for each category.   

print(df.groupby("category")["retail_price"].mean())

#13. Regional Analysis
#Find the total number of products available in each region.    

print(df.groupby("region")["product"].count())  

#14. Pivot Table
#Create a pivot table showing:  

#Region × Category

#and count the number of products in each combination.

print(pd.pivot_table(df, index="region", columns="category", values="product", aggfunc="count"))

#15.Merge Datasets
#Create two small DataFrames:

#customers
#customer_id
#customer_name
#city

#and

#orders
#order_id
#customer_id
#order_amount

customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "customer_name": ["Karthik", "Ramesh", "Suresh"],
    "city": ["Dharmapuri", "Salem", "Krishnagiri"], 

})

orders = pd.DataFrame({
    "order_id": [101, 102, 103],
    "customer_id": [234, 456, 789],
    "order_amount": [1000, 2000, 3000]
})  

merged_df = pd.merge(customers, orders, on="customer_id")
print(merged_df)    

#PART B — NUMPY

#16. Create a 1D Array

#Create a NumPy array containing:

#10, 20, 30, 40, 50

import numpy as np 

arr = np.array([10, 20, 30, 40, 50])
print(arr.ndim)

#Display the array and its data type.
print(arr)
print(arr.dtype)    

#17. Array Information

#Create a 1D array containing 10 numbers and display:

#ndim
#shape
#size

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

#18. Array Indexing

#Given:
arr = np.array([25, 40, 55, 70, 85, 100])

#Find the:

#First value
#Third value
#Last value

print(arr[0])
print(arr[2])   
print(arr[-1]) 

#19. Array Slicing
#Using the same array, extract:

40, 55, 70

#without manually creating another array.

print(arr[1:4])

#20. Array Arithmetic

#20. Array Arithmetic

#Given:

#prices = np.array([100, 200, 300, 400, 500])

#Increase every price by ₹50.

prices = np.array([100, 200, 300, 400, 500])
print(prices + 50)

#21. Discount Calculation

#Given:

#prices = np.array([1000, 2000, 3000, 4000])

#Apply a 10% discount to every price.

prices = np.array([1000, 2000, 3000, 4000])
print(prices *10/100)

#22. Find Statistical Values

#Given:

#sales = np.array([1200, 1500, 1800, 2100, 2500])

#Find:

#Total
#Average
#Maximum
#Minimum

sales = np.array([1200, 1500, 1800, 2100, 2500])

print(sales.sum())
print(sales.mean())
print(sales.max())
print(sales.min())  

#23. Find Maximum Position

#Given:
#Find the position/index of the highest sales value.

sales = np.array([1200, 1800, 900, 2500, 1500])  #np.argmax() function returns insides of the maximum value of the array.

print(np.argmax(sales))

#24. Create a 2D Array

#Create the following NumPy array:

10, 20, 30
40, 50, 60
70, 80, 90

#Display:

np.ndim
np.shape
np.size

arr2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(arr2d.ndim)
print(arr2d.shape)
print(arr2d.size)   

#25. 2D Array Indexing

#Using the previous array, extract:

50

#using row and column indexing.

print(arr2d[1, 1])  #row index 1 and column index 1

#26. 2D Array Slicing

#Extract the following portion:

20, 30
50, 60  


#using NumPy slicing.

print(arr2d[0:2, 1:3])  #row index 0 to 1 and column index 1 to 2

#27. Reshape an Array

#Create:

arr = np.arange(1, 13)

#Convert it into:

#3 rows × 4 columns

#using reshape().

arr = np.arange(1, 13)
new_arr = arr.reshape(3, 4)

print(new_arr)


#28. Concatenate Arrays

#Create:

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

#Concatenate them into:

#[10 20 30 40 50 60]


print(np.concatenate([a, b]))

#29. Compare Two Arrays

#Given:

a = np.array([10, 20, 30, 40])
b = np.array([15, 20, 25, 40])

#Find which elements of a are greater than the corresponding elements of b.

print(a > b)

#30. Mini Data Analytics Challenge 

#Given:

sales = np.array([
    [1000, 1200, 1500],
    [1800, 1600, 2000],
    [900,  1100, 1300]
])

#Consider:

#Rows    → Regions
#Columns → Months

#Find:

#Total sales
#Average sales
#Highest sales
#Lowest sales
#Shape of the array
#Total sales for each row

print(sales.sum())
print(sales.mean())
print(sales.max())
print(sales.min())
print(sales.shape)
print(sales.sum(axis=1))















