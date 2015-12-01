import numpy
from PIL import Image

def printMatrix(image):
    for row in image:
        for col in row:
            if col != 0:
                if col < 10:
                    print int(col),
                else:
                    print ">",
            else:
                print " ",
        print ""

def matrixToImage(matrix):
    im = Image.new("L", (matrix.shape[1], matrix.shape[0]))
    im.putdata(matrix.flatten())
    return im


def imageToNPMatrix(image):
    (width, height) = image.size
    imdata = list(image.getdata())

    mat = numpy.zeros(shape=(height,width))
    for x in range(0, width):
        for y in range(0, height):
            mat[y][x] = image.getpixel((x, y))
    return mat

def makeWhiteOnBlack(image):
    thresholdedImage = image.point(lambda x: 0 if x < 128 else 255, '1')

    imdata = list(thresholdedImage.getdata())

    def countWhite(list):
        c = 0
        for x in list:
            if x > 128:
                c = c + 1
        return c
    def invert(list):
        return [255 - x for x in list]

    # force it to white on black
    print countWhite(imdata), len(imdata)
    if countWhite(imdata) > len(imdata) * 0.5:
        imdata = invert(imdata)

    thresholdedImage = Image.new(thresholdedImage.mode, thresholdedImage.size)
    thresholdedImage.putdata(imdata)

    return thresholdedImage

def _2dArrayToImage(matrix):
    im = Image.new("L", (matrix.shape[1], matrix.shape[0]))
    im.putdata(matrix.flatten())
    return im

# TAKES IN A MATRIX y,x ordering
def identifyLetters(image):
    bw = makeWhiteOnBlack(image)
    image = bw

    image = imageToNPMatrix(image)
    bw = imageToNPMatrix(bw)

    distinctShapes = numpy.zeros(shape=image.shape)
    (height, width) = image.shape

    letters = []

    def recursiveFill(letter, x, y, num):
        if x == -1 or y == -1 or x >= width or y >= height:
            return # done
        if bw[y][x] == 0 or distinctShapes[y][x] != 0:
            return # done
        letter.append((x, y))
        distinctShapes[y][x] = num
        recursiveFill(letter, x - 1, y, num)
        recursiveFill(letter, x + 1, y, num)
        recursiveFill(letter, x, y + 1, num)
        recursiveFill(letter, x, y - 1, num)

    num = 1

    for y in range(0, height):
        for x in range(0, width):
            if bw[y][x] != 0 and distinctShapes[y][x] == 0:
                # if we found an unmarked nonempty pixel then we will flood fill it
                letter = [] # we build a list of the coordinates of the pixels in the letter. really slow but w/e
                recursiveFill(letter, x, y, num)
                num = num + 1

                # determine the bounding box of the letter...
                min_x = width
                min_y = height
                max_x = 0
                max_y = 0

                for (x, y) in letter:
                    if x < min_x:
                        min_x = x
                    if y < min_y:
                        min_y = y
                    if x > max_x:
                        max_x = x
                    if y > max_y:
                        max_y = y

                # rasterize the letter
                letter_rastered = numpy.zeros((max_y - min_y + 1, max_x - min_x + 1))
                for (x,y) in letter:
                    letter_rastered[y - min_y][x - min_x] = image[y][x]
                # push it to the letters list...
                letters.append(((min_x, min_y), letter_rastered))
    letters.sort(key=(lambda tupple: tupple[0][0]))
    return letters