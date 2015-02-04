#!/usr/bin/python
# Program reads topology file and atotype.atp as well as ffnonbonded.itp
# in order to create single matrix containing aa residues atoms list with atom
# mass, charge, epsilon, sigma and atom name in PDB format

import sys,os,re,csv,fileinput
import pandas as pd
from pandas import *
import numpy as np
from numpy import *
# from collections import defaultdict

residue_name=[]
atom_data=[]
epsi_data=[]
lines_epsi=[]
lines_mass=[]
lines_pdb=[]


# Prints entire data frame
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

# Rmin claculation
def Rmin(column):
    return (math.pow(2.0,1.0/6)*column['Sigma']/2)*10

# Creating temp dir
dirs= ['.temp', '.par']
for d in dirs:
    if not os.path.exists(d):
        os.mkdir(d)


# Topology name from command line
name=sys.argv[1]


###############################################################################
#Temporary files creation
###############################################################################
##Temporary files for atoms:
##  -z_atomlist.tmp - list of every atom in every residue from topology file
##  -z_mass.tmp - types of all atoms and their mass
##  -z_epsi.tmp - types of atoms and  epsilon and sigma values
##  -z_atoms.tmp - atom types , mass, epsilon and sigma values in one file.
#
# Reads residues, atom types and partial charge fromtopology and stores data in temporary file
with open('aminoacids.rtp','r') as input_topo, open('.temp/z_atomlist.tmp','w') as atomlist:
    for line in input_topo:
        if line.startswith(';'):
            continue
        if line.startswith('[') and line[2:8].isupper():
            residue_name=line.split()
        if '.' in line:
            atoms_list = line.split()
            data = '{}\t{}\t{}\t{: >}\n'.format(residue_name[1],atoms_list[0],atoms_list[1],atoms_list[2])
            atomlist.write(data)

# Reads atom types and mass from atomtypes.tpr
with open('atomtypes.atp','r') as input_mass, open('.temp/z_mass.tmp','w') as zmass:
    for line in input_mass:
        if line.startswith(';'):
            continue
        if '.' in line:
            atom_mass = line.split()
            mass = '{}\t{}\n'.format(atom_mass[0],atom_mass[1])
            zmass.write(mass)
# Reads epsilon and sigma from ffnonbonded.itp

with open('ffnonbonded.itp','r') as input_epsi, open('.temp/z_epsi.tmp','w') as epsi:
    for line in input_epsi:
        if line.startswith(';'):
            continue
        if '.' in line:
            atom_epsi = line.split()
            epsi_data = '{}\t{}\n'.format(atom_epsi[5],atom_epsi[6])
            epsi.write(epsi_data)

# Reads atom PDB name from atom_nom_md.tbl
with open('atom_nom_md.tbl','r') as pdb_names, open ('.temp/z_pdb_names.tmp','w')as output:
    for line in pdb_names:
        if line.startswith(';'):
            continue
        else:
            lines_pdb = line.split()
            if len(lines_pdb)>1:
                pdb_data = '{}\t{}\t{}\n'.format(lines_pdb[0],lines_pdb[1],lines_pdb[4])
                output.write(pdb_data)

##############################################################################
##############################################################################




#Building matrix and saving in atoms.par
with open('.temp/z_atomlist.tmp','r') as atom_list:
    dfatomlist=pd.read_csv(atom_list, header=None,index_col=None,sep='\t',names=['Residue','AtName','AtType','Charge'])

with open('atom_types_sigma_epsilon.tmp','r') as atoms:
    dfatoms=pd.read_csv(atoms, header=None,index_col=None,sep='\t',names=['AtType','Mass','Sigma','Epsilon'])

with open('.temp/z_pdb_names.tmp','r') as pdb_names:
    dfpdbnames=pd.read_csv(pdb_names, header=None, index_col=None,sep='\t',names=['Residue','AtName','PDBName'])


#PDB names after aton name
dftemp=pd.merge(dfatomlist,dfpdbnames,how='left',on=['Residue','AtName'])
dftemp=dftemp[['Residue', 'AtName','PDBName', 'AtType', 'Charge']]

#add mass sigma and esilon
dfsum= pd.merge(dftemp,dfatoms,on='AtType',how = 'left')

#Rmin calculation
dfrmin= pd.DataFrame({'AtType': dfsum['AtType'],'Rmin': Rmin(dfsum)})

#Rmin insertion to the results table

dfres=merge(dfsum, dfrmin, right_index=True, left_index=True, how='outer')

with open ('.par/'+name+'_atoms.par','w') as output:
    dfres.to_csv(output,sep='\t')
