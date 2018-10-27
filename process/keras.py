from keras.layers import *
from keras.models import *


def model_1():
    input = Input(shape=(14,50))
    lstm = LSTM(1)
    fullyconnected = Dense(1)

