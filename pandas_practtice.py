

import pandas as pd
data ={
    'Name': ['Karthik', 'Dines', 'Vikram'],
    'Score': [85, 90, 78],
    'Age': [24, 22, 21]}
result =pd.DataFrame(data)

print(result)

# Pandas is a Python library used for working with structured/tabular data.
# Pandas helps us manipulate and analyze tabular data using Python.
# Pandas is a Python library used to work with data easily.
# Excel + Python  = Pandas
# Raw Data → Pandas → Clean Data → Analyze Data → Insights → Visualization

"""import pandas as pd"""

"""pandas → actual library name
pd → short name/alias
as → means "give another name"""

"""print(pd.__version__)"""

"""
Pandas lets you programmatically:

read data
inspect data
filter rows
select columns
handle missing values
remove duplicates
calculate statistics
group data
sort data
clean data
prepare data for visualization/modeling"""



import pandas as pd

# Create some data
"""data = {
    "Name": ["Arun", "Priya", "Rahul"],
    "Age": [22, 23, 21],
    "Marks": [85, 90, 78]
}
"""
# Convert the data into a DataFrame
# DataFrame = table-like structure in Pandas.
# DataFrame is like an Excel table, but we can manipulate it using Python.
"""df = pd.DataFrame(data)"""

# Display the DataFrame
"""print(df)"""


"""1. What is Pandas?
        ↓
2. import pandas as pd
        ↓
3. What is DataFrame?
        ↓
4. Create DataFrame
        ↓
5. print DataFrame
        ↓
6. Select one column
        ↓
7. Select multiple columns
        ↓
8. head()
9. tail()
10. shape
11. columns
12. info()"""
"""

data = {
    "Name": ["Arun", "Priya", "Rahul"],
    "Age": [22, 23, 21],
    "Marks": [85, 90, 78]
}"""

""" Name  → column    ["Arun", "Priya", "Rahul"] --> are the values inside the Name column.
Age   → column
Marks → column   """

# Convert it into a DataFrame Now:
"""
import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Rahul"],
    "Age": [22, 23, 21],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
# df is simply a variable name.

print(df)
"""




df = pd.DataFrame({
    "Name": ["Arun", "Priya", "Rahul"],
    "Age": [22, 23, 21],
    "Marks": [85, 90, 78]
})

print(df)


print(df[df["Marks"]>80])



print(df.iloc[0:3])