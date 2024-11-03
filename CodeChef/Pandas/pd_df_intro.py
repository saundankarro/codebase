import pandas as pd
import numpy as np

"""
Intro to Data Frames

"""

# Series: Single column of data (e.g., daily temperatures)
temperatures = pd.Series([20, 22, 23, 19, 21], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print("Temperature Series:")
print(temperatures)
print("\nAverage temperature:", temperatures.mean())

# DataFrame: Multiple related columns (e.g., weather data)
weather_data = pd.DataFrame({
    'Temperature': [20, 22, 23, 19, 21],
    'Humidity': [45, 47, 50, 43, 42],
    'WindSpeed': [10, 12, 8, 15, 11]
}, index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])

print("\nWeather DataFrame:")
print(weather_data)
print("\nAverage conditions:")
print(weather_data.mean())

"""
Practice Task 1

Create a DataFrame from a dictionary that represents weather data for a week, including columns for 'Day', 'Temperature', and 'Condition'.

Output the dataframe to the console.

"""

weather_data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'Temperature': [72, 75, 70, 68, 74],
    'Condition': ['Sunny', 'Partly Cloudy', 'Rainy', 'Cloudy', 'Sunny']
}

weather_df = pd.DataFrame(weather_data)

print(weather_df)

"""
Practice Task 2

We have created a DataFrame from a list of lists representing a small gradebook with columns for 
    'Student', 'Subject', and 'Grade'.
Update the code in the IDE to rename the rows with the updated index values provided in the Output below.

"""

gradebook_data = [
    ['Alice', 'Math', 95],
    ['Bob', 'Math', 87],
    ['Charlie', 'Math', 91],
    ['Alice', 'Science', 92],
    ['Bob', 'Science', 88],
    ['Charlie', 'Science', 94]
]

# Update your code below
gradebook_df = pd.DataFrame(gradebook_data, columns=['Student', 'Subject', 'Grade'], index=['ID1','ID2','ID3','ID4','ID5','ID6'])
print(gradebook_df)

"""
Example of Dataframes created from list of dictionaries

"""

# Case 1: All keys are common
data = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]

df = pd.DataFrame(data)
print('Common keys:\n', df)

# Case 2: Missing keys
data1 = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30},  # Missing 'city'
    {'name': 'Charlie', 'city': 'Los Angeles'}  # Missing 'age'
]

df1 = pd.DataFrame(data1)
print('Missing keys:\n', df1)

# Case 3: Extra keys
data2 = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco', 'salary': 75000},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles', 'department': 'Sales'}
]

df2 = pd.DataFrame(data2)
print('Extra keys:\n',df2)


"""
Practice Task 3

We have create a DataFrame with at least 10 rows of student data (Name, Age, Grade). Output the following to the console

The first 3 rows
The last 5 rows
Basic information about the DataFrame

"""

np.random.seed(0)
student_data = pd.DataFrame({
    'Name': [f'Student_{i}' for i in range(1, 11)],
    'Age': np.random.randint(18, 25, 10),
    'Grade': np.random.randint(60, 101, 10)
})

print(student_data.head(3))

print(student_data.tail(5))

print(student_data.info())

"""
Practice Task 4

Display only the 'Name' and 'City' columns
Display the data for the 5th row - i.e. 'Eve'

"""
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston']
})


print(df[['Name','City']])

print(df.iloc[4])

"""
Practice Task 5

Perform the following operations and output the result to the console

Entries where Salary is > 64000
Entries where Salary is 65000 or 70000

"""
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
    'Salary': [50000, 70000, 65000, 60000, 75000]
})

big_slry = df[df['Salary']>60000]
print(big_slry)

spcfc_slry = df[df['Salary'].isin([65000,70000])]
print(spcfc_slry)

"""
Practice Task 6

Output the following to the console

DataFrame corresponding to the 3rd and 4th column and the 3rd, 4th and 5th row using iloc
DataFrame corresponding to the 'Name', 'Age' and 'Salary' columns for 'Charlie' and 'David'

"""
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
    'Salary': [50000, 70000, 65000, 60000, 75000]
})

print(df.iloc[2:,2:])

print(df.loc[[2,3],['Name','Age','Salary']])

"""
Practice Task 7

Perform the following operations and output the updated DataFrame after each operation

Add a 'Family_name' column with the values ['Marks', 'Higgins', None, 'Stark', 'Evans']
Reset everyone's salary to 0
Finally, delete the 'City' column from the dataset

"""
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
    'Salary': [50000, 70000, 65000, 60000, 75000]
})

df['Family_name'] = ['Marks', 'Higgins', None, 'Stark', 'Evans']

print(df)

df['Salary'] *= 0

print(df)

del df['City']

print(df)