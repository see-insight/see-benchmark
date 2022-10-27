# see-benchmark
Tools for running research benchmarks on shared HPC systems

## Install see-segment
The following instructions will assume see-segment is installed in this directory

```git clone git@github.com:see-insight/see-segment.git```

## HPCC singularity overlay

Step 1: create an overlay  
```create_jupyter_singularity_overlay```
  
```overlay_start```
  
```source activate_conda.sh```

```conda env update --file ./see-segment/environment.yml```

WAIT.......

```exit```

```singularity build centos7.sif /opt/software/CentOS.container/7.4/bin/centos```

```singularity sif add --datatype 4 --partfs 2 --parttype 4 --partarch 2 --groupid 1 centos7.sif overlay.img```

## Testing See segment
Go into the see-segment folder and run the following command:

```make test```




 
