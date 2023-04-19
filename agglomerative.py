import numpy as np
import scipy.cluster.hierarchy as hac


def agglomerative_clustering(points, k):
    distances = np.array([[np.linalg.norm(point1 - point2) for point2 in points] for point1 in
                          points])
    linkage = hac.linkage(distances, method="single")
    labels = hac.fcluster(linkage, k, criterion="maxclust")
    clusters = [[] for i in range(k)]
    for i, label in enumerate(labels):
        clusters[label - 1].append(points[i])
    return clusters


points = np.array([[3, 4], [3, 6], [3, 2], [6, 4], [6, 6], [6, 3]])

clusters = agglomerative_clustering(points, 2)
print("Clusters:", clusters)