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


# Let's start with an example and import our graduate admission dataset. First we'll bring in pandas
import pandas as pd
# Then we'll load in our CSV file
df = pd.read_csv('datasets/Admission_Predict.csv', index_col=0)
# And we'll clean up a couple of poorly named columns like we did in a previous lecture
df.columns = [x.lower().strip() for x in df.columns]
# And we'll take a look at the results
df.head()

# a Boolean Series. The resultant Series is indexed where the value of each cell is either True or False 
# depending on whether a student has a chance of admit higher than 0.7
admit_mask=df['chance of admit'] > 0.7

# So, what do you do with the boolean mask once you have formed it? Well, you can just lay it on top of the
# data to "hide" the data you don't want, which is represented by all of the False values. We do this by using
# the .where() function on the original DataFrame.
df.where(admit_mask).head()

# Despite being really handy, where() isn't actually used that often. Instead, the pandas devs
# created a shorthand syntax which combines where() and dropna(), doing both at once. And, in
# typical fashion, the just overloaded the indexing operator to do this!

df[df['chance of admit'] > 0.7].head()

# DataFrame, it now does two things:

# It can be called with a string parameter to project a single column
df["gre score"].head()

# Or you can send it a list of columns as strings
df[["gre score","toefl score"]].head()
# Or you can send it a boolean mask
df[df["gre score"]>320].head()