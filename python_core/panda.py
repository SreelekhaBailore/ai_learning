import pandas as pd
import numpy as np
#Create using  dictionaries of lists
print("Create using  dictionaries of lists")
df = pd.DataFrame({'columnA': [3,4,5,6], 'columnB': [5,8,9,0]})
print(df)

#Create using  list of dictionaries
print("Create using  list of dictionaries")
df = pd.DataFrame([
    {'columnA': 3, 'columnB': 5},
    {'columnA': 4, 'columnB': 8},
    {'columnA': 5, 'columnB': 9}
])
print(df)

data = {
    'Name': pd.Series(['Alice', 'Bob', 'Charlie']),
    'Age': pd.Series([25, 30, 35]),
    'City': pd.Series(['New York', 'Los Angeles', 'Chicago'])
}
df = pd.DataFrame(data)
print(df)

#Create using  list of lists
print("Create using  list of lists")
df = pd.DataFrame([
    [3,5],
    [4,8],
    [5,9]
], columns=['columnA', 'columnB'])
print(df)

print(np.array(df['columnA']))

#Create using  array
print("Create using  array")
arr = np.array([[3,5],[4,8],[5,9]])
df = pd.DataFrame(arr, columns=['columnA', 'columnB'])
print(df)

#Creating an empty Dataframe
print("Creating an empty Dataframe")
df = pd.DataFrame()
print(df)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
df = pd.DataFrame(matrix, columns=list('ABC'))
print(df)
print(df.columns)

#Creating indexes
print("Creating indexes")
df = pd.DataFrame(matrix, columns=list('ABC'), index=list('XYZ'))
print(df)
print(df.columns)
print(df.shape)

df['D'] = [10,11,12]
print(df)

df['D'] = [0,0,5]
print(df)

df['E'] = 100
print(df)

df['F'] = np.random.rand(3)
print(df)

df['G'] = [[1,2],[3,4],[5,6]]
print(df)

