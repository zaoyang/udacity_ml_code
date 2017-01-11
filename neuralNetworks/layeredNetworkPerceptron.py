import numpy as np


class LayeredNetwork:


    # Two hidden layers of multi layer network
    def calculateTwoHiddenLayers(self, input, hiddenLayers, outputLayer):


        inputResultArr = []
        for idx, hiddenLayer in enumerate(hiddenLayers):
            a = np.dot(input,hiddenLayer)
            inputResultArr.append(a)

        # TODO check if the inputResult Arr is the same as the outputLayer
        result = np.dot(inputResultArr, outputLayer)

        return result




def main():
    layerNetwork = LayeredNetwork()
    result = layerNetwork.calculateTwoHiddenLayers([1,2,3],[[1,1,-5],[3,-4,2]],[2,-1])

    result1 = layerNetwork.calculateTwoHiddenLayers([1, 0], [[3,2], [-1,4],[3,-5]], [1,2,-1])
    print "Result1 X dot product stuff ", result1


    result1 = layerNetwork.calculateTwoHiddenLayers([1, 0], [[3, 2], [-1, 4], [3, -5]], [1, 2, -1])
    print "Result1 X dot product stuff ", result1

if __name__ == "__main__":
    main()