"""import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu"]
temperatures = [28, 30, 29, 32]

plt.plot(days, temperatures)
plt.title("Weekly temperatures")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()"""

""""import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.show()

x = [54,20,35,40]

y = [1,2,3,4]

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 85, 90, 95]

plt.hist(marks, bins=5)

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()"""


import matplotlib.pyplot as plt

x =[1,2,3,4,5]
y= [10, 20, 30, 40, 50]

plt.plot(x,y)
plt.show()

# add markers 

months = ["jan", "feb", "mar", "apr", "may"]
sales = [12000, 15000, 30000, 45000, 55000]

plt.plot(months, sales, marker = "*")

plt.title("monthly sales")
plt.xlabel("months")
plt.ylabel("sales")

plt.show()

plt.plot(months, sales, marker = "*")

