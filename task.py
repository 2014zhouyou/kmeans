import sys
from clusters import KMeansCluster
from data import ThreeDimensionalRoadNetworkData
from data import IRisData
from data import LibraData


def test_clusters(k):
    # data_set = data.get_data_set()
    data_set = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1],
                [4, 1], [5, 0], [5, 1], [5, 2], [6, 1],
                [9, 1], [10, 0], [10, 1], [10, 2], [10, 1],
                [14, 1], [15, 0], [15, 1], [15, 2], [16, 1],
                [19, 1], [20, 0], [20, 1], [20, 2], [20, 1],
                [24, 1], [25, 0], [25, 1], [25, 2], [26, 1]]
    cluster = KMeansCluster()
    # clusters, centroids = cluster.cluster(data_set[0:10000], k)
    # clusters, centroids = cluster.cluster(data_set, k)
    cluster.set_diameter_threshold(5)
    clusters, centroids = cluster.bisecting_cluster(data_set)
    print(centroids)
    print("in test function:  cluster num = " + str(len(clusters)))
    for cluster in clusters:
        print(cluster)
    sum_sse = KMeansCluster.compute_sse(clusters, centroids)
    print("value k = " + str(k) + ", sse = " + str(sum_sse))


def test_a(data, k_list):
    data_set = data.get_data_set()
    # data_set = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1],
    #             [4, 1], [5, 0], [5, 1], [5, 2], [6, 1],
    #             [9, 1], [10, 0], [10, 1], [10, 2], [10, 1],
    #             [14, 1], [15, 0], [15, 1], [15, 2], [16, 1],
    #             [19, 1], [20, 0], [20, 1], [20, 2], [20, 1],
    #             [24, 1], [25, 0], [25, 1], [25, 2], [26, 1]]
    cluster = KMeansCluster()
    sse_list = list()
    for value in k_list:
        clusters, centroids = cluster.cluster(data_set[0:1000], value)
        sse = KMeansCluster.compute_sse(clusters, centroids)
        sse_list.append(sum(sse))
    best_k = 0
    best_sse = sys.maxsize
    print("for " + type(data).__name__)
    for k, sse in zip(k_list, sse_list):
        print("k = " + str(k) + ", sum_sse = " + str(sse))
        if sse <= best_sse:
            best_k = k
            best_sse = sse
    print("best k = " + str(best_k) + ", best sse = " + str(best_sse))


if __name__ == '__main__':
    # test_clusters(6)
    # my_data = ThreeDimensionalRoadNetworkData('3d-road-network/3D_road_network.csv')
    # test_a(my_data, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    # iris = IRisData('iris/iris.csv')
    # test_a(iris, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    libra = LibraData('libra/libra.csv')
    test_a(libra, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
