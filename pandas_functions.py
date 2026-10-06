import pandas as pd 

df=pd.read_csv("D:\pandas_Series\E-Commerce-1.csv")
# Reads the CSV file and stores it in a DataFrame called 'df'

"""print(df.head(10))"""
# Commented out - would print the first 10 rows if uncommented

print(df.tail(10))
# Prints the last 10 rows of the DataFrame

print(df.shape)
# Prints the dimensions of DataFrame as (rows, columns) - e.g., (8004, 5)

print(df.info())
# Prints detailed info: column names, data types, non-null counts, memory usage

print(df.describe())
# Prints statistical summary: count, mean, std, min, 25%, 50%, 75%, max for numeric columns

print(df.columns)
# Prints all column names in the DataFrame

print(df.loc[0:1])
# Prints rows with index labels 0 to 1 (inclusive on both ends) using label-based indexing

print(df.iloc[[]])
# Prints an empty selection - returns DataFrame with 0 rows (empty brackets mean no rows selected)

df["mobile_number"]=9597280170
# Adds a new column called 'mobile_number' with value 9597280170 assigned to all rows     

print(df)
# Prints the DataFrame after the column deletion

print(df.drop(8000))
# Prints the DataFrame excluding row with index 8000 (doesn't permanently delete it)

print(df.loc[7999:8003])
# Prints rows 7999 to 8003 again (same as before since drop() doesn't modify original df)