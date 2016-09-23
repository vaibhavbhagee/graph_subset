#! /bin/bash

python generate.py $1 $2 $3 $4 > test.graphs
python gen_input.py
./minisat test.satinput test.satoutput
python gen_output.py
python check.py test.graphs test.mapping