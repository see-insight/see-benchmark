#!/bin/bash

export SLURM_ARRAY_TASK_ID=$1
export SLURM_JOB_ID=$2

if [ "$1" == "" ]
then
    export SLURM_ARRAY_TASK_ID=1
fi

if [ "$2" == "" ]
then
    export SLURM_JOB_ID=2
fi


source ./EXAMPLES_Batch.sb 
