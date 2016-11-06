import random
import math


class KMeansCluster:
    _stop_threshold = 1

    def cluster(self, data_set, clusters_num):
        # select the K initial points
        records_num = len(data_set)
        centroids = self._select_centroids(data_set, clusters_num)
        print("in cluster method: init centroids " + str(centroids))
        while True:
            clusters = list()
            for i in range(0, clusters_num):
                clusters.append([])
            print(clusters)
            count = 0
            for record_id in range(0, records_num):
                count += 1
                print(count)
                distance = [KMeansCluster.compute_distance(data_set[record_id], centroid)
                            for centroid in centroids]
                print("item = " + str(data_set[record_id]) + " distance = " + str(distance))
                cluster_id = distance.index(min(distance))
                print("it belongs to cluster: " + str(cluster_id))
                clusters[cluster_id].append(data_set[record_id])
                for cluster in clusters:
                    print(cluster)
            next_centroids = self._calc_centroids(clusters)
            if self._close_enough(centroids, next_centroids):
                print("clustering finishes!")
                break
            else:
                print("next centroid = " + str(next_centroids))
                centroids = next_centroids
        return [clusters, centroids]

    def _calc_centroids(self, clusters):
        centroids = list()
        for cluster in clusters:
            distances = list()
            for i in range(0, len(cluster)):
                distances.append([sum([KMeansCluster.compute_distance(cluster[i], point)
                                  for point in cluster])])
                print(distances)
            centroids.append(cluster[distances.index(min(distances))])
        return centroids

    def _close_enough(self, centroids, next_centroids):
        distance = [KMeansCluster.compute_distance(centroid, next_centroid)
                    for centroid, next_centroid in zip(centroids, next_centroids)]
        if sum(distance) < self._stop_threshold:
            return True
        else:
            return False

    def _select_centroids(self, data_set, points_num):
        records_num = len(data_set)
        points = list()
        while len(points) < points_num:
            temp = random.randint(0, records_num - 1)
            if data_set[temp] not in points:
                points.append(data_set[temp])
        return points

    @staticmethod
    def compute_distance(x, y):
        # return math.sqrt(sum([(float(a) - float(b)) * (float(a) - float(b)) for a, b in zip(x, y)]))
        return sum([(float(a) - float(b)) * (float(a) - float(b)) for a, b in zip(x, y)])

    @staticmethod
    def compute_sse(clusters, centroids):
        return [sum([KMeansCluster.compute_distance(example, centroid)
                    for example in cluster])
                for centroid, cluster in zip(centroids, clusters)]

