# Program reads par file and crewrites PDB atom name convention

import sys,os,re,csv,fileinput,glob


#Removes blank lines
def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

name = sys.argv[1]

with open('.par/'+name+'.ff_atoms.par','r') as par_input, open('.par/'+name+'.ff_name2pdb.par','w') as output:
    for line in par_input:
        if line.startswith(' '):
            continue
        lines = line.split()

       	x=[]
       	x=lines
       	# x[3]='{:_4^	s}'.format(x[3])
        x[3] = '{:_^4}'.format(x[3])
        # print x
        # print len(x)
        # print x,type(x)
        if len(x)==6:
      		x='{}\t{}\t{}\t{}\t{}\t{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5])
        if len(x)==7:
        	x='{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
        if len(x)==8:
        	x='{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
        if len(x)==9:
        	x='{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
        if len(x)==10:
        	x='{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9])
        if len(x)==11:
        	x='{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10])
        output.write(x)



