import numpy as np
from scipy.spatial import distance
from math import *



# create list of numbers
# Create a list of KNN where you can initialize it
# with a list of constructors

class KNN:

    # initialize KNN with a number of points
    def __init__(self, pointsX, targetY):

        # make sure lists are the same size
        if(len(pointsX) == len(targetY)):
            self.pointsX = pointsX
            self.targetY = targetY
        else:
            raise ValueError("Wrong value for merged points")

    def queryKNN(self, numNeighbors, distanceMetric, queryPoint):

        # Querying the classes

        self.distanceList = []
        if distanceMetric == "eucledian":
            for idx, point in enumerate(self.pointsX):
                d = distance.euclidean(point, queryPoint)
                self.distanceList.append(d)
        elif distanceMetric == "manhatten":
            for idx, point in enumerate(self.pointsX):
                d = abs(point[0] - queryPoint[0])+abs(point[1] - queryPoint[1])
                self.distanceList.append(d)

        self.getOrderedList(queryPoint)

        outputVal = 0
        endIdx = 0

        for idx, value in enumerate(self.mergedPoints):

            if idx < numNeighbors:
                outputVal += value[1] # sum all the Ys up
            elif idx >= (numNeighbors): # distance metric to see if you're tied
                if self.mergedPoints[idx + 1]:
                    if(value[2] == self.mergedPoints[idx-1][2]):
                        outputVal += value[1]
                    else:
                        endIdx = idx
                        break

        return outputVal/(endIdx)

    # implement manhatten distance
    def manhattan_distance(x, y):
        return sum(abs(a - b) for a, b in zip(x, y))

    def getOrderedList(self, queryPoint):
        if self.distanceList:
            self.mergedPoints = zip(self.pointsX, self.targetY, self.distanceList)
            self.mergedPoints.sort(key=lambda p: p[2])


if __name__ == '__main__':
    X = [(1,6),(2,4),(3,7),(6,8),(7,1), (8,4)]
    y = [7,8,16,44,50,68]
    queryPoint = (4,2)

    knn = KNN(X, y)
    print knn.queryKNN(1, "eucledian", queryPoint)
    print knn.queryKNN(3, "eucledian", queryPoint)
    print knn.queryKNN(1, "manhatten", queryPoint)
    print knn.queryKNN(3, "manhatten", queryPoint)

