import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

iris = load_iris()
X = iris.data
Y = iris.target

optimal= 3
kmeans = KMeans(n_clusters= optimal, init ='k-means++',random_state = 42)
y_means = kmeans.fit_predict(X)

pca  = PCA(n_components = 2)

x_pca = pca.fit_transform(X)

color = ['red', 'blue', 'cyan']
# Common Marker Styles
  # 'o': Circle
  # 's': Square
  # '^': Triangle
  # 'D': Diamond
  # 'x': X-mark
marker = ['o', '^', 'D']
for i, color, marker in zip(range(optimal), color, marker):
  plt.scatter(x_pca[y_means == i, 0], x_pca[y_means == i, 1], s = 80, c=color, marker=marker, label =f'Cluster {i+1}')

centroid_pca = pca.transform(kmeans.cluster_centers_)
plt.scatter(centroid_pca[:,0], centroid_pca[:,1], s=120, c='yellow', edgecolors='black', marker='*',label = 'Centroid')

# plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Câu 2: Kmeans clustering (Iris Dataset)", fontsize=12)
plt.xlabel('X', fontsize =12)
plt.ylabel('Y', fontsize =12)
plt.legend()
plt.grid(True)
plt.show()