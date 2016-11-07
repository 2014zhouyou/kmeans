import csv
import numpy as np


def normalize(data_set):
    data_matrix = np.matrix(data_set).astype(float)
    max_value = data_matrix.max(0)
    min_value = data_matrix.min(0)
    normalized_data_set = ((data_matrix - min_value) / (max_value - min_value)).tolist()
    return normalized_data_set


class ThreeDimensionalRoadNetworkData:
    data_set = None
    normalized_data_set = None
    max_value = None
    min_value = None

    def __init__(self, file_name):
        self.data_set = list()
        file = open(file_name, 'r')
        reader = csv.reader(file)
        for row in reader:
            self.data_set.append(row)
        self.normalized_data_set = normalize(self.data_set)

    def get_data_set(self):
        return self.normalized_data_set


class IRisData:
    def __init__(self, file_name):
        self.data_set = list()
        file = open(file_name, 'r')
        reader = csv.reader(file)
        for row in reader:
            self.data_set.append(row[0:-1])
        self.normalized_data_set = normalize(self.data_set)

    def get_data_set(self):
        return self.normalized_data_set


class LibraData:
    def __init__(self, file_name):
        self.data_set = list()
        file = open(file_name, 'r')
        reader = csv.reader(file)
        for row in reader:
            self.data_set.append(row)
        self.normalized_data_set = normalize(self.data_set)

    def get_data_set(self):
        return self.normalized_data_set



if __name__ == '__main__':
    # my_data = ThreeDimensionalRoadNetworkData("3D_road_network.csv")
    # print(normalize(my_data.data_set))
    # iris = IRisData('iris/iris.csv')
    # print(iris.get_data_set())
    libra = LibraData('libra/libra.csv')
    print(libra.get_data_set())
