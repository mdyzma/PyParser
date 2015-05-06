#!/usr/bin/python

import sys,os, re, csv
import pandas as pd
import numpy as np
from collections import defaultdict

residue_name=[]
atom_data=[]
epsi_data=[]
lines_epsi=[]
lines_mass=[]
lines_pdb=[]


def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')


########################################################
########################################################
#Temporary files for atoms
#z__atomlist.tmp - list of every atom in every residue from topology file
#z_mass.tmp - types of all atoms and their mass
#z_epsi.tmp - types of atoms and  epsilon and sigma values
#z_atoms.tmp - atom types , mass, epsilon and sigma values in one file.
#
# #Reads residues, atom types and partial charge fromtopology and stores data in temporary file
# with open('aminoacids.rtp','r') as input_topo, open('z_atomlist.tmp','w') as atomlist:
#     for line in input_topo:
#         if line.startswith(';'):
#             continue
#         if line.startswith('[') and line[2:8].isupper():
#             residue_name=line.split()
#         if '.' in line:
#             atoms_list = line.split()
#             data = '{}\t{}\t{}\t{: >}\n'.format(residue_name[1],atoms_list[0],atoms_list[1],atoms_list[2])
#             atomlist.write(data)



# #Reads atom types and mass from atomtypes.tpr
# with open('atomtypes.atp','r') as input_mass, open('z_mass.tmp','w') as zmass:
#     for line in input_mass:
#         if line.startswith(';'):
#             continue
#         if '.' in line:
#             atom_mass = line.split()
#             mass = '{}\t{}\n'.format(atom_mass[0],atom_mass[1])
#             zmass.write(mass)


# #Reads epsilon and sigma from ffnonbonded.itp
# with open('ffnonbonded.itp','r') as input_epsi, open('z_epsi.tmp','w') as epsi:
#     for line in input_epsi:
#         if line.startswith(';'):
#             continue
#         if '.' in line:
#             atom_epsi = line.split()
#             epsi_data = '{}\t{}\n'.format(atom_epsi[5],atom_epsi[6])
#             epsi.write(epsi_data)


# #Main atom output combination
# with open('z_mass.tmp','r') as atom_mass, open('z_epsi.tmp','r') as atom_epsi,open('z_atoms.tmp','w') as output:
#     reader1 = csv.reader(atom_mass, delimiter='\t')
#     reader2 = csv.reader(atom_epsi,delimiter='\t')
#     writer = csv.writer(output,delimiter='\t')
#     for row1, row2 in zip(reader1,reader2):
#         zipped = row1[0],row1[1],row2[0],row2[1]
#         ff='{}\t{}\t{}\t{}\n'.format(row1[0],row1[1],row2[0],row2[1])
#         output.write(ff)

# with open('atom_nom_output.tbl','r') as pdb_names, open ('z_pdb_names.tmp','w')as output:
#     for line in pdb_names:
#         if line.startswith(';'):
#             continue
#         else:
#             lines_pdb = line.split()
#             pdb_data = '{}\t{}\t{}\t{}\t{}\n'.format(lines_pdb[0],lines_pdb[1],lines_pdb[2],lines_pdb[3],lines_pdb[4])
#             output.write(pdb_data)

########################################################
########################################################





with open('z_atomlist.tmp','r') as atom_list:
    df1=pd.read_csv(atom_list, header=None,index_col=None,sep='\t',names=['Residue','AtName','AtType','Charge'])

with open('z_atoms.tmp','r') as atoms:
    df2=pd.read_csv(atoms, header=None,index_col=None,sep='\t',names=['AtType','Mass','Sigma','Epsilon'])

# with open('z_pdb_names.tmp','r') as pdb_names:
    # df3=pd.read_csv(pdb_names, header=None, index_col=None,sep='\t',names=['Residue','XPLOR','MSI','GROMACS','PDB'])

    print_full(df1)

with open ('atoms.par','w') as output:
    df4= pd.merge(df1,df2,on='AtType',how = 'left')
    df4.to_csv(output,sep='\t')


    # df5=pd.merge(df4,df3['PDB'],left_on='AtType',right_on='PDB',left_index=True)
    # print_full(df5)
