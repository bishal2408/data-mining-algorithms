import numpy as np
import random

def euclidean_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

def kmeans(points, k, max_iterations=100):
    centroids = [points[i] for i in random.sample(range(len(points)), k)]
    
    for iteration in range(max_iterations):
        clusters = [[] for i in range(k)]
        
        for point in points:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(point)
        
        for i in range(k):
            centroids[i] = np.mean(clusters[i], axis=0)
    
    return centroids, clusters
    
points = np.array([[2, 7],[2, 5],[2, 3],[5, 1],[5, 6],[5, 5]])
centroids, clusters = kmeans(points, 2)
print("Centroids:", centroids)
print("Clusters:", clusters)
