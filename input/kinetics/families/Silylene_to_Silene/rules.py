#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_to_Silene/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')


.. [MRHCBSQB3RRHO] M.R. Harper (mrharper_at_mit_dot_edu or michael.harper.jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 calculations.  The zero-point
energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the 
temperatures used were: 300, 331, 370, 419, 482, 568, 692, 885, 1227, 2000 (evenly spaced on inverse temperature scale).

.. [Tsang1990] W. Tsang; "Chemical kinetic database for combustion chemistry. Part IV. Isobutane" J. Phys. Chem. Ref. Data 19 (1990) 1-68

.. [Tsang1991] W. Tsang; "Chemical kinetic database for combustion chemistry. Part V. Propene" J. Phys. Chem. Ref. Data 20 (1991) 221-273
"""
entry(
        index = 1,
        label = "SiRYSiH",
        kinetics = ArrheniusEP(
                A = (7.9E12, 'cm^3/(mol*s)'),
                n = 0,
                alpha = 0,
                E0 = (5.3095, 'kJ/mol'),
                Tmin = (300, 'K'),
                Tmax = (1600, 'K'),
        ),
        rank = 1,
        shortDesc = u"""Top level node""",
        longDesc =
u"""
Rate is from the reaction H3Si-SiH <-> H2Si=SiH2, high P limit of QRRK calcs. From Dollet and de Persis, J. Anal. Apply. Pyrolysis, 2007, 460-470.
""",
)

