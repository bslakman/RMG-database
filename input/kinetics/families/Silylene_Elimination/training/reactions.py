#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Elimination/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
#entry(
#    index = 1,
#    label = "SiH4 + Ar <=> SiH2 + H2 + Ar",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (7.2E15, 'cm^3/(mol*s)'),
#        n = 1,
#        Ea = (45.1, 'kcal/mol'),
#        T0 = (1, 'K'),
#        Tmin = (1060, 'K'),
#        Tmax = (1730, 'K'),
#    ),
#    reference = Article(
#        authors = ["Petersen, E.L.", "Crofton, M.W."],
#        title = "Measurements of high-temperature silane pyrolysis using SiH4 IR emission and SiH2 laser absorption",
#        journal = "J. Phys. Chem. A",
#        pages = """10988-10995""",
#        year = "2003",
#    ),
#    longDesc = 
#u"""
#Shock tube experiment where species concentrations are measured by IR emission of SiH4 and laser absorption of SiH2. Error in Ea +/- 1.2 kcal/mol. Competing reactions were accounted for by the mechanism proposed by Woiki et al., Ceram. Process. 1997.
#""",
#)

entry(
    index = 2,
    label = "Si2H6 <=> SiH2 + SiH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7E15, '1/s'),
        n = 1,
        Ea = (215.677, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Matsumoto, K.", "Klippenstein, S.J.", "Tonokura, K.", "Koshi, T."],
        title = "Channel specific rate constants relevant to the thermal decomposition of disilane",
        journal = "J. Phys. Chem. A",
        pages = """4911-4920""",
        year = "2005",
    ),
    longDesc = 
u"""
Potential energy surface was calculated with G3/B3LYP//6-3111++G(d,p) basis set, VARIFLEX was used to compute rate expressions from TST.
""",
)
