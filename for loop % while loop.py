"""for i in range(5):
    print("Hello")"""


for i in range(4):
    print("Karthikeyan")

"""for k in "dinesh":
    print(k,end="")"""

# we don't use i inside the loop. we only need the loop to repeat 5 times. 

# Loop = Repeat a task automatically.

for i in range(5):
    print(i)

#FOR LOOP ###
# used when we want to iterate over a sequence or 
# when we generally know the number/range of iteration.

### range(stop)---> range(5)--> 0 1 2 3 4
# range(start--> stop--->) --> range(1, 6) --> 1 2 3 4 5

# range(start, stop, step) ---> range(1, 10, 2)-->1 3 5 7 9 

#here,
#  1 starting value 
#  10 stopping value
#  2 increment value

# print even numbers
for i in range(2, 30, 2):
    print(i)

#print odd numbers
 
for i in range (1, 25, 2):
    print(i)

for i in ("laptop"):
    print(i)

def even (number):
    for i in range (11, number,2):
        print(i)
even(20)

def odd (number):
    for i in range(2, number, 2):
        print(i)
odd(30)

"""n=int(input("Enter the Number:"))
for i in range(80,n,-5):
    print(i)"""

## Loop Through a list ##
sales= [1000, 2000, 3000, 4000]
for sale in sales:
    print(sale)

#Loop + condition 
#Operators + Condition + Loops

sales = [1500, 2000, 3000, 4000, 5000]
for sale in sales:
    if sale > 3000:
        print(sale)

# calulate Total using a Loop
# Suppose:
sales = [1000 , 2000, 3000, 4000]
total = 0

for sale in sales:
    total = total + sale

print(total)

fruits = ['apple', 'banana', 'mango', 'grapes']
for fruit in fruits:
    print("i like:", fruit)

     
