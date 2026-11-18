# Advanced Machine Learning and Model Optimization

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load Dataset
data = pd.read_csv("Breast cancer dataset.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)

# Preprocessing
data = data.drop(columns=["id", "Unnamed: 32"], errors="ignore")
X = data.drop("diagnosis", axis=1)
y = data["diagnosis"].map({"M": 1, "B": 0})

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Define Models
models = {
    "SVM": make_pipeline(StandardScaler(), SVC()),
    "Random Forest": RandomForestClassifier(random_state=42),
    "AdaBoost": AdaBoostClassifier(random_state=42)
}

# Grid Search Parameters
params = {
    "SVM": {"svc__C": [0.1, 1, 10],
            "svc__kernel": ["linear", "rbf"]},

    "Random Forest": {"n_estimators": [50, 100],
                      "max_depth": [None, 5, 10]},

    "AdaBoost": {"n_estimators": [50, 100],
                 "learning_rate": [0.5, 1.0]}
}

# Performance Evaluation
print("\n========== MODEL PERFORMANCE ==========")

for name, model in models.items():

    # Before Optimization
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print("\n", name, "- Before Optimization")
    print("Accuracy :", round(accuracy_score(y_test, pred), 4))
    print("Precision:", round(precision_score(y_test, pred), 4))
    print("Recall   :", round(recall_score(y_test, pred), 4))
    print("F1-Score :", round(f1_score(y_test, pred), 4))

    # Cross Validation
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print("Cross Validation:", round(scores.mean(), 4))

    # Grid Search Optimization
    grid = GridSearchCV(model, params[name], cv=5, scoring="accuracy")
    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_
    pred = best_model.predict(X_test)

    print("\n", name, "- After Optimization")
    print("Best Parameters:", grid.best_params_)
    print("Accuracy :", round(accuracy_score(y_test, pred), 4))
    print("Precision:", round(precision_score(y_test, pred), 4))
    print("Recall   :", round(recall_score(y_test, pred), 4))
    print("F1-Score :", round(f1_score(y_test, pred), 4))