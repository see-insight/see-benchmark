#!/bin/bash
#Only run once! 
#Script to build overlay image and run a benchmark on Examples folder

git clone git@github.com:see-insight/see-segment.git

create_jupyter_singularity_overlay

overlay_exec conda shell.bash activate > activate_conda.sh
chmod 775 activate_conda.sh  
overlay_exec ./activate_conda.sh; conda env update --file ./see-segment/environment.yml

singularity build centos7.sif /opt/software/CentOS.container/7.4/bin/centos

singularity sif add --datatype 4 --partfs 2 --parttype 4 --partarch 2 --groupid 1 centos7.sif overlay.img

sbatch runExamples.sb 



 
