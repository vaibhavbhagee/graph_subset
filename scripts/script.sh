#! /bin/bash

python ../src/generate.py $1 $2 $3 $4 > $5.graphs
./compile.sh
./run1.sh $5
./../minisat $5.satinput $5.satoutput
./run2.sh $5
python ../src/check.py $5.graphs $5.mapping