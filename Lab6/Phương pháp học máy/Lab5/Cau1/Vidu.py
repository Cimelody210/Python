import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 
from sklearn_extra.cluster import KMedoids
import matplotlib.pyplot as plt

# Load Iris dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# Standardize the data
scaler = StandardScaler()
X_scaler = scaler.fit_transform(X)

# Define the number of clusters
n_cluster = 3

# Apply K-Medoids clustering
kmedoids = KMedoids(n_clusters=n_cluster, metric='euclidean', method='pam', random_state=42)
kmedoids.fit(X_scaler)

# Get the labels and medoid indices
label = kmedoids.labels_
medoid_indices = kmedoids.medoid_indices_
center = X_scaler[medoid_indices]

# Reduce dimensionality using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaler)
centers_pca = pca.transform(center)

# Plot the clusters
plt.figure(figsize=(8,6))
for i in range(n_cluster):
    plt.scatter(X_pca[label == i, 0], X_pca[label == i, 1], label=f'Cluster {i+1}')
plt.scatter(centers_pca[:, 0], centers_pca[:, 1], marker='x', s=100, label='Centers')

# Set titles and labels
plt.title("K-Medoids Clustering on Iris Dataset with PCA (2D Projection)", fontsize=12)
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()
