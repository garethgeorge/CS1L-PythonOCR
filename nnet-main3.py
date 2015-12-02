import cPickle
from pybrain.tools.customxml import NetworkWriter


print "Loading MNIST data ..."
from myMnist import data_training
from myMnist import data_testing
print len(data_training), len(data_testing)
print "... Loaded MNIST data"


from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer


ds = SupervisedDataSet( 28 ** 2, 10)

for row in data_training:
    ds.addSample(row[1], row[2])

net = buildNetwork(28 ** 2, 35, 10, bias=True, hiddenclass=TanhLayer)

trainer = BackpropTrainer(net, ds)

def outputsToNumber(outputs):
    max = outputs[0]
    value = 0
    for x in range(0, 10):
        if outputs[x] > max:
            max = outputs[x]
            value = x
    return value

print "Beginning a training pass..."
for _ in range(0, 5):
    print trainer.train()

for thing in data_training[0:20]:
    print "expected label: ", thing[0], "nnet label: ", outputsToNumber(net.activate(thing[1]))

fileObject = open('trainedNetwork', 'w')
cPickle.dump(net, fileObject)
fileObject.close()

NetworkWriter.writeToFile(net, 'nnet.xml')
