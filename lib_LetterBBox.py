from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def fitTo28x28(letter):
    (width, height) = letter.size

    x_left = -1
    x_right = -1

    y_top = -1
    y_bottom = -1

    for x in range(0, width):
        for y in range(0, height):
            if letter.getpixel((x, y)) != 0:
                x_left = x
                break
        if x_left != -1:
            break

    for x in range(width-1, 0, -1):
        for y in range(0, height):
            if letter.getpixel((x, y)) != 0:
                x_right = x
                break
        if x_right != -1:
            break
    
    for y in range(0, width):
        for x in range(0, height):
            if letter.getpixel((x, y)) != 0:
                y_top = y
                break
        if y_top != -1:
            break

    for y in range(height-1, 0, -1):
        for x in range(0, width):
            if letter.getpixel((x, y)) != 0:
                y_bottom = y
                break
        if y_bottom != -1:
            break

    #print x_left, x_right, y_top, y_bottom
    # crop the image to the new size
    letter_c = letter.crop((x_left, y_top, x_right + 1, y_bottom + 1))
    #letter_c = letter.crop((10, 10, 20, 20))
    letter_c = letter_c.resize((28, 28), Image.ANTIALIAS)
    return letter_c
