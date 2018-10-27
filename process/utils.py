import numpy as np
import random


def create_set(exp, station, data_version):
    path = "../../results_" + str(station) + "/" + str(exp) + "/"
    X = np.load("../../data/" + str(data_version) + "/X_train_" + str(station) + ".npy")
    Y = np.load("../../data/" + str(data_version) + "/Y_train_" + str(station) + ".npy")
    l_X = []
    l_Y = []
    for k in range(X.shape[2]):
        begin = 14 + random.randint(0, 6)
        for j in range(begin, X.shape[1], 14):
            l_X.append(X[:, j - 14:j, k])
            l_Y.append(Y[:, j - 14:j, k])
    shuffle = np.random.permutation(np.arange(len(l_X))).tolist()
    X = np.array(l_X)[shuffle]
    Y = np.array(l_Y)[shuffle]
    X = np.swapaxes(X, 1, -1)
    Y = np.swapaxes(Y, 1, -1)
    split = int(0.8 * len(l_X))
    X_train = X[:split, :, :]
    X_valid = X[split:, :, :]
    Y_train = Y[:split, :, :]
    Y_valid = Y[split:, :, :]
    np.save(path + "X_train", X_train)
    np.save(path + "Y_train", Y_train)
    np.save(path + "X_valid", X_valid)
    np.save(path + "Y_valid", Y_valid)
    return X_train, Y_train, X_valid, Y_valid
