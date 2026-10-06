#1 Arithmetic Operators

# Addition        10 + 5
# Subtraction     10 - 5
# Multiplication  10 * 5
# Division        10 / 5
# Modulus         10 % 5
# Floor Division  10 // 5
# Exponentiation  10 ** 5

# Operator = +, -, *, /, %, //, **
# Operand = 10, 3 
# Operation = 10 + 3, 10 - 3, 10 * 3, 10 / 3, 10 % 3, 10 // 3, 10 ** 3


a = 10
b = 3
print (a + b)  # Addition
print (a - b)  # Subtraction
print (a * b)  # Multiplication
print (a / b)  # Division
print (a % b)  # Modulus
print (a // b) # Floor Division
print (a ** b) # Exponentiation


# Analytics concept

total_sales = 100000
total_orders = 250

average_order_value = total_sales / total_orders
print(average_order_value)

total_revenue = 100000
total_customers = 250
average_revenue_per_customer = total_revenue // total_customers
print(average_revenue_per_customer)


#2 Assignment Operators
# These are used to assign/update values.

# =      Assignment
# +=     Add and assign
# -=     Subtract and assign
# *=     Multiply and assign
# /=     Divide and assign
# %=     Modulus and assign

sales = 20000

sales += 5000  # which means sales = sales + 5000
sales -= 3000  # which means sales = sales - 3000
sales *= 2     # which means sales = sales * 2
sales /= 4     # which means sales = sales / 4
sales %= 3     # which means sales = sales % 3
sales //= 2    # which means sales = sales // 2
print(sales)


# which means sales = sales + 5000

#3 Comparison Operators
# This is VERY important because you'll use these in conditional statements later.

# Comparison operators compare two values and give:
#True or False

# ==	Equal to
# !=	Not equal
# >	    Greater than
# <	    Less than
# >=	Greater than or equal
# <=	Less than or equal

sales = 80000 

print(sales > 75000)
print(sales < 75000)
print(sales == 75000)
print(sales != 75000)
print(sales >= 75000)
print(sales <= 75000)

# Comparison operators always help us answer a question: True or False?


#4 Logical Operators

#These combine multiple conditions.
#There are three:
#and
#or
#not

# AND = Both conditions must be True.

age = 25
salary = 50000

print(age > 18 and salary > 30000)

# OR = At least one condition must be True.
age = 25
salary = 20000
print(age > 18 or salary > 15000)

# age > 18       → True
# salary > 30000 → False
# True OR False → True

# not
# Reverses True/False.

is_active = False
print(not is_active)


#5 Membership Operators
# Very useful when working with lists and strings.

# in
# not in

cities = ["Chennai", "Mumbai", "Delhi"]

print("Chennai" in cities)
print("Kolkata" not in cities)

print("Dubai" in cities)

regions = ["India", "UAE", "UK"]

print("India" in regions)
print("USA" not in regions)


#6 Identity Operators
# is
#is not

#These check whether two variables refer to the same object in memory.

a = [1, 2, 3]
b = a

print(a is b)
print(a is not b)

# == checks whether values are equal.
# is checks whether they are the same object.

#7 Bitwise Operators
#These work at the binary/bit level.

# Bitwise AND: &
# Bitwise OR: |
# Bitwise XOR: ^
# Bitwise NOT: ~
# Bitwise Left Shift: <<
# Bitwise Right Shift: >>

a= 5  # Binary: 0101
b= 3  # Binary: 0011
print(a & b)  # Output: 1
print(a | b)  # Output: 7
print(a ^ b)  # Output: 6
print(~a)     # Output: -6
print(a << 1) # Output: 10
print(a >> 1) # Output: 2



