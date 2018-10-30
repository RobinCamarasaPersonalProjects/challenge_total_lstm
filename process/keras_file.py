from keras.layers import *
from keras.models import *
from keras.callbacks import *


def create_model():
    model = Sequential()
    model.add(LSTM(14, input_shape=(14, 50,), activation='sigmoid'))
    model.add(Reshape((14,1)))
    model.add(Dense(50))
    model.add(LSTM(14, input_shape=(14, 50,), activation='sigmoid'))
    model.compile(loss='mean_squared_error', optimizer='adadelta')
    return model


def callbacks(path):
    return [TensorBoard(log_dir=path + 'logs'),
            BaseLogger(),
            ProgbarLogger(),
            ModelCheckpoint(path + 'weights.hdf5', save_best_only=True),
            CSVLogger(path + 'training.csv'),
            History()
            ]
