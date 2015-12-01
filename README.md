# PYTHON OCR
by Gareth George

Python OCR is a basic optical character recognition library written in python. It takes an image file as it's input and returns what it believes the contents of the image file to be.

It uses a neural network (using pybrain's implementation) to perform the actual digit classification. This neural network is trained on samples of a number of fonts so it can recognise various typefaces. By default Ariel and Helvetica are coded in though more can be added in lib fontydatasets.py.

### THE STEPS
 - simple thresholding and image binarization
 - letter seperation via a flood fill type algorithm
 - image resizing to 28x28 pixels.
 - classification with pybrain neural network

# INSTALLATION

DEPENDENCIES
 - pybrain
 - python
 - PIL

