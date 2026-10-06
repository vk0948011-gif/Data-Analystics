def add(a, b):
    print(a + b)
    
add(10, 20)
add(100, 200)

#But this doesn't execute yet.
#we need to call the function to execute it.
#welcome()

#Function with parameters
#Suppose we want to welcome different people.
#mulitple times, we can use a parameter in the function.
#mulitple calls to the function with different names as arguments all given different outputs.
#list calls
#name is the parameter of the function.
#karthikeyan is the argument passed to the function.
#parameter = placeholder 
#Argument = actual value 

def welcome(num):
    print("hello", num)

welcome(50)
welcome(60)
welcome(70)
welcome(80)

#2nd call to the function with different argument.

print("enter your number:")
name=int(input())
welcome(50)   
print("enter your num:")  
name=int(input())   
welcome(60)

#Muliple parameters in a function
def divide(a, b):
    print(a / b)

#call
divide(10, 20) 
divide(358, 518)

#Return statement in a function
#Instead of printing the result, we can return it.

def divide(a, b):
    return a / b
result = divide(10, 20)

print(result)

#return: sends the result back to the place where the function was called.

#EG:
#addition
def calulate_total(m1, m2,m3):
    return  m1 + m2 + m3

# call the function

total = calulate_total(90, 80, 70)
print(total)    

#Percentage 
def calculate_percentage(total):
    return total / 5

percentage = calculate_percentage(total)
print(percentage)

#Funtion with condition.
def check_result(marks):
    if marks >= 80:
        return "pass"
    else:
        return "fail"

result = check_result(90)
print(result)
  
result = check_result(70)
print(result)   
