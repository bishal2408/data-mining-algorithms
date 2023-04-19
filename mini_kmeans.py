import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
data = np.random.rand (500, 2)* 100
mbk = MiniBatchKMeans(n_clusters=5, init="random", batch_size=500)
mbk.fit(data)
centers =  mbk.cluster_centers_
labels = mbk.labels_
                                
print("Cluster Centers:", centers) 
colors= ["g", "r", "b", "y", "m"] 
markers = ["+", "x", "", ".", "d"]
for i in range (len(data)):
       plt.plot(data[i][0], data[i][1], color=colors[labels[i]], marker=markers[labels[i]]) 
plt.scatter(centers [:, 0], centers [:, 1], marker="o", s=50, linewidths=5)
plt.show()