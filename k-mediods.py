import numpy as np
import random

def manhattan_distance(point1, point2):
    return np.sum(np.abs(point1 - point2))

def kmedoids(points, k, max_iterations=100):
    indices = [i for i in range(len(points))]
    medoids = [indices[i] for i in random.sample(indices, k)]

    for iteration in range(max_iterations):
        clusters = [[] for i in range(k)]

        for i, point in enumerate(points):
            distances = [manhattan_distance(point, points[medoid]) for medoid in medoids]
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(i)

        new_medoids = []

        for cluster in clusters:
            total_distance = 0

            for i in cluster:
                for j in cluster:
                    total_distance += manhattan_distance(points[i], points[j])

            min_distance = float("inf")

            for point_index in cluster:
                distance = 0

                for other_point_index in cluster:
                    distance += manhattan_distance(points[point_index], points[other_point_index])

                if distance < min_distance:
                    min_distance = distance
                    new_medoid = point_index

            new_medoids.append(new_medoid)

        if set(medoids) == set(new_medoids):
            break

        medoids = new_medoids

    return medoids, [points[i] for i in medoids], [points[i] for cluster in clusters for i in cluster]

points = np.array([[3, 4], [3, 6], [3, 2], [6, 4], [6, 6], [6, 3]])

medoids, centroids, clusters = kmedoids(points, 2)

print("Medoids:", medoids)
print("Centroids:", centroids)
print("Clusters:", clusters)
