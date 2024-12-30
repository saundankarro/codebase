import numpy as np
import pandas as pd
from scipy.stats import mode
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# %matplotlib inline

print(f"Reading Training Data")
path = "dataset/Training.csv"
data = pd.read_csv(path).dropna(axis=1)

print(f"Counting disease prognoses.")
disease_counts = data["prognosis"].value_counts()

print(f"Creating barplot on Count of disease prognoses")
temp_df = pd.DataFrame({
    "Disease": disease_counts.index,
    "Counts": disease_counts.values
})

plt.figure(figsize=(18,8))
sns.barplot(x="Disease", y="Counts", data=temp_df)
plt.xticks(rotation=90)
plt.show()

print(f"Encoding prognosis to numerical value to help train machine learning model")
encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

X = data.iloc[:,:-1]
Y = data.iloc[:,-1]
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.2, random_state=24)

print(f"Training data for X: {X_Train.shape}.\nTraining data for Y: {Y_Train.shape}")
print(f"Testing data for X: {X_Test.shape}.\nTesting data for Y: {Y_Test.shape}")

def cv_scoring(estimator, X, Y):
    return accuracy_score(Y, estimator.predict(X))

models = {
    "SVC":SVC(),
    "Gaussian NB": GaussianNB(),
    "Random Forest": RandomForestClassifier(random_state=18)
}

for model in models:
    nm = models[model]
    scores = cross_val_score(nm, X, Y, cv=10,
                             n_jobs=1,
                             scoring=cv_scoring)
    
    print("=="*30)
    print(model)
    print(f"Scores:- {scores}")
    print(f"Mean Scure:- {np.mean(scores)}")