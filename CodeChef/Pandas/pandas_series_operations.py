import pandas as pd
import numpy as np

"""
Basic Operations with Series
"""

print(f"\nShowing various operations possible on Pandas Series")

s = pd.Series([1, 2, 3, 3, 5])

print(f"\nPrinting a series:-\n{s}")
print(f"\nAdding 2 to the series:-\n{s + 2}")
print(f"\nMultiplying the series by 2:-\n{s * 2}")
print(f"\nGetting the mean/avg of the Series:-\n{s.mean()}")
print(f"\nGetting the median of the Series:-\n{s.median()}")
print(f"\nGetting the Std Dev of the Series:-\n{s.std()}")


"""
Practice Task 1

Calculate and print the following

The temperature increase if each day was 2 degrees warmer
The weekly average temperature
The difference between each day's temperature and the weekly average

"""

print(f"\nPractice Task 1 - \nCalculate temp if each day was 2 degrees warmer,\nWeekly avg temp,\nDiff between each day's tmep and weekly avg")

temperatures = pd.Series([20, 22, 25, 23, 21, 19, 24],
                         index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])


print(f"Practice Task 1 output:- ")
print(temperatures+2)
print(temperatures.mean())
print(temperatures.std())

"""
Practice Task 2

You are given a series representing monthly sales data for a year. Output the following to the console

Access the sales data for March and September
Get the sales data for the first quarter (first three months)
Find the months with sales greater than the yearly average

"""
monthly_sales = pd.Series([4000, 4500, 5100, 5400, 5800, 6200, 6500, 6300, 5900, 5600, 5200, 4800],
                          index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

print(f"Practice Task 2 output:- ")
print(monthly_sales['Mar'])
print(monthly_sales['Sep'])
print(monthly_sales[:3])

avg_sales = monthly_sales.mean()

high_sales = monthly_sales[monthly_sales > avg_sales]
print(high_sales)


"""
Practice Task 3

Using the gradebook Series:

Add 10 points all scores and output the series
Cap the maximum score at 100 and output the series
Create a new Pandas series - 'grade_summary' - which summarises the count of students in different score ranges.
"""

grades = pd.Series([65, 92, 68, 72, 84], index=['Alice', 'Bob', 'Charlie', 'David', 'Eva'])

print(f"Practice Task 3 output:- ")
grades = grades+10

print(grades)

grades =grades.clip(upper=100)
print(grades)

Low = ((grades < 60).sum())

Mid = (grades.between(60,79).sum())

High = ((grades >=80).sum())

grade_summary = pd.Series([Low,Mid,High], index=["<60","60-79","80-100"])
print(grade_summary)