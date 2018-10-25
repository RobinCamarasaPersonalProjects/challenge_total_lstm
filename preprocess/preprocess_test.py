import sys
from utils import *

# coding: utf-8

path_csv = '../../data/0/' + sys.argv[1]
nb_products = int(sys.argv[2])
nb_lines = int(sys.argv[3])
nb_days = int(sys.argv[3]) / int(sys.argv[2])
path = '../../data/' + sys.argv[4] + '/'
nb_features = 50
nb_exp = int(sys.argv[5])

print ('file : ' + path_csv)
print ('\tnb_product : ' + str(nb_products))
print ('\tnb_lines : ' + str(nb_lines))
print ('\tnb_days : ' + str(nb_days))
print ('\tpath: ' + path)

create_X(nb_exp, 'test', path, path_csv, nb_days, nb_features, nb_products)

print('processed')