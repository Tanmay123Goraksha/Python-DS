import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 22, 28, 21],
    'Major': ['Math', 'English', 'History', 'Biology']
}

df = pd.DataFrame(data)
print(df)

print(df.loc[2])  # Access row with index 2



df.set_index('Name', inplace=True)
print(df)