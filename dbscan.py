import numpy as np

def dbscan(points, eps, min_samples):
    n_points = len(points)
    labels = [0] * n_points
    visited = [False] * n_points
    clust_id = 0
    
    for point_idx in range(n_points):
        if visited[point_idx]:
            continue
        visited[point_idx] = True
        neighbors = [i for i in range(n_points) if np.linalg.norm(points[point_idx] - points[i]) <= eps]
        
        if len(neighbors) < min_samples:
            labels[point_idx] = -1
        else:
            clust_id += 1
            labels[point_idx] = clust_id
            for neighbor_idx in neighbors:
                if visited[neighbor_idx]:
                    continue
                visited[neighbor_idx] = True
                neighbor_neighbors = [i for i in range(n_points) if np.linalg.norm(points[neighbor_idx] - points[i]) <= eps]
                if len(neighbor_neighbors) >= min_samples:
                    neighbors.extend(neighbor_neighbors)
                labels[neighbor_idx] = clust_id
                
    clusters = [[] for i in range(clust_id)]
    for i, point in enumerate(points):
        if labels[i] == -1:
            continue
        clusters[labels[i] - 1].append(point)
        
    return clusters

points = np.array([[2, 7],[2, 5],[2, 3],[5, 1],[5, 6],[5, 5]])
clusters = dbscan(points, 2, 2)
print("Clusters:", clusters)
