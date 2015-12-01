import random

from lib_dataset import nnetResultToChar, scoreNetAccuracy
from lib_fontydatasets import dataset, IMAGE_WIDTH, IMAGE_HEIGHT, chars

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
"""
import threading

                # lrate , hid, lrdecay, momentum, weightdecay
seedParameters = (0.0018, 100, 1.0)

generations = 10

results = [(seedParameters, None)]
for _ in range(0, 10):
    parent = results[0][0]
    results = []
    generation = []
    for _ in range(0, 4):
        lrate = parent[0] + (random.random() - 0.5) * 0.01
        if lrate <= 0.0005:
            lrate = 0.0005
        hid = parent[1] + random.randint(-10,10)
        if hid <= 20 or hid >= 200:
            hid = 100
        lrdecay = parent[2] + (random.random() - 0.5) * 0.1
        if lrdecay > 1:
            lrdecay = 1
        generation.append((lrate, hid, lrdecay))
    print generation


    threads = []
    for child in generation:
        def train():
            lrate = child[0]
            hid = child[1]
            lrdecay = child[2]

            net = buildNetwork( IMAGE_WIDTH * IMAGE_HEIGHT, hid, len(chars), bias=True, hiddenclass=TanhLayer)

            trainer = BackpropTrainer(net, ds, verbose=False, learningrate=lrate, lrdecay=lrdecay)
            trainer.trainUntilConvergence(
                verbose=False,
                trainingData=ds,
                validationData=ds,
                maxEpochs=20)

            results.append((child, scoreNetAccuracy(net, dataset), net))
        threads.append(threading.Thread(target=train, args=[]))
    for thread in threads:
        thread.start()
        thread.join()
    results.sort(key=(lambda x: -x[1]))
    print "winning accuracay in generation ", _, results[0][1]
"""

results = []
for _ in range(0, 10):

    net = buildNetwork( IMAGE_WIDTH * IMAGE_HEIGHT, 100, len(chars), bias=True, hiddenclass=TanhLayer)

    trainer = BackpropTrainer(net, ds, verbose=True, learningrate=0.0018, lrdecay=1)
    trainer.trainUntilConvergence(
        verbose=True,
        trainingData=ds,
        validationData=ds,
        maxEpochs=10)

    results = (scoreNetAccuracy(net, dataset), net)
results.sort(key=(lambda x: -x[0]))
net = results[0][1]




print "testing..."

for datum in dataset[0:10]:
    print "expected: ", datum[0], "result: ", nnetResultToChar(net.activate(datum[1]))

print "Accuracy rateing: ", scoreNetAccuracy(net, dataset)

from pybrain.tools.customxml import NetworkWriter
NetworkWriter.writeToFile(net, 'nnet.xml')