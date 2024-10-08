import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

# import IPython.display as display
# import io
# import base64

iris = load_iris()
X = iris.data

wcss =[]
for i in range (1,11):
  kmeans = KMeans(n_clusters= i, init ='k-means++',random_state = 42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

plt.figure(figsize=(8,5))
plt.plot(range(1,11), wcss, marker ='o', linestyle ='--', color ='b')
# plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Câu 1: Elbow Method for Optional Optimal K", fontsize=10)
plt.xlabel('Number of cluster')
plt.ylabel('Wcss (Within cluster sum of squares)')
plt.show()