import random

from lib_fontydatasets import dataset, IMAGE_WIDTH, IMAGE_HEIGHT, chars, nnetResultToChar, scoreNetAccuracy

# lets train the network
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer


# put the dataset into a nnet dataset
print "Reformatting data for neural network..."
ds = SupervisedDataSet( IMAGE_WIDTH * IMAGE_HEIGHT, len(chars))

for row in dataset:
    ds.addSample(row[1], row[2])

print "... Reformatted data for neural network."

print "Constructing and training random networks, will return the best one."

BEST_NETWORK = None
BEST_NETWORK_SCORE = -1
BEST_NETWORK_HIDDEN_SIZE = 0

for _ in range(0, 10):
    
    hiddenSize = random.randint(3, 150)
    net = buildNetwork( IMAGE_WIDTH * IMAGE_HEIGHT, hiddenSize, len(chars), bias=True, hiddenclass=TanhLayer)

    trainer = BackpropTrainer(net, ds, verbose=True)
    trainer.trainUntilConvergence(
        verbose=True,
        trainingData=ds,
        validationData=ds,
        maxEpochs=16)

    score = scoreNetAccuracy(net, dataset)
    if score > BEST_NETWORK_SCORE:
        print "NETWORK BEAT PREVIOUS BEST SCORE WITH: ", score
        print "\tHIDDEN SIZE: ", hiddenSize
        BEST_NETWORK_SCORE = score
        BEST_NETWORK_HIDDEN_SIZE = hiddenSize
        BEST_NETWORK = net

print "DONE TRAINING NETWORK!!!"

net = BEST_NETWORK
print "Best network score was: ", BEST_NETWORK_SCORE
print "Best network hidden size was: ", BEST_NETWORK_HIDDEN_SIZE

print "testing..."

for datum in dataset[0:10]:
    print "expected: ", datum[0], "result: ", nnetResultToChar(net.activate(datum[1]))

print "Accuracy rateing: ", scoreNetAccuracy(net, dataset)

from pybrain.tools.customxml import NetworkWriter
NetworkWriter.writeToFile(net, 'nnet.xml')