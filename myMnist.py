from mnist import MNIST
import numpy as np

#
#  LOADING MNIST DATA SET
#

mnist_path = '/Users/beta/Documents/workspaces-classes/CS1L/project-ocr/mnist'

mndata = MNIST(mnist_path)

def to_nnet_outputs(range):
    return lambda x: [1 if x == y else 0 for y in range]

# scales a list. woot woot.
def scale(factor):
    def f(list):
        return [x * factor for x in list]
    return f
data_training = (lambda d: zip(d[1], map(scale(1.0/255.0), d[0]))) (mndata.load_training())
data_testing = (lambda d: zip(d[1], map(scale(1.0/255.0), d[0]))) (mndata.load_testing())

to_nnet_digit_outputs = to_nnet_outputs(range(0, 10))

data_training = map (lambda x: (x[0], x[1], to_nnet_digit_outputs(x[0])), data_training)
data_testing = map (lambda x: (x[0], x[1], to_nnet_digit_outputs(x[0])), data_training)

np.random.shuffle(data_training)
np.random.shuffle(data_testing)