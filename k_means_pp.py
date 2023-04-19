import numpy as np
import random

def euclidean_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

def kmeans_pp(points, k, max_iterations=100):
    # Step 1: Choose a random centroid from the dataset
    centroids = [points[random.randint(0, len(points)-1)]]
    
    # Step 2: Choose the remaining k-1 centroids using probability distribution
    for i in range(1, k):
        distances = []
        for point in points:
            min_distance = float('inf')
            for centroid in centroids:
                distance = euclidean_distance(point, centroid)
                if distance < min_distance:
                    min_distance = distance
            distances.append(min_distance**2)
        probabilities = distances / np.sum(distances)
        index = np.random.choice(range(len(points)), p=probabilities)
        centroids.append(points[index])
    
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

centroids, clusters = kmeans_pp(points, 2)
print("Centroids:", centroids)
print("Clusters:", clusters)
