import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pathlib import Path
import re


def getslurmoutputfiles(directory='.'):
    slurmoutdir = Path(directory)
    slurmfiles = slurmoutdir.glob('*.out')

    filelist = []

    for file in slurmfiles:
        jobnum = re.findall('-[0-9]*_', str(file))[0][1:-1]
        array = re.findall('_[0-9]*\.', str(file))[0][1:-1]
        item = [str(file), int(jobnum), int(array)]
        filelist.append(item)

    df = pd.DataFrame(filelist, columns=['filename', 'jobid', 'arrayid'])
    df = df.sort_values(by=['arrayid', 'jobid'])
    return df

def Namespace(input_file='', input_mask='', seed=60, pop_size=0, num_iter=0):
    ns = {}
    ns['input_file'] = input_file;
    ns['input_mask'] = input_mask;   
    ns['seed'] = seed;
    ns['pop_size'] = pop_size;
    ns['num_iter'] = num_iter
    #print(ns)
    return ns

def parseoutput(filename):
    bestsofar = []
    stats = {}
    times = []
        index = 0
        for line in f:
            if 'TRUE_BST' in line:
                vecstr = line[9:]
            if 'BEST' in line:
                vecstr = line[6:]
                x = eval(vecstr)
                x = [index] + x
                bestsofar.append(x)
            if '#input_file' in line:
                stats['input_file'] = item.split('=')[1]
            if '#mask_file' in line:
                stats['mask_file'] = item.split('=')[1]
            if 'Namespace' in line:
                data = line[10:-2].split(',')
                for item in data:
                    name,value = item.strip().split('=')
                    stats[name]=value   
            #if 'TIME' in line:
            #    times.append(float(line.split(' ')[1]))
            #if 'HASH' in line:
            #if slurmstepd: 
            index += 1

    return bestsofar, stats, times

def parseall(df):
    examples = {}
    iterations = {}
    mystats = {}
    times = {}
    for index, row in df.iterrows():
        if True: #if f"_{item}." in row['filename']:
            bestsofar, stats, thistime = parseoutput(row['filename'])
            #print(f"{row['filename']} - {len(bestsofar)}")
            if not row['arrayid'] in examples:
                examples[row['arrayid']] = bestsofar
                iterations[row['arrayid']] = [ len(examples[row['arrayid']]) ]
                mystats[row['arrayid']] = stats
                times[row['arrayid']] = thistime
            else:
                examples[row['arrayid']] = examples[row['arrayid']] + bestsofar
                iterations[row['arrayid']].append(len(examples[row['arrayid']]))
                times[row['arrayid']] = times[row['arrayid']] + thistime
                if mystats[row['arrayid']] == None:
                    mystats[row['arrayid']] = stats

    rundata = {}
    for arrayid in mystats:
        key = Path(mystats[arrayid]['input_file'][1:-1]).stem
        if not key in rundata:
            rundata[key] = mystats[arrayid]
            rundata[key]['iterations'] = [iterations[arrayid]]
            rundata[key]['data'] = [examples[arrayid]]
            if arrayid in times:
                if len(times[arrayid]) > 0:
                    rundata[key]['times'] = [ (np.array(times[arrayid]) - times[arrayid][0])/1000/60 ]
        else:
            rundata[key]['data'].append(examples[arrayid])
            rundata[key]['iterations'].append(iterations[arrayid])
            if arrayid in times:
                if len(times[arrayid]) > 0:
                    rundata[key]['times'].append((np.array(times[arrayid]) - times[arrayid][0])/1000/60)
    return rundata

def plot_rundata(mydata, key='label'):
    legend = []
    for index,data in enumerate(mydata['data']):
        results = pd.DataFrame(data, columns=['index', 'fitness', 'individual'])
        trend = [1] + list(results['fitness']);
        plt.title(f"{key}")
        legend.append(f"{trend[-1]}")
        if len(mydata['iterations'][index]) > 1:
            for idx in mydata['iterations'][index]:
                plt.plot([idx, idx], [0, 1], 'r')
        plt.plot(trend[:])
    plt.legend(legend)
