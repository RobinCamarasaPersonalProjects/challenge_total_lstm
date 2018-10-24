#!/bin/sh

npy_creation_train() {

    lines=`expr $(cat ../../data/0/$1 | wc -l) - 1`
    nb_products=`expr $(cut -f4 -d';' ../../data/0/$1 | sort | uniq  | wc -l) - 1`


    python preprocess_train.py $1 $nb_products $lines $2 $3
}

npy_creation_test() {

    lines=`expr $(cat ../../data/0/$1 | wc -l) - 1`
    nb_products=`expr $(cut -f4 -d';' ../../data/0/$1 | sort | uniq  | wc -l) - 1`


    python preprocess_test.py $1 $nb_products $lines $2 $3
}

n=`expr $(ls ../../data | sort | tail -n1) + 1`
mkdir ../../data/$n
npy_creation_train train_station_1.csv $n 1
echo ""
npy_creation_train train_station_2.csv $n 2
echo ""
npy_creation_test test_station_1.csv $n 1
echo ""
npy_creation_test test_station_2.csv $n 2
echo ""