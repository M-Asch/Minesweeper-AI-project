from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation

import matplotlib.pyplot as plt
import numpy as np

from data import *

file = open("boards.json", "r")

boards, choices = cleanData(file)
y = findFlags(boards, choices)
boards = boards[:-1]

x = []
count = 0
for board in boards:
    rows = []
    for row in board:
        rows = rows + row
    x.append(rows)
x = np.array(x)
y = np.array(y)


size = int(len(x))
print(x)

train_x = x[:int(size*.8)]
test_x = x[int(size*.8 + 1):]


y = keras.utils.to_categorical(y, num_classes=1200)
train_y = y[:int(size*.8)]
test_y = y[int(size*.8 + 1):]

model = Sequential()
model.add(Dense(400, input_dim=400, activation ='relu'))
model.add(Dense(800, activation='relu'))
model.add(Dense(1000, activation='relu'))
model.add(Dense(1200, activation='softmax'))

model.compile(optimizer='sgd', loss='mse', metrics=['accuracy'])

model.summary()

model.fit(train_x, train_y, epochs=100, batch_size=128)
score = model.evaluate(test_x, test_y, batch_size=128)
print(score[0], score[1])