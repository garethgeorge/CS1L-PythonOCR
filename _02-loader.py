from lib_fontydatasets import dataset, IMAGE_WIDTH, IMAGE_HEIGHT, chars, nnetResultToChar, scoreNetAccuracy

# lets train the network
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer

import random

# lets train the network
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer

from pybrain.tools.customxml import NetworkWriter
from pybrain.tools.customxml import NetworkReader

net = NetworkReader.readFrom('nnet.xml')

print "Loaded network from file."

print "testing..."

for datum in dataset[0:100]:
    print "expected: ", datum[0], "result: ", nnetResultToChar(net.activate(datum[1]))

print "Accuracy rateing: ", scoreNetAccuracy(net, dataset)

from pybrain.tools.customxml import NetworkWriter
NetworkWriter.writeToFile(net, 'nnet.xml')