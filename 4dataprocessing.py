import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#load dataset
df=pd.read_csv("heart.csv")

#print 5 lines
print(df.head())

# 2 data cleaning
df=df.drop_duplicates()

#3.handling missing values

for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col]=df[col].fillna(df[col].mean())
        else:
            df[col]=df[col].fillna(df[col].mode()[0])
    print("Missing Values")
    print(df.isnull().sum())

#4 statistical

print(df.describe())

#5 input output

X=df.drop("target",axis=1)
y=df["target"]

#6 encoding

X=pd.get_dummies(X,drop_first=True,dtype=int)

#7 split into

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#8 fewture scaling

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

print("Training Test:",X_train.shape)
print("testing test:",X_test.shape)

#9 boxplot of cholestrol
plt.figure(figsize=(10,5))
sns.boxplot(x=df["chol"])
plt.title("Boxplot of Cholestrol")
plt.xlabel("chol")
plt.show()

#10 Boxplot of Age

plt.figure(figsize=(10,5))
sns.boxplot(x=df["age"])
plt.title("Boxplot of Age")
plt.xlabel("age")
plt.show()

#11 Histogram Of chol

plt.figure(figsize=(10,5))
plt.hist(df["chol"].dropna(),bins=20,edgecolor="black")
plt.title("Histogram of cholestrol")
plt.xlabel("chol")
plt.ylabel("frequency")
plt.show()

#12 Histogram of age

plt.figure(figsize=(10,5))
plt.hist(df["age"].dropna(),bins=20,edgecolor="black")
plt.title("Histogram of age")
plt.xlabel("age")
plt.ylabel("frequency")
plt.show()