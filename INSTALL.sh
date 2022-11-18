#!/bin/bash
# Build everything we need to INSTALL on HPCC and run inside of singularity
#
# Output is a centos7.sif image with see-segment, jupyter and everything installed.
# Secondary output is an overlay.img file you can use with OnDemand

#Create base overlay
create_jupyter_singularity_overlay

#Clone see-segment
if [ -d see-segment ]
then
    echo "see-segment already found"
else
    echo "Downloading see-segment"
    git clone https://github.com/see-insight/see-segment.git
fi

#Update overlay with see-segment enviornment.
overlay_exec conda env update --name base --file ./see-segment/environment.yml

#Make a local copy of centos7
singularity build centos7.sif /opt/software/CentOS.container/7.4/bin/centos

#Wrap overlay.img into centos7
singularity sif add --datatype 4 --partfs 2 --parttype 4 --partarch 2 --groupid 1 centos7.sif overlay.img


