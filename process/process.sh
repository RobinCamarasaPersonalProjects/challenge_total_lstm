#!/bin/sh

n=`expr $(ls ../../results_$1 | sort -n | tail -n1) + 1`

echo "$1; $n;" >> ../../dashboard.csv

mkdir ../../results_$1/$n
python process.py $n $1 $2