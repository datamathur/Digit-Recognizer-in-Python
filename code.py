# Importing important libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from tensorflow import keras
from tensorflow.keras import layers
from keras.utils.np_utils import to_categorical 
from keras.models import Sequential
from keras.optimizers import Adam

"""
Importing Data and Data Preprocessing
"""
train_data = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

#Spliting the data to train and dev sets
train, dev =  train_test_split(train_data, train_size = 0.92858)

y_train = train["label"]
x_train = train.drop(labels = ["label"],axis = 1)

y_dev = dev["label"]
x_dev = dev.drop(labels = ["label"],axis = 1)

x_test = test.values

#Normalizing the data 
x_train = x_train / 255.0
x_dev = x_dev / 255.0
x_test = test / 255.0

#Reshaping the data 
x_train = x_train.values.reshape(-1,28,28,1)
x_dev = x_dev.values.reshape(-1,28,28,1)
x_test = test.values.reshape(-1,28,28,1)

#Encoding the Labels
y_train = to_categorical(y_train, num_classes = 10)
y_dev = to_categorical(y_dev, num_classes = 10)


""""
Making and training CNN Model
"""

#Building the Model
Model = keras.Sequential(
    [
        keras.Input(shape=(28, 28, 1)),
        layers.Conv2D(filters = 16 , kernel_size=(5, 5), activation="relu", padding = 'Same'),
        layers.MaxPooling2D(pool_size=(2, 2), strides = 2),
        layers.Conv2D(filters = 32 , kernel_size=(5, 5), activation="relu", padding = 'Valid'),
        layers.MaxPooling2D(pool_size=(2, 2), strides = 2),
        layers.Flatten(),
        layers.Dense(80, activation="relu"),
        layers.Dense(20, activation="relu"),
        layers.Dense(10, activation="softmax"),
    ]
)

#Training the Model
batch_size = 128
epochs = 15

Model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
Model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

#Testing the Model
score = Model.evaluate(x_dev, y_dev, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

"""
Predicting the output for test case
"""
# predict results
results = Model.predict(x_test)

# select the indix with the maximum probability
results = np.argmax(results,axis = 1)
results = pd.Series(results,name="Label")

#Preparing the submission file 
submission = pd.concat([pd.Series(range(1,28001),name = "ImageId"),results],axis = 1)
submission.to_csv("cnn_submission.csv",index=False) 
