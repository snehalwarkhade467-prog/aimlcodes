import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Load Dataset
df = pd.read_csv("Mall_Customers.csv")
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
print(df.head())

# Elbow Method
wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, random_state=42, n_init=10)
    wcss.append(km.fit(X).inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# K-Means Clustering
km = KMeans(n_clusters=5, random_state=42, n_init=10)
df['KMeans_Cluster'] = km.fit_predict(X)

print("\nK-Means Cluster Counts:")
print(df['KMeans_Cluster'].value_counts().sort_index())

sns.scatterplot(x=X.iloc[:, 0], y=X.iloc[:, 1],
                hue=df['KMeans_Cluster'], palette='viridis', s=60)
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
            color='red', marker='X', s=200, label='Centroids')
plt.title("K-Means Clustering")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()

# Dendrogram
Z = linkage(X, method='ward')
dendrogram(Z, truncate_mode='lastp', p=30)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()

# Hierarchical Clustering
hc = AgglomerativeClustering(n_clusters=5, linkage='ward')
df['Hierarchical_Cluster'] = hc.fit_predict(X)

print("\nHierarchical Cluster Counts:")
print(df['Hierarchical_Cluster'].value_counts().sort_index())

sns.scatterplot(x=X.iloc[:, 0], y=X.iloc[:, 1],
                hue=df['Hierarchical_Cluster'], palette='viridis', s=60)
plt.title("Hierarchical Clustering")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()

# Cluster Analysis
print("\nCluster Analysis:")
print(df.groupby('KMeans_Cluster')[
    ['Annual Income (k$)', 'Spending Score (1-100)']
].mean().round(2))

print("\nFirst 10 Clustered Records:")
print(df.head(10))