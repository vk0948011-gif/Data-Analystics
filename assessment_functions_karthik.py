def welcome():
    print("Welcome to Python")

welcome()

# 2.Using the above function, add to values:

def add(a, b):
    print(a + b)    
add(10, 20 )

#3.what is the difference between print() and return inside a function?

def subtract(a, b):
    return a - b

result = subtract(20, 10)

print(result)      

# return returns the value to the caller, while print() outputs the value.
#print() is used to display output.

#4. Identify the type of function.
# This is a user-defined function.  

def display_message():    # user-defined function (def)
    print("Hello Students")   # Bulit -in function (print())

# 5. Identify the type of function.
numbers = [10, 20, 30, 40]

print(len(numbers))  
# Built-in function (len()) # It is also a Mutable data type.

#6. What will be the output?
def calculate_total(price, quantity):
    return price * quantity

laptop = calculate_total(40000, 5)
print(laptop)

#7. Write a function named greet() that prints:

def greet ():
  return "welcome to python programming"
result = greet()

print(result)

#8. Write a function welcome_student() that accepts a student's name and prints:

def welcome_student(name):
  return name 
welcome_student = ("welcome karthikeyan")
  
print(welcome_student)

#9. Write a function add_numbers(a, b) that accepts two numbers and prints their sum.

def add_numbers(a, b):
  return a + b
addition = add_numbers(50, 70)

print(addition)

#10. write a function subtract_number(a,b) that return between different two numbers.

def subtract_numbers(a, b):
  return a - b
subtraction = subtract_numbers(-50, -70)

print(subtraction)

#11.Write a function multiply_numbers(a, b) that returns the multiplication result.

def multiply (a, b):
  return a * b
multiplication =(12 * 24)

print(multiplication)

# Part - B Function with Parameters.
# 12. Write a function calulate_area (length, width) to calulate and return the area of a rectangle.

def calulate_area(length, width):
  return (length * width)
area = calulate_area(40, 7)

print(area)
 
#13. write a function calulate_average (a,b,c) that calulates the average of three numbers.

def calulate_average(k, l, m):
   return k / l / m
average = calulate_average(100, 600, 700)

print(average)

#14. Write a fucntion Calulate_salary (basic_salary, bonus) that returns the total salary.

def calulate_salary(basic_salary, bonus):
  return basic_salary + bonus

total_salary = calulate_salary(14000, 8000)

print(total_salary)

#15. Write a fucntion caluate_discount(price, discount_percentage) the calcualtes the discount amount.

def calulate_discount(price, discount_percentage):
  return price * discount_percentage / 100

discount = calulate_discount(40000, 10)
print(discount)

#Part - 3 Functions + Conditions.

#16. Write a fucntion check_even_odd(number) that checks whether a number is even or odd.

def check_even_odd (number):
  if number % 2 == 0:
    return "Number is an even"
  else: 
    return "Number is an odd"
even_odd = check_even_odd(10)

print(even_odd)

#17. Write a fucntion check_positive_negative(number) that checks whether a number is positive, negative, or zero.

def check_positive_negative(number):
   if number > 0:
      return "That can be positvie number"
   elif number < 0:
      return "That can be negative number"
   else:
    return "That can be Zero"
check = check_positive_negative(80)

print(check)

#18. Write a function checK_pass_fail(marks).

def check_pass_fail(marks):
   if marks > 50:
      return "pass"
   elif marks < 35:
      return "fail"

result = check_pass_fail(58)
print(result)

#19.Write a function find_greater(a, b) that returns the greater number.

def find_greater(a,b):
   if a > b:
      return "Greater"
   else:
      return "Lessthan"
result = find_greater(70,60)

print(result)

#20. Write a function check_age().

def check_age():
  age = int(input("Enter your age:"))
  if age>= 18:
      print("Eligible to vote")
  else:

      print("Not eligible to vote")

check_age()

# PART C -Functions for Data Analytics
#21. Write a function calculate_total_sales(sales1, sales2, sales3) that returns total sales.

def calulate_total_sales(sales1,sales2,sales3):
   return sales1 + sales2 + sales3
sales = calulate_total_sales(15000,20000,30000)

print(sales)

#22. Write a function calculate_profit(sales, cost).

def calualte_profit(sales, cost):
   return sales - cost

profit = calualte_profit(50000, 5000)
print(profit)

#23. Write a function calualte_profit_percentage(sales, cost).

def calulate_profit_percentage(sales, cost):
   return sales - cost % 10
percentage = calulate_profit_percentage(100, 600)

print(percentage)

#24. Write a function calculate_average_sales(total_sales, number_of_orders)

def calulate_average_sales(total_sales, number_of_orders):
   return total_sales / number_of_orders
average = calulate_average_sales(5000, 20)

print(average)

#25.  Write a function calculate_revenue(price, quantity)

def calulate_revenue(price, quantity):
   return price * quantity
revenue = calulate_revenue(500, 15)

print(revenue)

# Part D. Funtions + Multiple conditions

#26. write a function sales_performance(sales)

def sales_performance(sales):
   if sales >=100000:
      return "Excellent"
   elif sales >=50000:
      return "Good"
   elif sales >=25000:
      return "Average"
   else:
      return "poor"

result = sales_performance(60000)
print(sales)

#27. Write a fucntion calulate_grade(marks).

def calulate_grade(mark):
   if mark >= 90:
    return "A"
   elif mark >= 80:
      return "B"
   elif mark >= 70:
      return "c"
   elif mark >= 60:
      return "D"
   else:
      return "E"
marks = int(input("Enter your mark:" ))
result = calulate_grade(marks)   
print(result)

# 28. write a function empolyee_bouns(salary, performance)

def empolyee_bonus(salary, performance):
   if performance >= 90:
      return "20% bonus"
   elif performance >= 75:
      return "10% bonus"
   elif performance >= 50:
      return "5% bouns"
   else:
      return "No bonus"
   
performance = int(input("Enter your performance:" ))
Bonus = empolyee_bonus(20000, 70)
print(Bonus) 
      
#29. Write a funtion loan_eligiblity(salary, credit_score).
 
def loan_eligiblity(salary, credit_score):

   if salary >= 50000 and credit_score >= 700:
      return " eligible for loan"
   else:
      return "Not eligible for loan"      
salary = loan_eligiblity (60000, 750)

print(salary)

#30. Write a function customer_category(total_purchase).

def customer_category(total_purchase):
   if total_purchase >= 100000:
      return "Permium customer"
   elif total_purchase >= 50000:
      return "Gold customer"
   elif total_purchase >=20000:
      return "silver customer"
   else:
      return "Regular customer"

customer = customer_category(20000)
print(customer)









