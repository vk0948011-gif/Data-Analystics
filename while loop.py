"""i = 4
while i <=4:
    print(i)
    i += 5

for i in range(1,6):
    if i == 5:
        break
    print(i)"""

"""number = 1
while number <=10:
    if number  % 2 == 0:
        print(number)
    number += 1

sales = [1000, 2000, 3000, 4000]
i =0 
while i < len(sales):
    print(sales[i])
    i += 1

# i represent the position/index.

# while loop to calulate total sales 

i = 0 
total = 0

while i < len(sales):
    total += sales[i]
    i += 1 

print("Total sales:", total)"""

"""reverse = "karthikeyan"
reverse_1 = ""

for i in reverse_1:
    reverse_1 = i + reverse_1
    print(reverse_1)"""

n = int(input("enter the 1st number:"))
n1 = int(input("enter the 2st number:"))
print(n+n1, '\n', n-n1, '\n', n*n1, '\n', n/n1, '\n', n**n1, '\n', n//n1)


# Break -- jump statements
for i in range (1, 10):
    if i == 5:
        break 
    print(i)

for i in range(1, 30, 2):
    if i == 25:
        break
    print(i)

"""# Continue -- jump statements 

for i in range(1,20):
    if i <= 15:
        continue
    print(i)

for i in range(1,20):
    if i >= 15:
        continue
    print(i)

for i in range(1, 20):
    if i == 9 and i==10 and i==11:
        continue
    print(i)  

i = 10

while i > 0:
    if i in (2,6,8):
        continue
    i =-1
    print(i)"""

i = 0
while i >0:
    if i in (2,6,8):
        i = i-1
        continue
    print(i)
    i = i-1

