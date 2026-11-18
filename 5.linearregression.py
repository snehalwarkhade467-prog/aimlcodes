# Linear and Polynomial Regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import *

# Load Dataset
print("Loading California Housing Dataset...")
df = pd.read_csv("california_housing.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())

# Split Dataset
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)

# Linear Regression
print("\nTraining Linear Regression...")
lr = LinearRegression()
lr.fit(X_train, y_train)
pred1 = lr.predict(X_test)

# Polynomial Regression
print("Training Polynomial Regression...")
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

pr = LinearRegression()
pr.fit(X_train_poly, y_train)
pred2 = pr.predict(X_test_poly)

# Model Performance
print("\n" + "=" * 45)
print("          MODEL PERFORMANCE")
print("=" * 45)

for name, pred in [("Linear Regression", pred1),
                   ("Polynomial Regression", pred2)]:
    print("\n" + name + ":")
    print("MSE:", round(mean_squared_error(y_test, pred), 4))
    print("MAE:", round(mean_absolute_error(y_test, pred), 4))
    print("R2 Score:", round(r2_score(y_test, pred), 4))

# Plot Graphs
plt.figure(figsize=(12, 5))

for i, (name, pred) in enumerate([
    ("Linear Regression", pred1),
    ("Polynomial Regression", pred2)
]):
    plt.subplot(1, 2, i + 1)
    plt.scatter(y_test, pred, alpha=0.2)
    plt.title(name)
    plt.xlabel("Actual House Value")
    plt.ylabel("Predicted House Value")
    plt.grid()

plt.tight_layout()
plt.show()

# Compare MAE
if mean_absolute_error(y_test, pred2) < mean_absolute_error(y_test, pred1):
    print("\nPolynomial Regression has a lower MAE.")
else:
    print("\nLinear Regression has a lower MAE.")