#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/training"
shortDesc = u"A list of solvation reactions used to train group additivity values"
longDesc = u"""
"""
entry(
    index = 1,
    reactants = ['CH3', 'CH4'], 
    solvent = 'water',
    barrierCorrection = (-4.4, 'kJ/mol'),
    shortDesc = u"""MO6-2X/MG3S calculations in g09 with SMD solvation model""",
    longDesc = 
u"""
"""
)

entry(
    index = 2,
    reactants = ['OH', 'CH4'], 
    solvent = 'water',
    barrierCorrection = (-3.2, 'kJ/mol'),
    shortDesc = u"""MO6-2X/MG3S calculations in g09 with SMD solvation model""",
    longDesc = 
u"""
"""
)

entry(
    index = 3,
    reactants = ['OOH', 'CH4'],
    solvent = 'water',
    barrierCorrection = (-2.6, 'kJ/mol'),
    shortDesc = u"""MO6-2X/MG3S calculations in g09 with SMD solvation model""",
    longDesc = 
u"""
"""
)

