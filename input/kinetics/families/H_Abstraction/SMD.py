#!/usr/bin/env python
# encoding: utf-8

# A script for gathering the SMD barrier correction values from Gaussian jobs.

import os.path
import argparse
from rmgpy.molecule import Molecule

parser = argparse.ArgumentParser(description="""
Given solvent, will get the delEa values from the output files.
""")
parser.add_argument("-s", "--solvent", help="Name of solvent, i.e. \'water\'")
args= parser.parse_args()

data_dir = '/Users/belinda/Code/Gaussian-log/SMD/H_Abs'
data_file = 'output_' + args.solvent + '.txt'
if not os.path.exists(os.path.join(os.getcwd(), args.solvent, 'training')):
    os.makedirs(os.path.join(os.getcwd(), args.solvent, 'training'))
output_file = os.path.join(os.getcwd(), args.solvent, 'training', 'solvationReactions.py')
output_dict = os.path.join(os.getcwd(), args.solvent, 'training', 'solvationDictionary.txt')

#print data_dir
#print data_file
#print output_file

out = open(output_file, 'w+')
out.write("""
#!/usr/bin/env python
# encoding: utf-8

name = \"H_Abstraction\/training\"
shortDesc = u\"A list of solvation reactions used to train group additivity values\"
longDesc = u\"\"\"
\"\"\"
"""
)
out.close()

index = 1
unique_reactants = {}

for subdir, dirs, files in os.walk(data_dir):
    reactionString = os.path.basename(os.path.normpath(subdir))
    if reactionString in ('H_Abs','solv2'): continue
    if not data_file in files: continue
    try: 
        reactants, products = reactionString.split("_")
    except:
        print("String {0} is wrong length".format(reactionString))
        raise
    if reactants in unique_reactants:
       unique_reactants[reactants] += 1
    else:
       unique_reactants.update({reactants: 1})
    try:
        r1, r2 = reactants.split("+") 
        p1, p2 = products.split("+")
    except:
        print("{0} or {1} is wrong length".format(reactants,products))
        raise
    if not unique_reactants[reactants] == 1:
       r2 = r2 + "-" + str(unique_reactants[reactants])
    f = open(os.path.join(subdir,data_file), 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
       if line.startswith("Difference"):
          text, barrierCorrection = line.split("= ")
    
    out = open(output_file, 'a')
    out.write('entry( \n')
    out.write('    index = ' + str(index) + ', \n') 
    out.write('    reactants = [\'' + r1 + '\', \'' + r2 + '\'], \n')
    out.write('    products = [\'' + p1 + '\', \'' + p2 + '\'], \n')
    out.write('    solvent = \'' + args.solvent + '\', \n')
    out.write('    correction = BarrierCorrection(correction = (' + barrierCorrection + ', \'kJ/mol\')), \n') 
    out.write('    shortDesc = u"""MO6-2X/MG3S calculations in g09 with SMD solvation model""", \n') 
    out.write('    longDesc = \n u\"\"\" \n \"\"\" \n )')
    out.write('\n')
    out.close()

    index += 1 

# Create the dictionary

    if os.path.exists(output_dict):
        d = open(output_dict, 'r')
    else: 
        d = open(output_dict, 'a+')
    entries = d.read().splitlines()
    d.close()
#    if not r1 in entries:
#        d = open(output_dict, 'a')
#        d.write(r1 + '\n')
#        d.write((Molecule().fromSMILES(r1)).toAdjacencyList() + '\n')
#        d.close()
#    if not r2 in entries:
#        d = open(output_dict, 'a')
#        d.write(r2 + '\n')
#        r2_SMILES = r2.split("-")[0]
#        d.write((Molecule().fromSMILES(r2_SMILES)).toAdjacencyList() + '\n')
#        d.close()
    if not p1 in entries:
        d = open(output_dict, 'a')
        d.write(p1 + '\n')
        d.write((Molecule().fromSMILES(p1)).toAdjacencyList() + '\n')
        d.close()
    if not p2 in entries:
        d = open(output_dict, 'a')
        d.write(p2 + '\n')
        d.write((Molecule().fromSMILES(p2)).toAdjacencyList() + '\n')
        d.close()
