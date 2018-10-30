import sys
from utils import *
from keras_file import *

exp = int(sys.argv[1])
station = int(sys.argv[3])
data_version = int(sys.argv[2])
path = "../../results_" + str(station) + "/" + str(exp) + "/"

X_train, Y_train, X_valid, Y_valid = create_set(path, station, data_version)
model = create_model()
model_json = model.to_json()
with open(path + "model.json", "w") as json_file:
    json_file.write(model_json)
model.summary()
model.fit(X_train, Y_train[:,:,0], validation_data=(X_valid, Y_valid[:,:,0]), callbacks=callbacks(path), epochs=500)
