import pandas as pd
import numpy as np

#by dictionary
df =pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 40, 45],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})
print(df)

#by nested list
df =pd.DataFrame(
     [['Alice',25, 'New York'],['Alice',30, 'Los Angeles'],['Alice',35, 'Chicago'],['Alice',40, 'Houston'],['Alice',45, 'Phoenix']],
     columns=['name', 'age', 'city']
)
print(df)

data = np.array([['Alice',25, 'New York'],['Alice',30, 'Los Angeles'],['Alice',35, 'Chicago'],
                ['Alice',40, 'Houston'],['Alice',45, 'Phoenix']])
col = ['name', 'age', 'city']
df = pd.DataFrame(data, columns=col)
print(df)