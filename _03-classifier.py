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

print "Loading neural network... "
net = NetworkReader.readFrom('nnet.xml')
print "... Loaded network from file"


for datum in dataset[0:100]:
    print "expected: ", datum[0], "result: ", nnetResultToChar(net.activate(datum[1]))

from pybrain.tools.customxml import NetworkWriter
NetworkWriter.writeToFile(net, 'nnet.xml')