import numpy as np

print(np.__version__)

#Numpy = Numerical Python 

#It is a python libary mainly used for numerical and array-based computing.

# Numpy is designed for efficient numerical operation on arrays, especially when we have lots of numerical date.

#Ex: Instead of manually doing:

"""Marks = [70, 80, 90, 85]

Marks[0] + 5
Marks[1] + 5
Marks[2] + 5
Marks[3] + 5

# Numpy can operate on the whole array:

import numpy as np 

marks = np.array([80, 75, 90, 85])
print(marks + 5)

# Numpy automatically performs the operation on every elemment.

numbers = [10, 20, 30, 40, 50]

#Converting it to Numpy:

arr = np.array(numbers)
print(arr)"""


# Numpy = Numerical Python. It is Python libary used mainly for working with numerical data efficiently.

""" NumPy
  ↓
Numerical Data
  ↓
Arrays
  ↓
Mathematical Operations
  ↓
Data Analysis"""

#array : An array is a collection of values arranged together.

# NumPy provides its own array structure for numerical computing.
# NumPy stands for Numerical Python, 
# so it is mainly used for working with numbers and performing mathematical operations efficiently.

#Array is the main data structure of NumPy.

marks = [80, 70, 90, 85]
#This is a Python list.


#A NumPy array is a data structure used to store numerical values 
# and perform mathematical operations efficiently.
# NumPy = library
# Array = data structure provided by NumPy
# Array is a data structure An array is a way of storing multiple values together.
"""arr = np.array([10, 20, 30, 40])

np.array(arr) """  #creates a NumPy array.


"""

numbers = np.array([10, 20, 30])

np      →      NumPy
array() →      NumPy function
numbers →      variable
[10, 20, 30] → values
numbers →      NumPy array"""

#NumPy is the library; Array is one of the main data structures provided by NumPy

# Dimensions:  1D dimensional - property of array...

arr = np.array([10, 20, 30, 40, 50])   #only single bracket is used for 1D array.
print(arr.ndim)  #1D array

#2D dimensional 
arr2 = np.array([[10, 20, 30], [40, 50, 60]])   #double bracket is used for 2D array.
print(arr2.ndim)  #2D array

print(arr2.shape)  #shape of the array

print(arr.size)

print(arr[0,1]) 
