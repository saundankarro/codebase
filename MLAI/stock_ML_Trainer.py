'''
Using Stocks to train a model, using Geeks for Geeks code as basis

'''

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
from sklearn.metrics import ConfusionMatrixDisplay
from xgboost import XGBClassifier
from sklearn import metrics
print("Imported modules from sklearn and xgboost packages)")

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
print("\n\nImported warnings and filtered out Deprecation Warnings")

print("\n\nStoring Microsoft Stock Data")
df = pd.read_excel('./MSFT_price_data.xlsx', parse_dates=['Date'])

print(f"\n\nViewing the data")
print(df.head())

print(f"\n\nDescribing the data")
print(df.describe(include="all"))
print(df.dtypes)

print(f"\n\nInfo on the data")
df.info()

print(f"\n\nCleaning the data")
df[df.columns[1]] = df[df.columns[1]].replace(r'[\$\,]','', regex=True).astype(float)
df[df.columns[3]] = df[df.columns[3]].replace(r'[\$\,]','', regex=True).astype(float)
df[df.columns[4]] = df[df.columns[4]].replace(r'[\$\,]','', regex=True).astype(float)
df[df.columns[5]] = df[df.columns[5]].replace(r'[\$\,]','', regex=True).astype(float)
df.rename(columns={"Close/Last":"Close"}, inplace=True)
print(df.dtypes)

print(f"\nViewing cleaned data")
print(df.describe(include="all"))


print(f"\nThe count of nulls in the data are as follows: -\n{pd.isnull(df).sum()}")

print(f"\n\nCreating Line Plot for stocks")
plt.figure(figsize=(15,5))
plt.plot(df['Date'],df['Close'])
plt.title('Microsoft Closing Price', fontsize=15)
plt.ylabel('Price in Dollars', fontsize=15)

plt.show()

print(f"\nMicrosoft Stock Price has increased by almost 4x in 10 years")

features = ['Open','High', 'Low', 'Close', 'Volume']

print(f"\nCreating Sub Plot for stocks")

plt.subplots(figsize=(20,10))

for i, col in enumerate(features):
    sb.displot(df[col], kde=True)

plt.show()

print(f"\nThe Volume of Microsoft stocks has outliers, which is causing the data to skew towards the right.")

df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

df['Is_Quarter_End'] = np.where(df['Month']%3==0,1,0)

print(f"\nExtracting Quarter end from data")
print(df.head())


print(f"\nAnalyzing the stock prices over time")
data_grouped = df.drop('Date', axis=1).groupby('Year').mean()
plt.subplots(figsize=(20,10))

for i, col in enumerate(['Open','High','Low','Close']):
    plt.subplot(2,2,i+1)
    data_grouped[col].plot.bar()

plt.show()

print(f"As expected, the stock prices for Microsoft has quadrupled in about 10 years")


print(f"\nAnalyzing the stock data, comparing months that are not quarter ends to months that are")
print(df.drop('Date',axis=1).groupby('Is_Quarter_End').mean())
print(f"\nMonths that are quarter ending months (March, June, September, and December) have lower stock prices and higher trade volumes than other months")

df['Open-Close'] = df['Open'] - df['Close']
df['Low-High'] = df['Low'] - df['High']
df['Target'] = np.where(df['Close'].shift(-1) > df['Close'],1,0)

print(f"Adding columns to help train the model. The target column is a signal if we should buy or not.")

print(f"\nAnalying pie graph to determine if target column is balanced")
plt.pie(df['Target'].value_counts().values,
        labels=[0,1], autopct='%1.1f%%') # %1.1f is for how many decimals to highlight on graph. %% at end is to include % sign
plt.show()


plt.figure(figsize=(10,10))


print(f"\nCreating a heat map to determine if there are any highly correlated features to avoid in the learning process of the algorithm")
sb.heatmap(df.drop('Date',axis=1).corr() > 0.9, annot=True, cbar=False)
plt.show()
print(f"As per the heatmap, the Open, Close, High and Low values are expectedly correlated.\nThe heatmap also shows the Open, Close, High, and Low values are highly correlated to the Year.")

print(f"\nStarting to normalize data for later training the model")

features = df[['Open-Close','Low-High','Is_Quarter_End']]
target = df['Target']

scalar = StandardScaler()
features = scalar.fit_transform(features)

X_Train, X_Valid, Y_Train, Y_Valid = train_test_split(
    features, target, test_size=0.1, random_state=2022
)

print(X_Train.shape, X_Valid.shape)

models = [LogisticRegression(), SVC(
    kernel='poly', probability=True), XGBClassifier()
]

for i in range(3):
    models[i].fit(X_Train, Y_Train)

    print(f"{models[i]} :")
    print(f"Training Accuracy: ", metrics.roc_auc_score(
        Y_Train, models[i].predict_proba(X_Train)[:,1]
    ))
    print(f"Validation Accuracy: ", metrics.roc_auc_score(
        Y_Valid, models[i].predict_proba(X_Valid)[:,1]
    ))

print(f"Models have been trained")

ConfusionMatrixDisplay.from_estimator(models[0], X_Valid, Y_Valid)
plt.show()