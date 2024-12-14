print("Importing packages")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
print("Imported numpy, pandas, matplotlib, and seaborn")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics
print("Imported modules from sklearn and xgboost packages)")

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
print("Imported warnings and filtered out Deprecation Warnings")

print("Storing Microsoft Stock Data")
df = pd.read_excel('./MSFT_price_data.xlsx', parse_dates=['Date'])

print(f"Viewing the data")
print(df.head())

print(f"Describing the data")
print(df.describe(include="all"))
print(df.dtypes)

print(f"Info on the data")
df.info()

print(f"Cleaning the data")
df[df.columns[1]] = df[df.columns[1]].replace(r'[\$\,]','', regex=True).astype(float)
df[df.columns[3]] = df[df.columns[3]].replace(r'[\$\,]','', regex=True).astype(float)
df[df.columns[4]] = df[df.columns[4]].replace(r'[\$\,]','', regex=True).astype(float)
df[df.columns[5]] = df[df.columns[5]].replace(r'[\$\,]','', regex=True).astype(float)
df.rename(columns={"Close/Last":"Close"}, inplace=True)
print(df.dtypes)

print(f"Viewing cleaned data")
print(df.describe(include="all"))


print(f"The count of nulls in the data are as follows: -\n{pd.isnull(df).sum()}")

print(f"Creating Line Plot for stocks")
plt.figure(figsize=(15,5))
plt.plot(df['Date'],df['Close'])
plt.title('Microsoft Closing Price', fontsize=15)
plt.ylabel('Price in Dollars', fontsize=15)

plt.show()

features = ['Open','High', 'Low', 'Close', 'Volume']

print(f"Creating Sub Plot for stocks")

plt.subplots(figsize=(20,10))

for i, col in enumerate(features):
    sb.displot(df[col], kde=True)

plt.show()