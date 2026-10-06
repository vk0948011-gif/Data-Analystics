i=1 
while i <=4:
    j=1
    while j<=i:        # Change: j <= i (instead of j <= 1)
        print(j,end =" ")
        j+=1
    print()
    i+=1 

i=1 
while i <=5:
    j=1 
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1


def star_pattern(n):

  for i in range(1, n+1):
      for j in range(1, i+1):
          
          print("*", end=" ")
      print()
  return "Mission Completed"
star = star_pattern(10)
print(star)


n=5 
for i in range(n):
    for j in range(n):
        if i== 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
