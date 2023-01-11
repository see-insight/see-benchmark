# see-benchmark
Tools for running research benchmarks on shared HPC systems.  If you just cloned this directory try running the following command to get started:

```./hpcc_build.sh```

More detailed instructinos are below.  

Assuming the above installation worked, there are multiple benchmarks that can be run from this directory.  Look for the '''<<NAME>>_Batch.sb''' file to run each exmple. Supporting files will have other names and extentions including:

* '''<<NAME>>_Results.ipynb''' - Jupyter notebooks to view results form the benchmark.
* '''<<NAME>>_Results.sb''' - File to consolodate data from the benchmarks. (only required on the really big runs)
* '''<<NAME>>_<<keyword>>.py''' - Python file used by the other scripts to manage the run.

## HPCC singularity overlay
These instructions are specific to the HPCC at MSU.  

### Step 0: Clone this repository

```git clone https://github.com/see-insight/see-benchmark.git``` 

```cd see-benchmark```

### Step 1: Run the installer  

```source INSTALL.sh```

WAIT.......

### Step 2: Run a test localy

```./testrunlocal.sh```

```<<ctrl-c to stop>>```

### Step 3: Run continuous run script

```sbatch continuousrun.sb```

### Step 4: View results on Jupyter

For these steps to work you need access to the "beta" group to use a singularity image in jupyter. If you have access to this group you should be able to run this singularity image using the following settings:

1. Go to <http://ondemand.hpcc.msu.edu> and log in using your MSU NetID / Password
2. Click on "Interactive Apps" and select "Jupyter (beta)"
3. Find the section labeled "Jupyter Location" and select "Singularity" from the dropdown menu.
4. Use all of the default settings except change the "Path to Overlay Image" to the ```overlay.img``` file in this folder.  

In case you need it, here are resonable useful settings:

| Setting | Default Values |
|---------|----------------|
| Number of Hours | 4 |
| Number of cores per task | 1 |
| Amount of Memory | 5gb |
| Jupyter Location | Singularity |
| Jupyter Path | /miniconda3/bin |
| Path to Singularity Image | /opt/software/CentOS.container/7.4/bin/centos | 
| ReadOnly | unchecked |
| Path to Overlay Image | Set this to your overlay.img path |

5. Open the ContinuousArray.ipynb and run to view results.



 
