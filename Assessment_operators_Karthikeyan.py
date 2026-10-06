# Part - A Arithmetic operators 
# 1. Addition 
#Write a Python program to accept two numbers and calculate their sum using the + operator.
a=10
b=20
print(a+b) # ouptut ---> 30

#2. Basic Arithmetic 
a=10
b=20

print(a+b) #ouptut ---> 30
print(a-b) #ouptut ---> -10
print(a*b) #ouptut ---> 200
print(a/b) #output ---> 0.5

#Using two numbers or mulitple numbers.
#3. Moduls 
#Write a program to accept two number and calulate the modules using the % operator.

a=10
b=5
print(a % b) #ouptut ---> o

# 4. Floor Divison 
#Write a program to accept two numbers and calculate the floor division using the // operator.
a=10
b=5
print(a // b) 

#5. Write a program to accept two numbers and calculate the exponentiation using the ** operator.

a=10
b=20
print(a ** b) # output ---> 100000000000000000000

#6. Average Order Value
#Write a program to accept total sales and total orders and calculate the average order value using the / operator.

def calulate_average_sales(total_sales, number_of_orders):
   return total_sales / number_of_orders
average = calulate_average_sales(5000, 20)
 
print(average) # output ---> 250.0  

#7. Average Revenue per Customer 
#Write a program to accept total revenue and total customers and calculate the average revenue per customer using the // operator.

def calulate_average_revenue(total_revenue, total_customer):
   return total_revenue // total_customer
Revenue = calulate_average_revenue(50000, 50 )
print(Revenue) # ouptut ---> 1000

#7. Assignment Operators
# Write a program to demonstrate the use of assignment operators (+=, -=, *=, /=)
x=10
print("Enter the value:", x)
x += 5
print(" += 5:", x) #output ---> 5:15

x -= 3
print(" -= 3:", x) #output ---> 3:12

x *= 2
print(" *= 2:", x) #output ---> 2:24

x /= 4
print(" /= 4:", x) #ouptu ---> 4:6.0

# 8. Find the Reminder
#Write a program to find the reminder when 25 is divided by 4 using %.

a=25
b=4

reminder = a % b
print(reminder)

#Floor division 
#Write a program to perform floor division of 25 by 4 using //.

a=25
b=4
floor_division = a // b
print(floor_division)

#10. calulate Average A sutdent has marks.

maths = 80
science = 75
english = 90

average = (maths + science + english) / 3
print(average)

# 11. calulate Average 
#write a program to calulate the average of three numbers using the / operator.
a=20
b=30
c=50

average = (a + b + c) / 3 
print(average)

#12 calulate discount

price = 5000
discount = 10

discount = price * discount / 100
print(discount)

#13. calulate Final price 
#Write a program to calulate the final price after discount.

price = 4000
discount = 10

final_price = price - (price * discount / 100)
print (final_price)

#14. predict the output.
# what will be output?

x = 10

x += 8
x -= 10
x *= 4
print(x) 

# 15. Comparison Operators
# Write a program to check whether:

a=10
b=5

print(a > b)
print(a < b)

#16. Write a program to check whether two numbers are equal using ==.

a=10
b=5

print(a == b)


#17. Write a program to check whether two numbers are not equal using !=.

a=10
b=10

print(a != b)

#18.  Write a program to check whether 10 is greater than or equal to 5 using >=.

a=10
b=5

print(a >= b)

#19. Write a program to check whether 10 is less than or equal to 5 using <=.

a=10
b=5
print(a <= b)


#20. Write a program to check whether 10 is greater than 5 and 10 is less than 20 using the and operator.

a=10
b=5
c=20

print(a > b and a < c)


#21. Write a program to check whether 10 is greater than 5 or 10 is less than 5 using the or operator.

a=10
b=5
c=5

print(a > b or a < c)

#22. Write a program to check whether 10 is not equal to 5 using the not operator.

a=10
b=5

print(not (a != b))


#23. Write a program to check whether a student passed.

maths=70
science=80
social_science=90
english=60
tamil=75

if (maths >= 35 and science >= 35 and social_science >= 35 and english >= 35 and tamil >= 35):
    
    print("The student has passed.")
else:
    print("The student has failed.")


#24. Write a program to check whether a student failed.

maths=30
science=40
social_science=56
english=68
tamil=45

if (maths >= 35 and science >= 35 and social_science >= 35 and english >= 35 and tamil >= 35):
    
    print("The student has passed.")
else:
    print("The student has failed.")

#25. Write a program to check whether a student is eligible for a scholarship.

Total_marks_obtained= int(input("Enter the total marks obtained by the student: "))
Attendance_pct= int(input("Enter the attendance percentage of the student: "))
Annual_family_income= int(input("Enter the Annual family income of the student: "))

avg_marks = Total_marks_obtained / 5

if avg_marks >= 75 and Attendance_pct >= 80 and Annual_family_income <= 200000:
    
    print(" eligible for a scholarship.")
else:
    print("not eligible for a scholarship.")


#26. Write a program to check whether a student is eligible for a scholarship based on their marks.


maths=70
science=80
social_science=90
english=60
tamil=75

average_marks = (maths + science + social_science + english + tamil) / 5

if average_marks >= 75:
    
    print("eligible for a scholarship.")
else:
    print("not eligible for a scholarship.")

    

#27. Write a program to check whether a student is eligible for a scholarship based on their marks and attendance.

maths=55
science=80
social_science=95
english=60
tamil=65
attendance_pct= 70

average_marks = (maths + science + social_science + english + tamil) / 5


if average_marks >= 75 and attendance_pct >= 80: 
    
    print(" eligible for a scholarship.")
else:
    print("not eligible for a scholarship.")


#28. Write a program to check whether a student is eligible for a scholarship based on their marks, attendance, and extracurricular activities.

maths=70
science=80
social_science=90
english=60
tamil=75
attendance_pct= 85
extracurricular_activities = ["Football", "Carrom", "cricket"]

average_marks = (maths + science + social_science + english + tamil) / 5


if average_marks >= 75 and attendance_pct >= 80 and extracurricular_activities:
    
    print("eligible for a scholarship.")
else:
    print("not eligible for a scholarship.")









