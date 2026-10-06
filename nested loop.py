
for i in range (1):
    for j in range (1):
        print("karthikeyan")
        print("dinesh")

for i in range(1, 6):
    for j in range(1, i + 1):

        print("*", end="")
    print()

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1, 5):
    print(str(i) * i)

#Multipliation Table.
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()

#palinedrome program 
def is_palindrome_number(n):
    n = str(n)
    return n == n[::-1]

num = int(input("Enter a number: "))
if is_palindrome_number(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

for i in range(3):
    for j in range(2):
        print(i, j)

#Nested loops with lists suppose:

departments = ["sales", "HR", "ITI"]
employees = ["A", "B"]

for department in departments:
    for employee in employees:
        print(department, employee)


for i in range(1,6):
    for j in range(1,6):
        if i == j:
            print(i,j)

i=1 
while i <=4:
    j=1
    while j<=i:        # Change: j <= i (instead of j <= 1)
        print(j,end =" ")
        j+=1
    print()
    i+=1 