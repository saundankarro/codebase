import pandas as pd
import numpy as np


'''
Problem 1

Create a new DataFrame containing only students aged 19 or older.
Display the first 3 rows and basic information about this new DataFrame.
'''

# Create the initial DataFrame
data = {
    'Student ID': range(1, 11),
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Age': [18, 19, 18, 20, 19, 18, 20, 19, 18, 20],
    'Math Score': [85, 76, 90, 88, 92, 78, 95, 82, 89, 91],
    'Science Score': [88, 82, 85, 90, 86, 80, 92, 78, 94, 89],
    'English Score': [92, 78, 88, 85, 90, 86, 94, 80, 91, 87]
}

df = pd.DataFrame(data)

# Update your code below this line

students = df[df['Age']>18]
print(students)

print(students.head(3))

print(students.info())

'''
Problem 2


Add a new column - 'Total_score'. This column should contain the total score of any student across all 3 tests.
Display the 'Name' and 'Total_score' columns for students with an total score greater than 240.
'''

data = {
    'Student ID': range(1, 11),
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Age': [18, 19, 18, 20, 19, 18, 20, 19, 18, 20],
    'Math Score': [85, 76, 90, 88, 92, 78, 95, 82, 89, 91],
    'Science Score': [88, 82, 85, 90, 86, 80, 92, 78, 94, 89],
    'English Score': [92, 78, 88, 85, 90, 86, 94, 80, 91, 87]
}

df = pd.DataFrame(data)

df['Total_score'] = df['Math Score'] + df['Science Score'] + df['English Score']

print(df)

print(df.loc[df['Total_score']>240,['Name','Total_score']])

'''
Problem 3

Use iloc to output the DataFrame corresponding to the 3rd, 4th row and the 2nd, 3rd column
Use loc to select and output the Math and Science scores for students David, Frank and Henry
'''


data = {
    'Student ID': range(1, 11),
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Age': [18, 19, 18, 20, 19, 18, 20, 19, 18, 20],
    'Math Score': [85, 76, 90, 88, 92, 78, 95, 82, 89, 91],
    'Science Score': [88, 82, 85, 90, 86, 80, 92, 78, 94, 89],
    'English Score': [92, 78, 88, 85, 90, 86, 94, 80, 91, 87]
}

df = pd.DataFrame(data)

print(df.iloc[2:4,1:3])

print(df.loc[[3,5,7],['Math Score','Science Score']])


'''
Problem 4

Create a new column 'Performance' with values 'Excellent' for total score > 270, 'Good' for total score > 240, and 'Average' for the rest.
Use boolean indexing to display all information about students who performed 'Excellent' in Math (score > 90).
'''