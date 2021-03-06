#!/usr/bin/python
# Program reads topology file and ffbonded.itd as well as ffnonbonded.itp
# in order to create single matrix containing aa residues atoms list with atom
# mass, charge, epsilon, sigma and atom name in PDB format

import sys,os,re,csv,fileinput,glob
import pandas as pd
from pandas import *
import numpy as np
from numpy import *


bonds= []
angles=[]
dihedrals=[]

#Prints entire data frame
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

#Removes blank lines
def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

# Creating temp dir if dont exist
dirs= ['.temp', '.par']
for d in dirs:
    if not os.path.exists(d):
        os.mkdir(d)


# Topology name from command line
name=sys.argv[1]

#############################################
#Bonds
#############################################

#Building matrix of bonds types and saving to z_bondtypes.tmp
with open('ffbonded.itp','r') as bonds_input, open ('.temp/z_bondtypes.tmp','w') as output:
    for line in bonds_input:
        if 'bondtypes' in line:
            break
    for line in nonblank_lines(bonds_input):
        if 'constrainttypes' in line:
            break
        if line.startswith(';') or line.startswith('['):
            continue
        bonds=line.partition(';')
        x=[]
        x=bonds[0].split()
        # print x
        # print x,type(x)
        x='{}\t{}\t{}\t{}\t{}\n'.format(x[0],x[1],x[2],x[3],x[4],)
        output.write(x)


with open('.temp/z_bondtypes.tmp','r') as bs, open ('.par/'+name+'_bonds.par', 'w') as output:
    df1=pd.read_csv(bs,header=None,index_col=None,sep='\t',names=['i','j','func','b0','Kb'])
    # print_full(df1)
    df1.to_csv(output,sep='\t')


#############################################
#Angles
#############################################

#Building matrix of angles types and saving to z_angletypes.tmp
with open('ffbonded.itp','r') as angle_input, open ('.temp/z_angletypes.tmp','w') as output:
    for line in angle_input:
        if 'angletypes' in line:
            break
    for line in nonblank_lines(angle_input):
        if 'dihedraltypes' in line:
            break
        if line.startswith(';') or line.startswith('['):
            continue
        angles=line.partition(';')
        x=[]
        x=angles[0].split()
        # print x
        # print x,type(x)
        x='{}\t{}\t{}\t{}\t{}\t{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],)
        output.write(x)


with open('.temp/z_angletypes.tmp','r') as angs, open ('.par/'+name+'_angles.par', 'w') as output:
    df2=pd.read_csv(angs,header=None,index_col=None,sep='\t',names=['i','j','k','func','th0','cth'])
    # print_full(df2)
    df2.to_csv(output,sep='\t')
