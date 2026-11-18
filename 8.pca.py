# Dimensionality Reduction using PCA

import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import *

# Load Dataset
data = load_digits()
X, y = data.data, data.target

print("Original Dataset Shape:", X.shape)
print("Features Before PCA:", X.shape[1])

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Classification Before PCA
lr = LogisticRegression(max_iter=2000)
lr.fit(X_train, y_train)
pred1 = lr.predict(X_test)

# Apply PCA
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

print("\nFeatures After PCA:", X_train_pca.shape)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Total Explained Variance:", pca.explained_variance_ratio_.sum())

# Classification After PCA
model = LogisticRegression(max_iter=2000)
model.fit(X_train_pca, y_train)
pred2 = model.predict(X_test_pca)

# Performance Comparison
print("\n" + "=" * 50)
print("       CLASSIFICATION PERFORMANCE")
print("=" * 50)

for name, pred in [("Before PCA", pred1), ("After PCA", pred2)]:
    print("\n", name)
    print("Accuracy :", round(accuracy_score(y_test, pred), 4))
    print("Precision:", round(precision_score(y_test, pred, average="weighted"), 4))
    print("Recall   :", round(recall_score(y_test, pred, average="weighted"), 4))
    print("F1-Score :", round(f1_score(y_test, pred, average="weighted"), 4))

# PCA Visualization
plt.figure(figsize=(8, 5))
plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1],
            c=y_train, cmap="viridis")

plt.title("PCA Dimensionality Reduction (64 -> 2)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar(label="Digit Class")
plt.tight_layout()
plt.show()