import pandas as pd

# Define the path 
file_path = 'D:\\ASSINGMENTS\\MSE800\\Activities\\WEEK04\\FileProcessor\\Data\\sample_text.txt'


# Read all lines
with open(file_path, 'r') as file:
    lines = file.readlines()

# Count the number of lines
line_count = len(lines)

# Join all lines to a single string and count double underscores
content = ''.join(lines)
double_underscore_count = content.count('__')

print(f"Number of lines: {line_count}")
print(f"Number of '__' occurrences: {double_underscore_count}")


