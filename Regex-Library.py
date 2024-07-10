#Regex Library
import re

grades = "AAAABBBBCCCAAAA"

# Define the pattern
pattern = r'(A{2,2}|B{2,2}|C{2,2})'

# Find all matches
matches = re.findall(pattern, grades)


print(matches) 


for item in re.finditer("(?P<title>[\w]+)(?=\[edit\])",wiki)



# (?P<title>[\w]+): This is a named capturing group (?P<title>). It captures a sequence of one or more (+) word characters ([\w]). Word characters include alphabetic characters, digits, and underscores.

# [\w] matches any word character.
# + quantifier specifies that the previous token ([\w]) must match one or more times.
# (?P<title> defines the start of a named capturing group with the name title.
# (?=\[edit\]): This is a positive lookahead assertion. It specifies a position in the string where what immediately follows is [edit].

# \[edit\] matches the literal string [edit].
# (?= is the start of the lookahead assertion, indicating that what follows should match [edit].
# \] matches the literal ].


 


