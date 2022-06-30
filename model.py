#=======================================================
# Ryan Erickson, Manas Panachavati, Mitchell Aschmeyer
# model.py
# June 2022
# This project allows for the creationg of a Minesweeper AI
# using keras to build a simple feed forward neural network.
#======================================================
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.regularizers import l2
from keras.metrics import TopKCategoricalAccuracy

import matplotlib.pyplot as plt
import numpy as np

import os

from data import *

#=======================================================
#Main File
#======================================================

#open up the two data files
file = open("noFlags.json", "r")
file2 = open("boards.json", "r")

#prepare the data for the model (file2 needs extra cleaning to remove excess moves)
x, y = prepData(file, file2)

#seperate and prepare test/train data
size = int(len(x))
train_x = x[:int(size*.8)]      #seperate into training and test data
test_x = x[int(size*.8 + 1):]

y = keras.utils.to_categorical(y, num_classes=400)
train_y = y[:int(size*.8)]
test_y = y[int(size*.8 + 1):]

#build the model
model = Sequential()
model.add(Dense(400, kernel_regularizer=l2(0.01), input_dim=400, activation ='relu'))
model.add(Dense(600, activation ='relu'))
model.add(Dense(800, activation ='relu'))
model.add(Dense(400, activation='softmax'))

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy', TopKCategoricalAccuracy(k=5, name='top_k_categorical_accuracy')])
model.summary()
location = os.getcwd()
model.save(location + "\saves")

#Print History for the model in the graph
history = model.fit(train_x, train_y, validation_data=(test_x, test_y), epochs=100, batch_size=128)
# for l in range(10, 35, 1):
#     pred = model.predict(train_x[l].reshape(1, 400))
#     plt.imshow(pred.reshape(20,20))
#     for i in range(20):
#         for j in range(20):
#             text = plt.text(j, i, train_x[l].reshape(20, 20)[i][j], ha="center", va="center", color="white")
#     plt.colorbar()
#     plt.show()

plt.plot(history.history['accuracy'], label='Accuracy')
plt.plot(history.history['val_accuracy'], label='Test Accuracy')
plt.plot(history.history['top_k_categorical_accuracy'], label='Top 5 Accuracy')
plt.legend()
plt.show()
