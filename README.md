# **Minesweeper-AI-project**
**Created By:** Manas Panchavati, Ryan Erickson, Mitchell Aschmeyer

This folder contains code to train a simple neural network which can be taught to play minesweeper. Already complete models can be found in the *saves* folder which will have keras models saved in there. This AI has 3 key files for its training: *data.py*, *minesweepertk.py*, and *model.py*. *minesweepertk.py* uses a simple tkinter version of minesweeper to save data. *data.py* cleans this data and reformats it to be passed into the model. *model.py* contains the model and when run will train a new model using the provided data set. 

## **Data Collection**

Raw data is first collected through *minesweepertk.py*. Each time a tile is flipped the code will save 2 pieces of data to a chosen file, the state of the board before the choice was made and the coordinates of the flipped tile. This will be exported as an array string using json and can be read in through *data.py*. 

The data requires quite a bit of cleaning as the setup for our model changed out data needed to be created midway through development. All input data is first normalized to remove extreme values used for unclicked and flagged tiles. *data.py* has two functions which handle different data cleaning. If times where mines where flagged were included in the data, then the function *findFlags()* should be used. If the data does not include flag moves use the *setOutputs()* function. 

The function *prepData()* has two inputs file1 and file2. file1 should be given clean data without flag moves while file2 can be given non-clean data with flag moves. It will then handle the cleaning of the data from the files and prepare it to be used by the keras model. 

## **Running the Model**

Once data has been collected simply open the files for the data and run them through the *prepData()* function. The data will then be split into training and testing data before being passed into the model. The model will then begin its training. 

As the model is training it will show the training/testing loss and accuracy along with the 'top_k_categorical_accuracy' which provides a more accurate measurment of success as the move made in testing is not the only possible move. 

Two types of images can be printed out. The first is a heatmap which shows what the network was seeing as its input where the color of the tile represents the confidence the network has that it is a safe choice. 

![Heatmap Ex. 1](\screenshots\Figure_1.png)

![Heatmap Ex. 2](\screenshots\Figure_2.png)

A graph plotting the testing and training accuracy along with the 'top_k_categorical_accuracy' can also be produced. Note that training accuracy and testing accuracy will be much lower then 'top_k_categorical_accuracy'. 

![Heatmap Ex. 2](..\screenshots\Results.png)
