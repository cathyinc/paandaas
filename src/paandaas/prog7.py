def display7():
    code = '''import numpy as np
def centroid(data, k):
    return data[np.random.choice(data.shape[0], k, replace=False)]
def clust(data, centroids):
    distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)
def update(data, clusters, k):
    return np.array([data[clusters == i].mean(axis=0) for i in range(k)])
def kmeans(data, k, max_iterations=100):
    centroids = centroid(data, k)
    for _ in range(max_iterations):
        clusters = clust(data, centroids)
        new_centroids = update(data, clusters, k)
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return centroids, clusters
if __name__ == "__main__":
    num_points = int(input("Enter number of data points: "))
    num_features = int(input("Enter number of features: "))
    k = int(input("Enter number of clusters: "))
    data = []
    print("Enter data points (space-separated values):")
    for _ in range(num_points):
        point = list(map(float, input().split()))
        data.append(point)
    data = np.array(data)
    centroids, clusters = kmeans(data, k)
    print("Final centroids:")
    print(centroids)
    print("Cluster assignments:")
    print(clusters)'''
    print(code)
