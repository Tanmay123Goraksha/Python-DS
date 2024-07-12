import pandas as pd

students = ['Alice', 'Jack', 'Molly', 'Harry']

students_data1 = [('Alice1', '1'), ('Alice2', '2'), ('Alice3', '3'), ('Alice4', '4')]

students_data2 = {'Alice1': '1', 'Alice2': '2', 'Alice3': '3', 'Alice4': '4'}

# Creating Pandas Series from different data structures
print(pd.Series(students))      # Series from list
print(pd.Series(dict(students_data1)))  # Series from list of tuples
print(pd.Series(students_data2))  # Series from dictionary

# Accessing elements in a Series
s = pd.Series(students_data2)
print(s.iloc[2])  # Accessing by integer position (iloc)
print(s.loc['Alice2'])  # Accessing by label (loc)

# Creating a DataFrame (assuming you have records defined somewhere)
# Example of DataFrame creation
records = [{'Name': 'Alice', 'Age': 25, 'Grade': 'A'},
           {'Name': 'Jack', 'Age': 24, 'Grade': 'B'},
           {'Name': 'Molly', 'Age': 27, 'Grade': 'A'},
           {'Name': 'Harry', 'Age': 23, 'Grade': 'C'}]

df = pd.DataFrame(records, index=['school1', 'school2', 'school3', 'school4'])

print(df.head())  # Printing the first few rows of the DataFrame

#https://github.com/dbabichenko/python_for_data_and_analytics
