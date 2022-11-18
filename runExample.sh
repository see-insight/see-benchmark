#!/bin/bash

export IMGNUM=$1
export PYTHONPATH="./see-segment/"

if [ ! -f imagefile.txt ]
then
    touch imagefile.txt

    for GT in ./see-segment/Image_data/Examples/*GT*
    do
       ROOTNAME=`echo $GT | sed -e "s/_GT.*$//"`
    echo `echo ${ROOTNAME}.*` $GT >> imagefile.txt
    done
fi
MINE=`head -n $1 imagefile.txt | tail -n 1`

python ./see-segment/see/RunSearch.py --seed $2 $MINE

echo "FINNISHED RUNNING SCRIPT"
