import pandas as pd
import numpy as np


"""
Practice Task 1
Create 3 Pandas series and output them to the console

List of fruits - 'apple', 'banana', 'cherry', 'date'
NumPy array - [0.5, 0.3, 0.8, 0.6]
Dictionary consisting of fruits and their corresponding prices - 'apple': 0.5, 'banana': 0.3, 'cherry': 0.8, 'date': 0.6
"""

print(f"Practice Task 1 - \nCreate 3 Pandas Series (one list of fruits, one numpy array on price, and a dictionary holding fruits and their prices) \nand output to console\n")

fruits = pd.Series(['apple','banana','cherry','date'])

Numarr = pd.Series(np.array([0.5,0.3,0.8,0.6]))

pd_dict = pd.Series(Numarr.values,index=fruits)

print(f"Practice Task 1 output:- ")
print(fruits)
print(Numarr)
print(pd_dict)

print("")

"""
Practice Task 2

We have given you a series of student grades.
Output the scores for Bob and David to the console on separate lines using the index labels.
"""

print(f"\nPractice Task 2 - Given a series of student grades, output scores for Bob and David on separate lines\n")

grades = pd.Series([85, 90, 88, 92, 95], index=['Alice', 'Bob', 'Charlie', 'David', 'Eva'])

print(f"Practice Task 2 output:- ")
print(f"{grades['Bob']}\n{grades['David']}")


"""
Practice Task 3

Create and print the series representing a gradebook for a class of 5 students.
The code in the IDE already contains the scores for the 5 students as a Pandas series.
"""

print(f"\nPractice Task 3 - \nCreate and print gradebook for a class of 5 students\n")

students = pd.Series(['Student_1','Student_2','Student_3','Student_4','Student_5'])

grades = pd.Series([85, 90, 88, 92, 95], index=students )

print(f"Practice Task 3 output:- ")
print(f"{grades}")