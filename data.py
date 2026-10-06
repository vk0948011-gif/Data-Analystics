"""import pandas as pd

data =pd.DataFrame({   
     "Name":  ["Vikram", "sakthivel", "vetrivel"],
      "Age":   ["22", "24", "23"],
    "Marks": ["80", "80", "75"] 

})
Marks = pd.DataFrame(data)
print(Marks)"""

"""
import pandas as pd

data = pd.DataFrame({ 

           "Name":    ["karthik", "Dinesh", "Vikram"],
    "Designation":     ["Supervisor", "Trainee", "Naps"],
         "Salary":     [35000, 20000, 18000]

})
print(data) 
"""
"""import pandas as pd


data = pd.DataFrame({ 

           "Name":    ["karthik", "Dinesh", "Vikram"],
    "Designation":     ["Supervisor", "Trainee", "Naps"],
         "Salary":     [35000, 20000, 18000]

})
print(data[data["Salary"]> 17000]) 
print(data.iloc[[2]]) # print ouput in vertical 
#print(data.iloc[2]) print output in Horizonatal 

print(data.iloc[0:3])"""

import pandas as pd

data = pd.DataFrame({ 


           "Name":    ["karthik", "Dinesh", "Vikram"],
    "Designation":     ["Supervisor", "Trainee", "Naps"],
         "Salary":     [35000, 20000, 18000]
})

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\n" + "="*50 + "\n")

print("DataFrame with mobile_number column:")
df["moblie_number"]= 9361969937, 6379272189, 9585406965
print(df)
