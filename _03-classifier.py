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
from lib_dataset import nnetResultToChar, topNResults, chars
import numpy

# first open image
print "Loading image file..."
image = Image.open('./test-text.png')
print "Extracting letters..."

# extract letter data
letters = identifyLetters(image.convert('L'))
# flatten to array inputs and clamp between 0 and 1
letters_processed = [fitTo28x28(matrixToImage(img)) for (pos, img) in letters]

# show us what they look like
for (letter, num) in zip(letters_processed, range(0, len(letters_processed))):
    letter.save('input-' + str(num) + '.png')

# create the inputs for the nnet
nnetInputs = [imageToNPMatrix(fitTo28x28(matrixToImage(img))).flatten() for (pos, img) in letters]

# create the outputs for the nnet
nnetOutputs = [net.activate(input) for input in nnetInputs]

def prePostProcessNnetOutput(nnetOutputs):
    res = []
    for output in nnetOutputs:
        res.append(zip(chars, output))
    return res

# POST PROCESSING
from lib_granny import dictionary_bigrams
print dictionary_bigrams
def postProcess(result):
    final = []
    for cur,next in zip(result[0:-1], result[1:]):
        res = []
        for ac, asc in cur:
            for bc, bsc in next:
                score = dictionary_bigrams[(ac, bc)] * asc * bsc
                res.append((score, ac, bc))
        res.sort(key=lambda x: -x[0])
        final.append(res[0][1])
    return final


#postProcess([[('h', 0.9), ('q', 1)], [('e', 0.6), ('p', 0.9)], [('l', 0.6), ('z', 0.1)]])
pp = postProcess(prePostProcessNnetOutput(nnetOutputs))
print "".join(pp)

# okay now lets apply bigrams to everything i think.




# print "".join(nnetOutputs)

# nnetOutputs = ["(" + ",".join(topNResults(net.activate(input), 3))+")" for input in nnetInputs]
# print "".join(nnetOutputs)