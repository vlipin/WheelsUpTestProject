#!/bin/sh

# this while loop iterates over all lines of the file
for i in 1 2 3 4 5 6 7
do
  touch my_file$i.txt
done
for i in 1 2 3 4
do
  rm my_file$i.txt
done


