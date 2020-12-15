# Digit Recognizer in Python <br>
One of the most exciting applications of Deep Neural Networks is character recognition. This repository contains the dataset and code file for a Digit recognizer model. <br>


## Dataset <br>
This dataset is a classic dataset of handwritten digits, released in 1999 by MNIST ("Modified National Institute of Standards and Technology"), which can be found on https://www.kaggle.com/c/digit-recognizer/overview .<br>  
The data files train.csv and test.csv contain gray-scale images of hand-drawn digits, from zero through nine.<br>

Each image is 28 pixels in height and 28 pixels in width, for a total of 784 pixels in total. Each pixel has a single pixel-value associated with it, indicating the lightness or darkness of that pixel, with higher numbers meaning darker. This pixel-value is an integer between 0 and 255, inclusive.<br>

The training data set, (train.csv), has 785 columns. The first column, called "label", is the digit that was drawn by the user. The rest of the columns contain the pixel-values of the associated image.<br>

The test data set, (test.csv), is the same as the training set, except that it does not contain the "label" column.<br>

## Training <br>

I've worked on two models here - **Neural Networks** and **Convolutional Neural Networks**. The models and there results are describes below.
| Model                              | Trainable Paramaters | Non-trainable paramerters | Test Accuracy |
| ---------------------------------- | -------------------- | ------------------------- | ------------- |
|Neural Networks (NN)                | 79,710               | 200                       |97.879 %       |
|Convolutional Neural Networks (CNN) | 213,334              | 128                       |99.21 %        |

The Model is inspired by the famous LeNet which was published in a paper in 1998 by Yann LeCun. The source code for the original paper is in the file 'LeCun.py'. <br>