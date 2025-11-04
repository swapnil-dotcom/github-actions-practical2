print("Extract Data")

import pandas as pd 

data = {
    "Id": [1, 2, 3, 4, 5],
    "Name": ["Swapnil", "Akash", "Sumit", "Pradip", "Rahul"],
    "Age": [25, 28, 23, 28, 24]
}

df = pd.DataFrame(data)
print(df)