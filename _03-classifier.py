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

from PIL import Image
from lib_threshold import identifyLetters, makeWhiteOnBlack, matrixToImage, imageToNPMatrix, thresholdMatrix
from lib_LetterBBox import fitTo28x28
from lib_dataset import nnetResultToChar
import numpy

# first open image
print "Loading image file..."
image = Image.open('./test-image2.png')
print "Extracting letters..."
# TODO : work on makeWhiteOnBlack implementation
letters = identifyLetters(image.convert('L'))
# flatten to array inputs and clamp between 0 and 1

nnetInputs = [thresholdMatrix(imageToNPMatrix(fitTo28x28(matrixToImage(img)))).flatten() for (pos, img) in letters]
nnetOutputs = [nnetResultToChar(net.activate(input)) for input in nnetInputs]
print "".join(nnetOutputs)