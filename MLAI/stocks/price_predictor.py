'''
Stock Price Predictor via Machine Learning, using Medium's code as base
'''
print(f"Importing libraries")
import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

print(f"Libraries Imported")
ticker = 'MSFT'

print(f"Pulling Microsoft stock data from Yahoo Finance")
# Multi Level Index is True by default. Setting as false allows iloc to work when predicting future gain
data = yf.download(ticker, multi_level_index=False)
print(f"Microsoft Stock data has been pulled.\n")
print(data.head())

print(f"\n{data.info()}")

print(f"\nCalculating Moving Averages")
data['MA_10'] = data['Close'].rolling(window=10).mean()
data['MA_50'] = data['Close'].rolling(window=50).mean()
print(f"Created Moving Average columns: \n", data.head(20))

data = data.dropna()

# Defining features and target
X = data[['Close','MA_10','MA_50']]
Y = data['Close'].shift(-1).dropna()
X = X[:-1]

print(f"Splitting the data into 2: Training and Testing")
# Splitting the data into training and testing sets
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y, test_size=0.2, random_state=42)

print(f"Initializing and Training Linear Regression Model")
model = LinearRegression()
model.fit(X_Train, Y_Train)

print(f"Making Predictions")
predictions = model.predict(X_Test)

print(f"Evaluating the model")
mse = mean_squared_error(Y_Test, predictions)
print(f"Mean Squared Error:- {mse}")

r2 = r2_score(Y_Test, predictions)
print(f"R² Score: {r2}")

plt.figure(figsize =(14,7))
plt.plot(Y_Test.index, Y_Test.values, label='Actual Price')
plt.plot(Y_Test.index, predictions, label='Predicted Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Actual vs. Predicted Stock Prices')
plt.legend()
plt.show()

init_bal = 10000 # Starting balance in USD
bal = init_bal
position = 0 # Number of shares

for i in range(len(X_Test)):
    current_price = X_Test.iloc[i]['Close']
    predicted_price = predictions[i]

    # print(f"current price: {current_price}")
    # print(f"Predicted price: {predicted_price}")

    if predicted_price > current_price and bal >= current_price:
        # Buy stock
        shares_to_buy = int(bal // current_price) # Buy whole shares only
        if shares_to_buy > 0:
            position += shares_to_buy
            bal -= shares_to_buy *  current_price
            print(f"Buying {shares_to_buy} shares at {current_price:.2f}")

        elif predicted_price < current_price and position > 0:
            # Sell Stock
            bal += position * current_price
            print(f"Selling {position} at {current_price:.2f}")
            position = 0

fin_bal = bal + (position*X_Test.iloc[-1]['Close'])
profit = fin_bal - init_bal
print(f"Final balance: {fin_bal:.2f}")
print(f"Profit:- {profit}")