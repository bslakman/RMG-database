#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/Hexanethial_nr"
shortDesc = u""
longDesc = u"""

"""
#entry(
#    index = 1,
#    label = "C6H12SHOH <=> C6H12O + H2S",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(3.43e+14, 's^-1'), n=-0.41, Ea=(44.42, 'kcal/mol'), T0=(1, 'K')),
#    longDesc = 
#u"""
#First one should be 36.30 kcal/mol, second 44.42 kcal/mol
#C6H12O + H2S = C6H12SHOH    6.13E+01    2.77    36.30    0.0    0.0    0.0
#""",
#)
#
entry(
    index = 1,
    label = "C5H11COHS <=> C5H11COSH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(59, 's^-1'), n=3.27, Ea=(19.59, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Correct value of next reaction is in R_Addition_MultipleBond
C5H11COHS + HJ = C5H11CJOHSH    1.18E+09    1.15    -0.06    0.0    0.0    0.0
""",
)

#entry(
#    index = 3,
#    label = "C5H11J + COS <=> C5H11COSJ",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (8.02E+06, 'cm^3/(mol*s)'),
#        n = 1.68,
#        Ea = (12.09, 'kcal/mol'),
#        T0 = (1, 'K'),
#    ),
#)
#
#entry(
#    index = 4,
#    label = "CHOHS + C5H11J <=> C6H12OHSJ",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(760, 'cm^3/(mol*s)'), n=2.56, Ea=(3.56, 'kcal/mol'), T0=(1, 'K')),
#)
#
#entry(
#    index = 5,
#    label = "C4H9CHJCHOHSH <=> SH + hexen-1-ol",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(1.92e+12, 's^-1'), n=0.14, Ea=(5.35, 'kcal/mol'), T0=(1, 'K')),
#    longDesc = 
#u"""
#reverse of reaction is in R_Addition_MultipleBond library:
#""",
#)

#entry(
#    index = 6,
#    label = "hexen-1-ol <=> C6H12O",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(5.32e-33, 's^-1'), n=12.94, Ea=(31.33, 'kcal/mol'), T0=(1, 'K')),
#)
#
#entry(
#    index = 7,
#    label = "CO + H2O <=> CO2 + H2",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(5000, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
#    longDesc = 
#u"""
#Approx water gas shift reaction
#""",
#)

entry(
    index = 2,
    label = "C6H12S + H2O <=> C6H12SHOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00133, 'cm^3/(mol*s)'),
        n = 3.95,
        Ea = (24.55, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
	longDesc = 
	u"""
	Divided A-factor by 2 to account for activity of SCW
	""",
)

entry(
    index = 3,
    label = "C6H12SHOH + H2O <=> C6H12O + H2S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.125, 'cm^3/(mol*s)'),
        n = 3.07,
        Ea = (22.27, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
	longDesc = 
	u"""
	Using F12 calculations for 1st one, and divided by 2 to account for SCW activity
	""",
)

entry(
    index = 4,
    label = "C6H12SHOH + H2S <=> C6H12O + H2S + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.172, 'cm^3/(mol*s)'), n=3.43, Ea=(27.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "C6H12SHOH + H2O <=> C6H12S + H2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.6, 'cm^3/(mol*s)'), n=2.56, Ea=(20.55, 'kcal/mol'), T0=(1, 'K')),
	longDesc = 
	u"""
	Divide by 2 for forward direction (should actually divide by 4 for reverse...)
	""",
)

entry(
    index = 6,
    label = "C6H12SHOH + H2S <=> C6H12S + H2O + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.14, 'cm^3/(mol*s)'), n=2.93, Ea=(28.62, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "C6H9SJ + C6H11SH <=> C6H10S + C6H11SJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(317, 'cm^3/(mol*s)'), n=3.17, Ea=(-4.8, 'kcal/mol'), T0=(1, 'K')),
	longDesc = 
	u"""
	Reverse reaction available in H_abs library
	""",
)

entry(
    index = 8,
    label = "C6H12S + HS2 <=> C6H13SJ + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9710, 'cm^3/(mol*s)'), n=1.37, Ea=(17.76, 'kcal/mol'), T0=(1, 'K')),
	longDesc = 
	u"""
	Reverse of these reactions has large negative Ea
	""",
)

entry(
    index = 9,
    label = "C6H9SH + HS2 <=> C6H10JSH + S2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.35, 'cm^3/(mol*s)'), n=3.27, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "delta-DHS <=> Et-THT + C6H13J",
    degeneracy = 1,
    kinetics = Arrhenius(A=(78900, 's^-1'), n=1.26, Ea=(9.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "C6H11SH + C6H11SJ <=> C6H11SJ + C6H12S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(82, 'cm^3/(mol*s)'), n=3.06, Ea=(7.7, 'kcal/mol'), T0=(1, 'K')),
	longDesc = 
	u"""
	These are close to deltaH=0, so RMG had trouble finding rate constants (which were calculated by AGV) H_Abs group reactions 6211,6131,
	""",
)

entry(
    index = 12,
    label = "H2S + C6H10JSH <=> SH + C6H11SH-2e",
    degeneracy = 1,
    kinetics = Arrhenius(A=(60.8, 'cm^3/(mol*s)'), n=3.06, Ea=(9.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "H2S + C6H10JSH-b <=> SH + C6H11SH-2e",
    degeneracy = 1,
    kinetics = Arrhenius(A=(116, 'cm^3/(mol*s)'), n=3.06, Ea=(7.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "C6H8S <=> VinylDHT",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+09, 's^-1'), n=0.545, Ea=(37.5, 'kcal/mol'), T0=(1, 'K')),
	longDesc = 
	u"""
	ene addition reactions to form vinyl-dihydrothiophene:
	""",
)

entry(
    index = 15,
    label = "Hexenethial <=> VinylTHT",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.3, 's^-1'), n=2.437, Ea=(24.18, 'kcal/mol'), T0=(1, 'K')),
)

