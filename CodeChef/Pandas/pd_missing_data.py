'''
Problem 1

Create a function that takes a DataFrame as input and returns the percentage of missing values in each column.
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, np.nan, 8],
                   'C': ['a', 'b', 'c', None]})
                   
# Update your code below this line