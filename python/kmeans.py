import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample dataset
data = pd.DataFrame({
    'x': [1, 2, 3, 8, 9, 10],
    'y': [2, 2.5, 4, 8, 7, 10]
})

# Apply KMeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# Get cluster labels and centroids
data['cluster'] = kmeans.labels_
centroids = kmeans.cluster_centers_

# Plot
plt.scatter(data['x'], data['y'], c=data['cluster'])
plt.scatter(centroids[:,0], centroids[:,1], marker='X')
plt.title("K-Means Clustering")
plt.show()