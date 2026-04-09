def display8():
    code = '''import numpy as np
from scipy.spatial.distance import euclidean
def init_clusters(data):
    return [[point] for point in data]
def closest_clusters(clusters):
    min_distance = float('inf')
    closest_pair = (0, 1)
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            centroid_i = np.mean(clusters[i], axis=0)
            centroid_j = np.mean(clusters[j], axis=0)
            distance = euclidean(centroid_i, centroid_j)
            if distance < min_distance:
                min_distance = distance
                closest_pair = (i, j)
    return closest_pair
def merge_clusters(clusters, i, j):
    clusters[i].extend(clusters[j])
    clusters.pop(j)
def cure(data, num_clusters):
    clusters = init_clusters(data)
    while len(clusters) > num_clusters:
        i, j = closest_clusters(clusters)
        merge_clusters(clusters, i, j)
    return clusters
if __name__ == "__main__":
    num_points = int(input("Enter the number of data points: "))
    num_features = int(input("Enter the number of features: "))
    num_clusters = int(input("Enter the number of clusters: "))
    data = []
    print("Enter data points (space-separated values):")
    for _ in range(num_points):
        point = list(map(float, input().split()))
        if len(point) != num_features:
            print("Error: Number of features does not match!")
            exit()
        data.append(point)
    data = np.array(data)
    clusters = cure(data, num_clusters)
    print("\\nFinal Clusters:")
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i+1}: {np.array(cluster)}")'''
    print(code)
