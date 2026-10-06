"""i=1 
while i >=i:
    print(i)
    i=i+1"""

"""numbers = int(input("enter your numbers:"))
while numbers >-15:
    print(numbers)
    numbers -= 1"""

"""numbers = int(input("enter your number:"))
while numbers >= numbers:
    print(numbers)
    numbers -= 1"""

name = "karthikeyan" 
i=0
while i < len(name):
    print(name[i])
    i += 1

numbers = [10, 20, 30, 40]
i = 0 
total = 0

"""while i < len(numbers):
    total += numbers[i]
    i+=1 
print("sum=", total)"""

num = int(input("enter the number:"))
while num >= 10:

    if num > 0:
        print("Positive Number")
    else:
        print("Negative Number")

    break


while i != "1234":
    i = input("enter the password:")

    if i == "1234":
        print("Correct password")
    else:
        print("Wrong password")