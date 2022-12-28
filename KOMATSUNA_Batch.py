#!/usr/bin/env python
# coding: utf-8

# # KOMATSUNA Batch file on HPCC
# 
# This program is us exploring how we want to run a big multi-image job using the HPCC.  To start we are just going to run a singl eimage job using different input files for training. 

import sys
sys.path.append('./see-segment')

import argparse
import matplotlib.pylab as plt
from imageio import v3 as imageio
from see import Segmentors
from see import JupyterGUI
from see.Segmentors import segmentor
from see.ColorSpace import colorspace
from see.Workflow import workflow
from see.Segment_Fitness import segment_fitness
from see import base_classes, GeneticSearch
from see import DataDownload
import random

parser = argparse.ArgumentParser(description='Run KOMATSUNA Search on Workflow')

parser.add_argument('--knum',type=int,default=10, help='Index for the image in the KOMATSUNA database')
parser.add_argument('--seed', type=int,default=1, help='Input seed (integer)') 
parser.add_argument('--pop_size', type=int,default=100, help='Population Size (integer)') 
parser.add_argument('--num_iter', type=int,default=50, help='Maximum Iterations (integer)') 
args = parser.parse_args()

print('\n\n')
print(args)
print('\n\n')


random.seed(args.seed)

# In[]:
[imagenames, masknames, outputnames] = DataDownload.getKomatsunaFolderLists(folder='./see-segment/Image_data/')

# In[]:



# put data in a pipeline
data = base_classes.pipedata()

print(f"#{input_file=}")
print(f"#{input_mask=}")


#TODO make this a KOMATSUNA measure
data.img = imageio.imread(imagenames[args.knum])
data.gmask = imageio.imread(imagenames[args.knum])


# In[]:
#define an algorithm workflow
workflow.addalgos([colorspace, segmentor, segment_fitness])

mydata = base_classes.pipedata()
mydata.append(data.img)
mydata.gtruth = data.gmask
#def geneticsearch
my_evolver = GeneticSearch.Evolver(workflow, mydata, pop_size=10)
            
# In[]:
#TODO This needs to be fixed Using the new syntax.
#my_evolver = GeneticSearch.Evolver(workflow, mydata, pop_size=10)
my_evolver = GeneticSearch.Evolver(workflow, mydata, pop_size=args.pop_size)

# In[]:
# warnings may appear when this runs
population = my_evolver.run(ngen=args.num_iter)





