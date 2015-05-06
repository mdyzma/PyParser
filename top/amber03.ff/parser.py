#!/usr/bin/python

import sys,os, re

residue_name=[]
atoms_list =[]
atoms_mass =[]
atoms_data = []
sigma = []
epsilon = []

with open('aminoacids.rtp','r') as input_topo, open('ffnonbonded.itp','r') as input_atoms:
# open('atoms.par','w') as atoms_output, open('bonds.par', 'w') as bonds_output,  open('dihedrals.par', 'w') as dihedrals_output:
    for line in input_topo:
        if line.startswith(';'):
            continue
        if line.startswith('[') and line[2:8].isupper():
            residue_name=line.split()
        if '.' in line:
            atoms_list = line.split()
    for line in input_atoms:
        if line.startswith(';') or line. startswith('['):
            continue
        else:
            atoms_mass=line.split()
            print residue_name, #atoms_list#atoms_mass[2],atoms_mass[4],atoms_mass[5]



# with open(ffnonbonded.itp,'r') as input_data:# open('atoms.par','w') as atoms_output, open('bonds.par', 'w') as bonds_output,  open('dihedrals.par', 'w') as dihedrals_output:
#     for line in input_data:
#         if line.startswith(';'):
#             continue
#         if :
#             atoms_data = line.split()
#             atoms_mass = atoms_data[2]
#             sigma = atoms_data[5]
#             epsilon = atoms_data[6]
        # print '{0: <10}\t{0: <10}\t{1: <10}\t{2: >10}\n'.format(residue_name[1],atoms_list[0],atoms_list[1],atoms_list[2])

            # atoms_data='{0: <10}\t{1: <10}\t{2: <10}\t{3: >10}\n'.format(residue_name[1],atoms_list[0],atoms_list[1],atoms_list[2])
            # atoms_output.write(atoms_data)
        # if line.startswith(' ') and len(line)==13:
        #     bonds_list = line.split()
        #     bonds_data='{0: <10}\t{1: <10}\n'.format(bonds_list[0],bonds_list[1])
        #     bonds_output.write(bonds_data)
                # print residue_name[1]
    # for line in input_topo:
    #     if line.startswith(';'):
    #         continue
    #     data.append(line)
    #     if len(line)-len(line.lstrip()) <= 2:
    #         atoms_list+=line.split()
    #         print atoms_list
#            x=data2.split()
#            print x
#            for i in
#            if line.startswith('[') and len(line)<=9:
#            residue_name=line.split()
#            print residue_name[1]
        # if line.startswith('  ') and len(line) in range(26:37):
            # atoms_list = line.split()
            # residue_name.append(residue_name)

          # words = re.compile(r'^[A-Z\d]+$',residue_name)
            # residue_list =residue_name.append()
            # for i in range(0,len()) residue_name:
            # test.append(residue_name[1])
            # print test

            # print residue_name[1]

                            # for items in lines(len(lines))
            # print items
            # atom_list=''
            # if line.startswith('  '):
                # atom_list=line.split()
                # print res_name[1]+'\t'+atom_list[0]
        #print res_name#+'\t'+atom_list[:-1]


        # if line.startswith(';'):
        #     continue
        # else:
        #     data+=line
        # # if data.startswith('[') and data[2:5].isalpha():
        # #     res_name+=data[2:5]
        #     print data

# import numpy as np
# from StringIO import StringIO

# def read_topo(li):

#topo_filename = sys.argv[1]


#
#residue_name=[]
#atom_list=[]
#test=[]

# if (len(args) <= 1):
#     print 'Must provide input files'
# parser = argparse.ArgumentParser()
# parser.add_argument("p", help="")
# parser.add_argument("-v", "--verbosity", action="count",
#                     help="increase output verbosity")

