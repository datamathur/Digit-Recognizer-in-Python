# Digit Recognizer in Python <br>
One of the most exciting applications of Deep Neural Networks is character recognition. This repository contains the dataset and code file for a Digit recognizer model. <br>

The basic concept used in developing this model is Convolutional Neural Networks(CNNs). CNN is a very efficient way of reducing the number of parameters while increasing the depth of Neural Networks. The file named 'code.py' conatins the model of a CNN which I developed for digit recognizer. The Model is inspired from the famous LeNet which was published in a paper in 1998 by Yann LeCun. The source code for the original paper is in the file 'LeCun.py'. <br>

The model that I made was able ot achieve 98.799% accuracy, which is similar to the accurary achieved by the model by Yann LeCun ,i.e., 98.866%. <br>

## Dataset <br>
This dataset is a classic dataset of handwritten digits, released in 1999 by MNIST ("Modified National Institute of Standards and Technology"), which can be found on https://www.kaggle.com/c/digit-recognizer/overview .<br>  
The data files train.csv and test.csv contain gray-scale images of hand-drawn digits, from zero through nine.<br>

Each image is 28 pixels in height and 28 pixels in width, for a total of 784 pixels in total. Each pixel has a single pixel-value associated with it, indicating the lightness or darkness of that pixel, with higher numbers meaning darker. This pixel-value is an integer between 0 and 255, inclusive.<br>

The training data set, (train.csv), has 785 columns. The first column, called "label", is the digit that was drawn by the user. The rest of the columns contain the pixel-values of the associated image.<br>

The test data set, (test.csv), is the same as the training set, except that it does not contain the "label" column.<br>
