# a simple program for training the network on a given set of fonts.
print "Will now attempt to generate the dataset."

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from lib_LetterBBox import fitTo28x28

import random

IMAGE_WIDTH = 28
IMAGE_HEIGHT = 28

dataset = []

fontNames = ['Arial.ttf' , 'Helvetica']
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def map0255to01(list):
    for index in range(0, len(list)):
        list[index] = float(list[index]) / 255.0

for fontName in fontNames:

    firstOf = True
    
    for size in range(27, 28, 1):
    
        # create the font
        font = ImageFont.truetype(fontName, size)

        for char_index in range(0, len(chars)):

            for repeat in range(0, 4):
                ox = random.random() * 4 - 2
                oy = random.random() * 4 - 2

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

random.shuffle(dataset)

def nnetResultToChar(result):
    max_index = 0
    max_value = result[max_index]

    for index in range(0, len(result)):
        if result[index] > max_value:
            max_value = result[index]
            max_index = index
    return chars[max_index]

def scoreNetAccuracy(net, ds):
    totalRight = 0.0
    total = 0.0
    for datum in dataset:
        total = total + 1.0
        if nnetResultToChar(net.activate(datum[1])) == datum[0]:
            totalRight = totalRight + 1.0
    return totalRight / total
