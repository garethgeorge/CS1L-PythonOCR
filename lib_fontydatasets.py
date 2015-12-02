# a simple program for training the network on a given set of fonts.
print "Will now attempt to generate the dataset."

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from lib_LetterBBox import fitTo28x28
from lib_dataset import dataset, fontNames, chars, IMAGE_WIDTH, IMAGE_HEIGHT

import random

def map0255to01(list):
    for index in range(0, len(list)):
        list[index] = float(list[index]) / 255.0
    return list

string = " ".join(chars)

from lib_threshold import identifyLetters, makeWhiteOnBlack, matrixToImage, imageToNPMatrix, printMatrix, thresholdMatrix

isFirst = True

def charToOutputs(char):
    arr = [0] * len(chars)
    arr[chars.index(char)] = 1
    return arr

for fontName in fontNames:
    for size in range(20, 28, 2):
        font = ImageFont.truetype(fontName, size)

        img = Image.new("L", (1000, 40), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), string, (255,255,255), font=font)
        img.save(fontName + '.png')

        letters = identifyLetters(img)
        _28x28Images = [(symbol, imageToNPMatrix(fitTo28x28(matrixToImage(letter[1]))), charToOutputs(symbol)) for (symbol, letter) in zip(chars, letters)]
        _28x28Images = [(symbol, image, outputs) for (symbol, image, outputs) in _28x28Images]
        if isFirst:
            isFirst = False
            for (symbol, matrix, outputs) in _28x28Images:
                printMatrix(matrix)
                matrixToImage(matrix).save(fontName + '-' + symbol + '.png')
        datums = [(symbol, map0255to01(list(matrix.flatten())), outputs) for (symbol, matrix, outputs) in _28x28Images]

        for d in datums:
            dataset.append(d)

        

'''
for fontName in fontNames:

    firstOf = True
    
    for size in range(20, 28, 2):
    
        # create the font
        font = ImageFont.truetype(fontName, size)

        for char_index in range(0, len(chars)):

            for repeat in range(0, 1):
                ox = 0
                oy = 0

                char = chars[char_index]

                # create the image
                img = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0))

                # setup the canvas
                draw = ImageDraw.Draw(img)
                tw, th = draw.textsize(char, font=font)

                # draw the text
                draw.text(((IMAGE_WIDTH-tw)*0.5 + ox, (IMAGE_HEIGHT-th)*0.5 + oy), char, (255, 255, 255), font=font)

                # greyify it
                grey = img.convert('L')
                grey = fitTo28x28(grey)

                if firstOf:
                    firstOf = False
                    grey.save(fontName + '.png')

                # make the input
                input = list(grey.getdata())
                map0255to01(input)

                # make the output
                output = [0] * len(chars)
                output[char_index] = 1

                dataset.append((char, input, output))
'''


random.shuffle(dataset)