#Help
# def main(argv):
#    inputfile = ''
#    outputfile = ''
#    try:
#       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#    except getopt.GetoptError:
#       print 'test.py -i <inputfile> -o <outputfile>'
#       sys.exit(2)
#    for opt, arg in opts:
#       if opt == '-h':
#          print 'test.py -i <inputfile> -o <outputfile>'
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = arg
#       elif opt in ("-o", "--ofile"):
#          outputfile = arg
#    print 'Input file is "', inputfile
#    print 'Output file is "', outputfile

# if __name__ == "__main__":
#    main(sys.argv[1:])

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print 'cannot open', arg
#     # else:
    #     print arg, 'has', len(f.readlines()), 'lines'
    #     f.close()
# pdb_filename = sys.argv[1]

# except:
#     print "USAGE:\n\t./parser.py pdb_filename rtp_filename"
#     sys.exit(0)

# with open(topo_filename) as input_topo:
#     topo_data = input_topo.read()



        # if data.find('atoms'):
        #     continue
        # atom_list=''
        # if data.startswith('  ') and data[21:31].isdigit():
        #     atom_list+=data.split()
        #     print res_name+'\t'+atom_list


#         residue_list=''
#         atom_list=''
# if res_name[-3:] in ['ALA','CYS','ASP','GLU','PHE','GLY','HIS','ILE','LYS',\
# 'LEU','MET','ASN','PYL','PRO','GLN','ARG','SER','THR','SEC','VAL',\
# 'TRP','TYR','HSD']:


# for i in pdb_filename:
# with open(pdb_filename) as input_pdb:
#     for line in input_pdb:
#         pdb_key=''
#         if line.startswith('ATOM'):
#             key1 = line[17:20]+'\t\t'+line[12:16]
#             under1=key1.replace (" ", "_")
#             #print under1
#             pdb_key += under1

#             print (pdb_key)
#         elif line.startswith('HETATM'):
#             key2=line[17:20]+'\t\t'+line[12:16]
#             under2=key2.replace (" ", "_")
#             pdb_key += under2
#             print (pdb_key)



# print ('================')
# print(topo_data)
# print ('================')




# def redfile():

# myarray = {}
# for line in open(file, 'r'):
#     x = prog.match(line)
#     myarray[x.group(1)] = [x.group(2)]

# try:
#     pdb_filename = sys.argv[1]
#     rtp_filename = sys.argv[2]
# except:
#     print "USAGE:\n\t./protein_dihedrals.py pdb_filename"
#     sys.exit(0)
# with open('test.txt') as input_data:
#     # Skips text before the beginning of the interesting block:
#     for line in input_data:
#         if line.strip() == 'Start':  # Or whatever test is needed
#             break
#     # Reads text until the end of the block:
#     for line in input_data:  # This keeps reading the file
#         if line.strip() == 'End':
#             break
#         print line  # Line is extracted (or block_of_lines.append(line), etc.)
# def isPro(res_name):
#     """Takes a string and returns a bool.  True if the string represents a
#     nucleoside, false otherwise."""
#     if res_name[-3:] in ['ALA','CYS','ASP','GLU','PHE','GLY','HIS','ILE','LYS',\
#              'LEU','MET','ASN','PYL','PRO','GLN','ARG','SER','THR','SEC','VAL',\
#              'TRP','TYR','HSD']:
#         return True
#     else:
#         return False

#         def is_backbone(atom_type):
#     """Takes a 4 character string representing an atom_type and returns a bool.
#     True if the atom_type represents a back_bone atom in a protein, false otherwise."""
#     if atom_type in [' N  ',' CA ',' C  ',' O  ',' OT1']:
#         return True
#     else:
#         return False

# def

# from itertools import takewhile

# is_delimiter = ' '.__eq__
# def build_tree(lines):
#     lines = iter(lines)
#     stack =[]
#     for line in lines:
#         indent = len(list(takewhile(is_delimiter, line)))
#         stack[indent:] = [line.lstrip()]
#         return stack

# def read_atoms(lines):
#
#     if line.startswith(';'):
#         continue
#     for line in input_topo:
#         if line.find('atoms'):
#             continue
#         if parsing:
#             x = build_tree(line.split('\n'))
