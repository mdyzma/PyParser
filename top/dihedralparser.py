#!/usr/bin/python
# Program reads topology file and ffbonded.itd as well as ffnonbonded.itp
# in order to create single matrix containing aa residues atoms list with atom
# mass, charge, epsilon, sigma and atom name in PDB format

import sys,os, re, csv
import pandas as pd
import numpy as np
from collections import defaultdict


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

##############################################
# Bonds
##############################################

# #Building matrix of bonds types and saving to z_bondtypes.tmp
# with open('ffbonded.itp','r') as bonds_input, open ('z_bondtypes.tmp','w') as output:
#     for line in bonds_input:
#         if 'bondtypes' in line:
#             break
#     for line in nonblank_lines(bonds_input):
#         if 'constrainttypes' in line:
#             break
#         if line.startswith(';') or line.startswith('['):
#             continue
#         bonds=line.partition(';')
#         x=[]
#         x=bonds[0].split()
#         # print x
#         # print x,type(x)
#         x='{}\t{}\t{}\t{}\t{}\n'.format(x[0],x[1],x[2],x[3],x[4],)
#         output.write(x)


# with open('z_bondtypes.tmp','r') as bs, open ('bonds.par', 'w') as output:
#     df1=pd.read_csv(bs,header=None,index_col=None,sep='\t',names=['i','j','func','b0','Kb'])
#     # print_full(df1)
#     df1.to_csv(output,sep='\t')


##############################################
# Angles
##############################################

# #Building matrix of angles types and saving to z_angletypes.tmp
# with open('ffbonded.itp','r') as angle_input, open ('z_angletypes.tmp','w') as output:
#     for line in angle_input:
#         if 'angletypes' in line:
#             break
#     for line in nonblank_lines(angle_input):
#         if 'dihedraltypes' in line:
#             break
#         if line.startswith(';') or line.startswith('['):
#             continue
#         angles=line.partition(';')
#         x=[]
#         x=angles[0].split()
#         # print x
#         # print x,type(x)
#         x='{}\t{}\t{}\t{}\t{}\t{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],)
#         output.write(x)


# with open('z_angletypes.tmp','r') as angs, open ('angles.par', 'w') as output:
#     df2=pd.read_csv(angs,header=None,index_col=None,sep='\t',names=['i','j','k','func','th0','cth'])
#     # print_full(df2)
#     df2.to_csv(output,sep='\t')



##############################################
# Dihedrals
##############################################

#Building matrix of dihedral angles and saving to z_dihedrals.tmp
with open('ffbonded.itp','r') as dih_input, open ('z_dihedraltypes.tmp','w') as output:
    for line in nonblank_lines(dih_input):
        if 'dihedraltypes' in line:
            break
        if line.startswith(';') or line.startswith('['):
            continue
        angles=line.partition(';')
        x=[]
        x=angles[0].split()
        if len(x)>5:
            print x,'\t',len(x)
        # x='{}\t{}\t{}\t{}\t{}\t{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],)
        # output.write(x)


# with open('z_angletypes.tmp','r') as dih, open ('dihedrals.par', 'w') as output:
#     df3=pd.read_csv(dih,header=None,index_col=None,sep='\t',names=['i','j','k', 'l', func','C0','C5','X'])
#     # print_full(df3)
#     df3.to_csv(output,sep='\t')
