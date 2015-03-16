#! /bin/bash

#uses pdftk to merge all pdf in the give directory in the order that they have been put in that
#directory

FILES=$(ls -tr)

pdftk $FILES cat output test.pdf
