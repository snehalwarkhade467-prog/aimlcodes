# Logistic Regression and KNN Classification

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import *

# Load Dataset
data = pd.read_csv("Breast cancer dataset.csv")
print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)
print("\nFirst 5 rows:\n", data.head())

# Preprocessing
data = data.drop(columns=["id", "Unnamed: 32"])
X = data.drop("diagnosis", axis=1)
y = data["diagnosis"].map({"M": 1, "B": 0})

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)

# Train Models
lr = LogisticRegression(max_iter=1000)
knn = KNeighborsClassifier(n_neighbors=5)

lr.fit(X_train, y_train)
knn.fit(X_train, y_train)

predictions = [lr.predict(X_test), knn.predict(X_test)]
names = ["Logistic Regression", "K-Nearest Neighbors"]

# Evaluation
print("\n" + "=" * 50)
print("          MODEL PERFORMANCE")
print("=" * 50)

for name, pred in zip(names, predictions):
    print("\n", name)
    print("Accuracy :", round(accuracy_score(y_test, pred), 4))
    print("Precision:", round(precision_score(y_test, pred), 4))
    print("Recall   :", round(recall_score(y_test, pred), 4))
    print("F1 Score :", round(f1_score(y_test, pred), 4))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, pred))

# Plot Confusion Matrices
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

for i, (name, pred) in enumerate(zip(names, predictions)):
    ConfusionMatrixDisplay.from_predictions(
        y_test, pred,
        display_labels=["Benign", "Malignant"],
        cmap="Blues", ax=ax[i]
    )
    ax[i].set_title(name)

plt.tight_layout()
plt.show()

# Compare Models
if accuracy_score(y_test, predictions[0]) > accuracy_score(y_test, predictions[1]):
    print("\nLogistic Regression performs better.")
elif accuracy_score(y_test, predictions[0]) < accuracy_score(y_test, predictions[1]):
    print("\nKNN performs better.")
else:
    print("\nBoth models have equal accuracy.")