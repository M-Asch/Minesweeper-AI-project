from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout

import matplotlib.pyplot as plt
import numpy as np

from data import *

file = open("boards.json", "r")

boards, choices = cleanData(file)
y = findFlags(boards, choices)
#print(y)
# counts = {"<400":0,"400-800":0,"800-1200":0}
# for point in y:
#     if point < 400:
#         counts["<400"] += 1
#     elif point < 800:
#         counts["400-800"] += 1
#     else:
#         counts["800-1200"] += 1
boards = boards[:-1]

print(boards[0], y[0])

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

train_x = x[:int(size*.8)]
test_x = x[int(size*.8 + 1):]


y = keras.utils.to_categorical(y, num_classes=1200)
train_y = y[:int(size*.8)]
test_y = y[int(size*.8 + 1):]

model = Sequential()
model.add(Dense(800, input_dim=400, activation ='relu'))
#model.add(Dense(1050, activation ='relu'))
#model.add(Dense(1100, activation ='relu'))
#model.add(Dropout(.2))
model.add(Dense(1200, activation='softmax'))

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

history = model.fit(train_x, train_y, validation_data=(test_x, test_y), epochs=50, batch_size=100)
#score = model.evaluate(test_x, test_y, batch_size=100)
#print(score[0], score[1])
plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='test')
plt.legend()
plt.show()
