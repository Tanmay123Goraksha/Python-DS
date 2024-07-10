import re

grades = "AAAABBBBCCCAAAA"

# Define the pattern
pattern = r'(A{2,2}|B{2,2}|C{2,2})'

# Find all matches
matches = re.findall(pattern, grades)


print(matches) 


 


