fontNames = ['Helvetica']
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

IMAGE_WIDTH = 28
IMAGE_HEIGHT = 28

dataset = []

def nnetResultToChar(result):
    max_index = 0
    max_value = result[max_index]

    for index in range(0, len(result)):
        if result[index] > max_value:
            max_value = result[index]
            max_index = index
    return chars[max_index]
def topNResults(result, count):
    thingy = zip(result, chars)
    thingy.sort(key=lambda x: -x[0])
    return map(lambda x: x[1], thingy[0:count])

def scoreNetAccuracy(net, ds):
    totalRight = 0.0
    total = 0.0
    for datum in dataset:
        total = total + 1.0
        if nnetResultToChar(net.activate(datum[1])) == datum[0]:
            totalRight = totalRight + 1.0
    return totalRight / total
