import cPickle
from pybrain.tools.customxml import NetworkWriter
from pybrain.tools.customxml import NetworkReader


from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer

net = NetworkReader.readFrom('nnet.xml')

def outputsToNumber(outputs):
    max = outputs[0]
    value = 0
    for x in range(0, 10):
        if outputs[x] > max:
            max = outputs[x]
            value = x
    return value

for mod in net.modules:
    print("Module:", mod.name)
    if mod.paramdim > 0:
        print("--nparameters: ", len(mod.params))
        print("--parameters:", mod.params)
    for conn in net.connections[mod]:
        print("-connection to", conn.outmod.name)
        if conn.paramdim > 0:
            print("- nparameters", len(conn.params))
            print("- parameters", conn.params)
    if hasattr(net, "recurrentConns"):
        print("Recurrent connections")
        for conn in net.recurrentConns:
            print("-", conn.inmod.name, " to", conn.outmod.name)
            if conn.paramdim > 0:
                print("- parameters", conn.params)

print "Loading MNIST data ..."
from myMnist import data_training
from myMnist import data_testing
print len(data_training), len(data_testing)
print "... Loaded MNIST data"


for thing in data_testing[0:20]:
    print "expected label: ", thing[0], "nnet label: ", outputsToNumber(net.activate(thing[1]))
