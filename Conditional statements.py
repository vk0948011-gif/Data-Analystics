## conditional statements 

## age= int(input("Enter your age: "))
## if age >= 18:
##    print("You are eligible to vote.")
## else:
##    print("You are not eligible to vote.")


""" marks= int(input("Enter your marks: "))
 if marks >= 90:
    print("Grade A")
 elif marks >= 50:
    print("`Grade B")
elif marks >= 35:
    print("Grade C")    
else:
    print("You have failed the exam.") """

# Write a program to check whether a student is eligible 
# for a scholarship based on their marks, attendance, and extracurricular activities.

""" marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))   
extracurricular = input("Do you participate in extracurricular activities? (y/n): ")

if marks >= 90 and attendance >= 80 and extracurricular == "y":
    print("You are eligible for a scholarship.")
else:
    print("You are not eligible for a scholarship.")"""


## Write a program loan_eligibility (salary, credit_score).

## Rules: Salary >= 50000 or Credit Score >= 700
## → Eligible Otherwise → Not Eligible

""" salary = int(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))

if salary >=40000 or credit_score >= 700:

    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")"""


a=int(input("Enter your 1st number: "))
b=int(input("Enter your 2nd number: "))
c=int(input("Enter your 3rd number: "))
if a>c or b>c:
    print("a is greater")
elif b<c or b<a:
    print("b is lesser")


else:
    print("c is greater")

import matplotlib
print(matplotlib.__version__)