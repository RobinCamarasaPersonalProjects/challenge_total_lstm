import sys
from utils import *

exp = int(sys.argv[1])
station = int(sys.argv[3])
data_version = int(sys.argv[2])
X_train, Y_train, X_valid, Y_valid = create_set(exp, station, data_version)
