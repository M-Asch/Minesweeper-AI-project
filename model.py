from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.regularizers import l2
from keras.metrics import TopKCategoricalAccuracy

import matplotlib.pyplot as plt
import numpy as np

from data import *

#open both files
file = open("noFlags.json", "r")
file2 = open("boards.json", "r")

#use both board files and clean the data from them
boards, choices = cleanData(file)
boards2, choices2 = cleanData(file2)

y = setOutputs(boards, choices)
y2, boards2 = findFlags(boards2, choices2)
boards = boards + boards2
y = y + y2

#prepare data so it can be used by the model
x = []
count = 0
for board in boards:
    rows = []
    for row in board:
        rows = rows + row
    x.append(rows)
x = np.array(x)
y = np.array(y)

#seperate and prepare test/train data
size = int(len(x))

train_x = x[:int(size*.8)]
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
#model.save("//saves")

#Print History for the model in the graph
history = model.fit(train_x, train_y, validation_data=(test_x, test_y), epochs=100, batch_size=128)
for l in range(10, 35, 1):
    pred = model.predict(train_x[l].reshape(1, 400))
    plt.imshow(pred.reshape(20,20))
    for i in range(20):
        for j in range(20):
            text = plt.text(j, i, train_x[l].reshape(20, 20)[i][j], ha="center", va="center", color="white")
    plt.colorbar()
    plt.show()

plt.plot(history.history['accuracy'], label='Accuracy')
plt.plot(history.history['val_accuracy'], label='Test Accuracy')
plt.plot(history.history['top_k_categorical_accuracy'], label='Top 5 Accuracy')
plt.legend()
plt.show()
