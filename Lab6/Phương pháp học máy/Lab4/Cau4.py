import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from sklearn.datasets import load_iris, load_digits
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

digit = load_digits()
X = digit.data
Y = digit.target
class_names =[str(i) for i in range (10)]

pca  = PCA(n_components = 2)
x_pca = pca.fit_transform(X)

optimal= 3
kmeans = KMeans(n_clusters= optimal, init ='k-means++',random_state = 42)
y_means = kmeans.fit_predict(X)

color = plt.get_cmap('tab10').colors
plt.figure(figsize =(10,8))
centroid = kmeans.cluster_centers_
centroid_pca = pca.transform(centroid)
scatter = plt.scatter(centroid_pca[:,0], centroid_pca[:,1], s=120, alpha = 0.75, marker ='x', label = 'Data point')

handle, labels = scatter.legend_elements()

for i in range(len(centroid)):
  handle.append(Line2D([0],[0], marker= 'x', markeredgecolor='red', markersize=10,  label =f'Centroid{i}'))
plt.legend(handles = handle, labels = labels, title ='Cluster and Centroid', loc ='best')

for i , class_names in enumerate(class_names):
  plt.scatter([],[], c= color[i], s=50, label= class_names)
plt.legend(handles = handle, labels = labels, title ='Cluster and Centroid', loc ='best')

plt.title("Câu 4: K-Means clustering on Digit Dataset PCA reduced ", fontsize=12)
plt.xlabel('PCA 1', fontsize =12)
plt.ylabel('PCA 2', fontsize =12)
plt.grid(True)
plt.show()