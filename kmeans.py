import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

sns.set()

X, y_true = make_blobs(n_samples=300, centers=8, cluster_std=0.20, random_state=0)
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.show()

kmeans = KMeans(n_clusters=8)

kmeans.fit(X)
y_kmeans = kmeans.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_

plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()
