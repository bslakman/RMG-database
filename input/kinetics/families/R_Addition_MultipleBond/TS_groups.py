#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/TS_groups"
shortDesc = u""
longDesc = u"""
The reaction site *3 should be a triplet, otherwise it will react via the 1+2_Cycloaddition family instead.
"""

entry(
    index = 1,
    label = "R_R",
    group = "OR{Cn_R, Od_R}",
    distances = DistanceData(
        distances = {'d12': 1.30691, 'd13': 2.00598, 'd23': 2.61304},
        uncertainties = {'d12': 0.068541, 'd13': 0.14532, 'd23': 0.229451},
    ),
    shortDesc = u"""Fitted to 161 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
[<Entry index=23 label="Od_Cds">, <Entry index=6 label="Cj">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=8 label="Cd_R">, <Entry index=5 label="Hj">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=16 label="OH">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 2,
    label = "YJ",
    group = "OR{Hj, Cj, Oj}",
    distances = DistanceData(distances={}),
)

entry(
    index = 3,
    label = "Cn_R",
    group = "OR{Cd_R, Ct_R}",
    distances = DistanceData(
        distances = {'d12': 0.004814, 'd13': 0.022924, 'd23': 0.011168},
        uncertainties = {'d12': 0.071184, 'd13': 0.14042, 'd23': 0.236037},
    ),
    shortDesc = u"""Fitted to 147 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=8 label="Cd_R">, <Entry index=5 label="Hj">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=16 label="OH">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 8,
    label = "Cd_R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u0 {2,D}
2 *2 R ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.011068, 'd13': 0.022107, 'd23': 0.006055},
        uncertainties = {'d12': 0.073371, 'd13': 0.141641, 'd23': 0.242523},
    ),
    shortDesc = u"""Fitted to 137 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=8 label="Cd_R">, <Entry index=5 label="Hj">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=16 label="OH">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 19,
    label = "Cds_R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D}
2 *2 R  ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.046145, 'd13': 0.059619, 'd23': 0.079059},
        uncertainties = {'d12': 0.032003, 'd13': 0.096332, 'd23': 0.175144},
    ),
    shortDesc = u"""Fitted to 91 distances.
""",
    longDesc = 
u"""
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=16 label="OH">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 36,
    label = "Cds_Cd_H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 [Cd,Cdd] ux {1,D}
3    H        u0 {1,S}
4    H        u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.044838, 'd13': 0.087215, 'd23': 0.146625},
        uncertainties = {'d12': 0.04085, 'd13': 0.113719, 'd23': 0.19849},
    ),
    shortDesc = u"""Fitted to 35 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=16 label="OH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 62,
    label = "Cds_Cds/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.047525, 'd13': 0.095329, 'd23': 0.149427},
        uncertainties = {'d12': 0.041669, 'd13': 0.109902, 'd23': 0.203388},
    ),
    shortDesc = u"""Fitted to 30 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
""",
)

entry(
    index = 63,
    label = "Cds_Cdd/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd ux {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.022576, 'd13': 0.019979, 'd23': 0.123401},
        uncertainties = {'d12': 0.057241, 'd13': 0.209266, 'd23': 0.269023},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 37,
    label = "Cds_Cd_RH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 [Cd,Cdd] ux {1,D}
3    R!H      ux {1,S}
4    H        u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.046852, 'd13': 0.054522, 'd23': 0.056383},
        uncertainties = {'d12': 0.028829, 'd13': 0.075251, 'd23': 0.140893},
    ),
    shortDesc = u"""Fitted to 37 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 64,
    label = "Cds_Cds/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.044645, 'd13': 0.052621, 'd23': 0.03912},
        uncertainties = {'d12': 0.032072, 'd13': 0.075238, 'd23': 0.151243},
    ),
    shortDesc = u"""Fitted to 24 distances.
""",
    longDesc = 
u"""
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
""",
)

entry(
    index = 65,
    label = "Cds_Cds/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cd ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.043908, 'd13': -0.013209, 'd23': 0.053462},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 66,
    label = "Cds_Cds/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 67,
    label = "Cds_Cds/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 68,
    label = "Cds_Cdd/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.038669, 'd13': 0.107851, 'd23': 0.211766},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 69,
    label = "Cds_Cdd/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cd  ux {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 70,
    label = "Cds_Cdd/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 71,
    label = "Cds_Cdd/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 38,
    label = "Cds_Cd_RR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 [Cd,Cdd] ux {1,D}
3    R!H      ux {1,S}
4    R!H      ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.04788, 'd13': -0.001113, 'd23': -0.044662},
        uncertainties = {'d12': 0.02397, 'd13': 0.116748, 'd23': 0.222229},
    ),
    shortDesc = u"""Fitted to 19 distances.
""",
    longDesc = 
u"""
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
""",
)

entry(
    index = 72,
    label = "Cds_Cds/Cs/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.044519, 'd13': 0.004628, 'd23': -0.070001},
        uncertainties = {'d12': 0.03255, 'd13': 0.12097, 'd23': 0.234528},
    ),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
""",
)

entry(
    index = 73,
    label = "Cds_Cds/Cs/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 74,
    label = "Cds_Cds/Cs/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 75,
    label = "Cds_Cds/Cs/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 76,
    label = "Cds_Cds/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 77,
    label = "Cds_Cds/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 78,
    label = "Cds_Cds/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 79,
    label = "Cds_Cds/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 80,
    label = "Cds_Cds/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 81,
    label = "Cds_Cds/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 82,
    label = "Cds_Cdd/Cs/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    Cs  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.025668, 'd13': -0.052769, 'd23': -0.043628},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 83,
    label = "Cds_Cdd/Cs/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    Cd  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 84,
    label = "Cds_Cdd/Cs/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 85,
    label = "Cds_Cdd/Cs/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 86,
    label = "Cds_Cdd/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cd  ux {1,S}
4    Cd  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 87,
    label = "Cds_Cdd/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cd  ux {1,S}
4    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 88,
    label = "Cds_Cdd/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cd  ux {1,S}
4    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 89,
    label = "Cds_Cdd/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 90,
    label = "Cds_Cdd/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Ct  u0 {1,S}
4    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 91,
    label = "Cds_Cdd/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cb  u0 {1,S}
4    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 39,
    label = "Cds_Od_H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 40,
    label = "Cds_Od_RH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 O   u0 {1,D}
3    H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 92,
    label = "Cds_Od/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    H  u0 {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 93,
    label = "Cds_Od/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    H  u0 {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 94,
    label = "Cds_Od/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    H  u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 95,
    label = "Cds_Od/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    H  u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 41,
    label = "Cds_Od_RR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 O   u0 {1,D}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 96,
    label = "Cds_Od/Cs/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 97,
    label = "Cds_Od/Cs/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 98,
    label = "Cds_Od/Cs/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 99,
    label = "Cds_Od/Cs/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 100,
    label = "Cds_Od/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 101,
    label = "Cds_Od/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 102,
    label = "Cds_Od/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 103,
    label = "Cds_Od/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 104,
    label = "Cds_Od/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 105,
    label = "Cds_Od/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 20,
    label = "Cdd_RR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D}
2 *2 R   ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.008736, 'd13': -0.019241, 'd23': -0.077754},
        uncertainties = {'d12': 0.022428, 'd13': 0.10898, 'd23': 0.166247},
    ),
    shortDesc = u"""Fitted to 11 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 42,
    label = "Cdd_CC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 C   ux {1,D}
3    C   ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.010153, 'd13': 0.118882, 'd23': 0.0259},
        uncertainties = {'d12': 0.029858, 'd13': 0.16237, 'd23': 0.146273},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
""",
)

entry(
    index = 106,
    label = "Cdd_Cds/Cds",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  ux {1,D}
3    Cd  ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.010153, 'd13': 0.118882, 'd23': 0.0259},
        uncertainties = {'d12': 0.029858, 'd13': 0.16237, 'd23': 0.146273},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
""",
)

entry(
    index = 107,
    label = "Cdd_Cds/Cdd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  ux {1,D}
3    Cdd u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 108,
    label = "Cdd_Cdd/Cdd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D}
3    Cdd u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 43,
    label = "Cdd_CO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 C   ux {1,D}
3    O   u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.026616, 'd13': -0.038166, 'd23': -0.07397},
        uncertainties = {'d12': 0.031167, 'd13': 0.134215, 'd23': 0.241811},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 109,
    label = "Cdd_Cds/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  ux {1,D}
3    O   u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.026616, 'd13': -0.038166, 'd23': -0.07397},
        uncertainties = {'d12': 0.031167, 'd13': 0.134215, 'd23': 0.241811},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 110,
    label = "Cdd_Cdd/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D}
3    O   u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 44,
    label = "CO2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O   u0 {1,D}
3    O   u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.085271, 'd13': -0.373519, 'd23': -0.433554},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 9,
    label = "Ct_R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u0 {2,T}
2 *2 R ux {1,T}
""",
    distances = DistanceData(
        distances = {'d12': -0.086349, 'd13': 0.034839, 'd23': 0.085692},
        uncertainties = {'d12': 0.035322, 'd13': 0.149579, 'd23': 0.145173},
    ),
    shortDesc = u"""Fitted to 10 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 21,
    label = "Ct_Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u0 {2,T} {3,S}
2 *2 C ux {1,T}
3    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.085946, 'd13': 0.06647, 'd23': 0.128448},
        uncertainties = {'d12': 0.045287, 'd13': 0.112232, 'd23': 0.075429},
    ),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 22,
    label = "Ct_Ct/R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C   u0 {2,T} {3,S}
2 *2 C   ux {1,T}
3    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.088165, 'd13': -0.107502, 'd23': -0.106708},
        uncertainties = {'d12': 0.035882, 'd13': 0.497388, 'd23': 0.53881},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 45,
    label = "Ct_Ct/C",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u0 {2,T} {3,S}
2 *2 C ux {1,T}
3    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.088165, 'd13': -0.107502, 'd23': -0.106708},
        uncertainties = {'d12': 0.035882, 'd13': 0.497388, 'd23': 0.53881},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 111,
    label = "Ct_Ct/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C  u0 {2,T} {3,S}
2 *2 C  ux {1,T}
3    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.090792, 'd13': -0.100709, 'd23': -0.119628},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 112,
    label = "Ct_Ct/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C  u0 {2,T} {3,S}
2 *2 C  ux {1,T}
3    Cd ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.087922, 'd13': -0.103279, 'd23': -0.112178},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 113,
    label = "Ct_Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C  u0 {2,T} {3,S}
2 *2 C  ux {1,T}
3    Ct u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.085782, 'd13': -0.118519, 'd23': -0.088318},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 114,
    label = "Ct_Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C  u0 {2,T} {3,S}
2 *2 C  ux {1,T}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 46,
    label = "Ct_Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u0 {2,T} {3,S}
2 *2 C ux {1,T}
3    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 4,
    label = "Od_R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O u0 {2,D}
2 *2 R ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.066872, 'd13': -0.318458, 'd23': -0.155146},
        uncertainties = {'d12': 0.034517, 'd13': 0.215441, 'd23': 0.166565},
    ),
    shortDesc = u"""Fitted to 14 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
[<Entry index=23 label="Od_Cds">, <Entry index=6 label="Cj">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 10,
    label = "Od_C",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O u0 {2,D}
2 *2 C ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.066872, 'd13': -0.318458, 'd23': -0.155146},
        uncertainties = {'d12': 0.034517, 'd13': 0.215441, 'd23': 0.166565},
    ),
    shortDesc = u"""Fitted to 14 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
[<Entry index=23 label="Od_Cds">, <Entry index=6 label="Cj">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 23,
    label = "Od_Cds",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C ux {2,D} {3,S}
2 *1 O u0 {1,D}
3    R ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.059243, 'd13': -0.355018, 'd23': -0.162177},
        uncertainties = {'d12': 0.038133, 'd13': 0.226216, 'd23': 0.17681},
    ),
    shortDesc = u"""Fitted to 12 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=6 label="Cj">]
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
""",
)

entry(
    index = 24,
    label = "Od_Cdd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C ux {2,D} {3,D}
2 *1 O u0 {1,D}
3    R ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.090606, 'd13': -0.204716, 'd23': -0.133269},
        uncertainties = {'d12': 0.051739, 'd13': 1.45342, 'd23': 1.00785},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
""",
)

entry(
    index = 11,
    label = "O2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O u0 {2,D}
2 *2 O u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 5,
    label = "Hj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 H u1
""",
    distances = DistanceData(
        distances = {'d12': -0.013618, 'd13': -0.188775, 'd23': -0.204495},
        uncertainties = {'d12': 0.077695, 'd13': 0.153293, 'd23': 0.221358},
    ),
    shortDesc = u"""Fitted to 44 distances.
""",
    longDesc = 
u"""
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=5 label="Hj">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 6,
    label = "Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 C u1
""",
    distances = DistanceData(
        distances = {'d12': -0.009356, 'd13': 0.140939, 'd23': 0.164189},
        uncertainties = {'d12': 0.075405, 'd13': 0.156782, 'd23': 0.277469},
    ),
    shortDesc = u"""Fitted to 79 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=23 label="Od_Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 12,
    label = "Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1
""",
    distances = DistanceData(
        distances = {'d12': -0.011146, 'd13': 0.151929, 'd23': 0.192037},
        uncertainties = {'d12': 0.076189, 'd13': 0.128247, 'd23': 0.225101},
    ),
    shortDesc = u"""Fitted to 56 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 25,
    label = "Csj_methyl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.001821, 'd13': 0.164062, 'd23': 0.213849},
        uncertainties = {'d12': 0.071514, 'd13': 0.124602, 'd23': 0.216828},
    ),
    shortDesc = u"""Fitted to 30 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 26,
    label = "Csj_RH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.015032, 'd13': 0.15125, 'd23': 0.182898},
        uncertainties = {'d12': 0.094718, 'd13': 0.147599, 'd23': 0.275736},
    ),
    shortDesc = u"""Fitted to 19 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
""",
)

entry(
    index = 47,
    label = "Csj_CH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.020886, 'd13': 0.138752, 'd23': 0.183663},
        uncertainties = {'d12': 0.107316, 'd13': 0.153152, 'd23': 0.281703},
    ),
    shortDesc = u"""Fitted to 12 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
""",
)

entry(
    index = 115,
    label = "Csj_Cs/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.026597, 'd13': 0.136428, 'd23': 0.182},
        uncertainties = {'d12': 0.112974, 'd13': 0.161227, 'd23': 0.294817},
    ),
    shortDesc = u"""Fitted to 11 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
""",
)

entry(
    index = 116,
    label = "Csj_Cd/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 117,
    label = "Csj_Ct/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 118,
    label = "Csj_Cb/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 48,
    label = "Csj_OH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.00625, 'd13': 0.169996, 'd23': 0.181751},
        uncertainties = {'d12': 0.102044, 'd13': 0.188433, 'd23': 0.359981},
    ),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
""",
)

entry(
    index = 27,
    label = "Csj_RRH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.055278, 'd13': 0.079008, 'd23': 0.088991},
        uncertainties = {'d12': 0.086227, 'd13': 0.169405, 'd23': 0.240384},
    ),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
""",
)

entry(
    index = 49,
    label = "Csj_CCH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.080325, 'd13': 0.026069, 'd23': 0.001696},
        uncertainties = {'d12': 0.01925, 'd13': 0.256299, 'd23': 0.318308},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
""",
)

entry(
    index = 119,
    label = "Csj_Cs/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.083058, 'd13': 0.034821, 'd23': 0.019877},
        uncertainties = {'d12': 0.031009, 'd13': 0.412083, 'd23': 0.499947},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
""",
)

entry(
    index = 120,
    label = "Csj_Cs/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 121,
    label = "Csj_Cs/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 122,
    label = "Csj_Cs/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 123,
    label = "Csj_Cd/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 124,
    label = "Csj_Cd/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 125,
    label = "Csj_Cd/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 126,
    label = "Csj_Ct/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 127,
    label = "Csj_Ct/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 128,
    label = "Csj_Cb/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 50,
    label = "Csj_COH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.030231, 'd13': 0.131946, 'd23': 0.176287},
        uncertainties = {'d12': 0.260676, 'd13': 0.293416, 'd23': 0.508137},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
""",
)

entry(
    index = 129,
    label = "Csj_Cs/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.030231, 'd13': 0.131946, 'd23': 0.176287},
        uncertainties = {'d12': 0.260676, 'd13': 0.293416, 'd23': 0.508137},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
""",
)

entry(
    index = 130,
    label = "Csj_Cd/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 131,
    label = "Csj_Ct/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 132,
    label = "Csj_Cb/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 51,
    label = "Csj_OOH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 28,
    label = "Csj_RRR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 52,
    label = "Csj_CCC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 133,
    label = "Csj_Cs/Cs/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 134,
    label = "Csj_Cs/Cs/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 135,
    label = "Csj_Cs/Cs/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 136,
    label = "Csj_Cs/Cs/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 137,
    label = "Csj_Cs/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 138,
    label = "Csj_Cs/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 139,
    label = "Csj_Cs/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 140,
    label = "Csj_Cs/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 141,
    label = "Csj_Cs/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 142,
    label = "Csj_Cs/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 143,
    label = "Csj_Cd/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 144,
    label = "Csj_Cd/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 145,
    label = "Csj_Cd/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 146,
    label = "Csj_Cd/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 147,
    label = "Csj_Cd/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 148,
    label = "Csj_Cd/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 149,
    label = "Csj_Ct/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 150,
    label = "Csj_Ct/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 151,
    label = "Csj_Ct/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 152,
    label = "Csj_Cb/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 53,
    label = "Csj_CCO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 153,
    label = "Csj_Cs/Cs/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 154,
    label = "Csj_Cs/Cd/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 155,
    label = "Csj_Cs/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 156,
    label = "Csj_Cs/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 157,
    label = "Csj_Cd/Cd/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 158,
    label = "Csj_Cd/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 159,
    label = "Csj_Cd/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 160,
    label = "Csj_Ct/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 161,
    label = "Csj_Ct/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 162,
    label = "Csj_Cb/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 54,
    label = "Csj_COO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 163,
    label = "Csj_Cs/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 164,
    label = "Csj_Cd/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 165,
    label = "Csj_Ct/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 166,
    label = "Csj_Cb/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 55,
    label = "Csj_OOO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 13,
    label = "Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1
""",
    distances = DistanceData(
        distances = {'d12': -0.011518, 'd13': 0.174154, 'd23': 0.213491},
        uncertainties = {'d12': 0.096791, 'd13': 0.10842, 'd23': 0.224619},
    ),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 29,
    label = "Cdj_Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd       u1 {2,D}
2    [Cd,Cdd] ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.011518, 'd13': 0.174154, 'd23': 0.213491},
        uncertainties = {'d12': 0.096791, 'd13': 0.10842, 'd23': 0.224619},
    ),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 56,
    label = "Cdj_CdH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    H        u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.042949, 'd13': 0.19899, 'd23': 0.219618},
        uncertainties = {'d12': 0.160369, 'd13': 0.185397, 'd23': 0.40301},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 167,
    label = "Cdj_CdsH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.042949, 'd13': 0.19899, 'd23': 0.219618},
        uncertainties = {'d12': 0.160369, 'd13': 0.185397, 'd23': 0.40301},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 168,
    label = "Cdj_CddH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 57,
    label = "Cdj_CdC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    C        ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.007108, 'd13': 0.159436, 'd23': 0.20986},
        uncertainties = {'d12': 0.111716, 'd13': 0.120248, 'd23': 0.231437},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
""",
)

entry(
    index = 169,
    label = "Cdj_Cds/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.026906, 'd13': 0.17346, 'd23': 0.227927},
        uncertainties = {'d12': 0.910613, 'd13': 0.603941, 'd23': 1.60655},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
""",
)

entry(
    index = 170,
    label = "Cdj_Cds/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cd ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.012607, 'd13': 0.261269, 'd23': 0.293125},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
""",
)

entry(
    index = 171,
    label = "Cdj_Cds/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 172,
    label = "Cdj_Cds/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 173,
    label = "Cdj_Cdd/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cs  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.029869, 'd13': 0.098002, 'd23': 0.154678},
        uncertainties = {'d12': 0.373695, 'd13': 0.694911, 'd23': 0.875222},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
""",
)

entry(
    index = 174,
    label = "Cdj_Cdd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cd  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 175,
    label = "Cdj_Cdd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 176,
    label = "Cdj_Cdd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 58,
    label = "Cdj_CdO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    O        ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 177,
    label = "Cdj_CdsO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 178,
    label = "Cdj_CddO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    O   ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 30,
    label = "Cdj_Od",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D}
2    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 59,
    label = "Cdj_OdH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 60,
    label = "Cdj_OdC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 179,
    label = "Cdj_OdCs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 180,
    label = "Cdj_OdCd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 181,
    label = "Cdj_OdCt",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 182,
    label = "Cdj_OdCb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 61,
    label = "Cdj_OdO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 14,
    label = "Ctj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Ct u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 31,
    label = "Ctj_Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 15,
    label = "Cbj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cb u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 7,
    label = "Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O u1
""",
    distances = DistanceData(
        distances = {'d12': 0.028842, 'd13': -0.054951, 'd23': -0.078873},
        uncertainties = {'d12': 0.043436, 'd13': 0.121996, 'd23': 0.118521},
    ),
    shortDesc = u"""Fitted to 38 distances.
""",
    longDesc = 
u"""
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=16 label="OH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
""",
)

entry(
    index = 16,
    label = "OH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.011601, 'd13': 0.054649, 'd23': -0.101109},
        uncertainties = {'d12': 0.052378, 'd13': 0.178263, 'd23': 0.116005},
    ),
    shortDesc = u"""Fitted to 12 distances.
""",
    longDesc = 
u"""
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
""",
)

entry(
    index = 17,
    label = "OjC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O u1 {2,S}
2    C ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 32,
    label = "OjCs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O  u1 {2,S}
2    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 33,
    label = "OjCd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O  u1 {2,S}
2    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 34,
    label = "OjCt",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O  u1 {2,S}
2    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 35,
    label = "OjCb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O  u1 {2,S}
2    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 18,
    label = "OjO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O u1 {2,S}
2    O ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.036279, 'd13': -0.102229, 'd23': -0.069281},
        uncertainties = {'d12': 0.042755, 'd13': 0.102542, 'd23': 0.127653},
    ),
    shortDesc = u"""Fitted to 26 distances.
""",
    longDesc = 
u"""
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
""",
)

tree(
"""
L1: R_R
    L2: Cn_R
        L3: Cd_R
            L4: Cds_R
                L5: Cds_Cd_H2
                    L6: Cds_Cds/H2
                    L6: Cds_Cdd/H2
                L5: Cds_Cd_RH
                    L6: Cds_Cds/Cs/H
                    L6: Cds_Cds/Cd/H
                    L6: Cds_Cds/Ct/H
                    L6: Cds_Cds/Cb/H
                    L6: Cds_Cdd/Cs/H
                    L6: Cds_Cdd/Cd/H
                    L6: Cds_Cdd/Ct/H
                    L6: Cds_Cdd/Cb/H
                L5: Cds_Cd_RR
                    L6: Cds_Cds/Cs/Cs
                    L6: Cds_Cds/Cs/Cd
                    L6: Cds_Cds/Cs/Ct
                    L6: Cds_Cds/Cs/Cb
                    L6: Cds_Cds/Cd/Cd
                    L6: Cds_Cds/Cd/Ct
                    L6: Cds_Cds/Cd/Cb
                    L6: Cds_Cds/Ct/Ct
                    L6: Cds_Cds/Ct/Cb
                    L6: Cds_Cds/Cb/Cb
                    L6: Cds_Cdd/Cs/Cs
                    L6: Cds_Cdd/Cs/Cd
                    L6: Cds_Cdd/Cs/Ct
                    L6: Cds_Cdd/Cs/Cb
                    L6: Cds_Cdd/Cd/Cd
                    L6: Cds_Cdd/Cd/Ct
                    L6: Cds_Cdd/Cd/Cb
                    L6: Cds_Cdd/Ct/Ct
                    L6: Cds_Cdd/Ct/Cb
                    L6: Cds_Cdd/Cb/Cb
                L5: Cds_Od_H2
                L5: Cds_Od_RH
                    L6: Cds_Od/Cs/H
                    L6: Cds_Od/Cd/H
                    L6: Cds_Od/Ct/H
                    L6: Cds_Od/Cb/H
                L5: Cds_Od_RR
                    L6: Cds_Od/Cs/Cs
                    L6: Cds_Od/Cs/Cd
                    L6: Cds_Od/Cs/Ct
                    L6: Cds_Od/Cs/Cb
                    L6: Cds_Od/Cd/Cd
                    L6: Cds_Od/Cd/Ct
                    L6: Cds_Od/Cd/Cb
                    L6: Cds_Od/Ct/Ct
                    L6: Cds_Od/Ct/Cb
                    L6: Cds_Od/Cb/Cb
            L4: Cdd_RR
                L5: Cdd_CC
                    L6: Cdd_Cds/Cds
                    L6: Cdd_Cds/Cdd
                    L6: Cdd_Cdd/Cdd
                L5: Cdd_CO
                    L6: Cdd_Cds/O
                    L6: Cdd_Cdd/O
                L5: CO2
        L3: Ct_R
            L4: Ct_Ct/H
            L4: Ct_Ct/R
                L5: Ct_Ct/C
                    L6: Ct_Ct/Cs
                    L6: Ct_Ct/Cd
                    L6: Ct_Ct/Ct
                    L6: Ct_Ct/Cb
                L5: Ct_Ct/O
    L2: Od_R
        L3: Od_C
            L4: Od_Cds
            L4: Od_Cdd
        L3: O2
L1: YJ
    L2: Hj
    L2: Cj
        L3: Csj
            L4: Csj_methyl
            L4: Csj_RH2
                L5: Csj_CH2
                    L6: Csj_Cs/H2
                    L6: Csj_Cd/H2
                    L6: Csj_Ct/H2
                    L6: Csj_Cb/H2
                L5: Csj_OH2
            L4: Csj_RRH
                L5: Csj_CCH
                    L6: Csj_Cs/Cs/H
                    L6: Csj_Cs/Cd/H
                    L6: Csj_Cs/Ct/H
                    L6: Csj_Cs/Cb/H
                    L6: Csj_Cd/Cd/H
                    L6: Csj_Cd/Ct/H
                    L6: Csj_Cd/Cb/H
                    L6: Csj_Ct/Ct/H
                    L6: Csj_Ct/Cb/H
                    L6: Csj_Cb/Cb/H
                L5: Csj_COH
                    L6: Csj_Cs/O/H
                    L6: Csj_Cd/O/H
                    L6: Csj_Ct/O/H
                    L6: Csj_Cb/O/H
                L5: Csj_OOH
            L4: Csj_RRR
                L5: Csj_CCC
                    L6: Csj_Cs/Cs/Cs
                    L6: Csj_Cs/Cs/Cd
                    L6: Csj_Cs/Cs/Ct
                    L6: Csj_Cs/Cs/Cb
                    L6: Csj_Cs/Cd/Cd
                    L6: Csj_Cs/Cd/Ct
                    L6: Csj_Cs/Cd/Cb
                    L6: Csj_Cs/Ct/Ct
                    L6: Csj_Cs/Ct/Cb
                    L6: Csj_Cs/Cb/Cb
                    L6: Csj_Cd/Cd/Cd
                    L6: Csj_Cd/Cd/Ct
                    L6: Csj_Cd/Cd/Cb
                    L6: Csj_Cd/Ct/Ct
                    L6: Csj_Cd/Ct/Cb
                    L6: Csj_Cd/Cb/Cb
                    L6: Csj_Ct/Ct/Ct
                    L6: Csj_Ct/Ct/Cb
                    L6: Csj_Ct/Cb/Cb
                    L6: Csj_Cb/Cb/Cb
                L5: Csj_CCO
                    L6: Csj_Cs/Cs/O
                    L6: Csj_Cs/Cd/O
                    L6: Csj_Cs/Ct/O
                    L6: Csj_Cs/Cb/O
                    L6: Csj_Cd/Cd/O
                    L6: Csj_Cd/Ct/O
                    L6: Csj_Cd/Cb/O
                    L6: Csj_Ct/Ct/O
                    L6: Csj_Ct/Cb/O
                    L6: Csj_Cb/Cb/O
                L5: Csj_COO
                    L6: Csj_Cs/O/O
                    L6: Csj_Cd/O/O
                    L6: Csj_Ct/O/O
                    L6: Csj_Cb/O/O
                L5: Csj_OOO
        L3: Cdj
            L4: Cdj_Cd
                L5: Cdj_CdH
                    L6: Cdj_CdsH
                    L6: Cdj_CddH
                L5: Cdj_CdC
                    L6: Cdj_Cds/Cs
                    L6: Cdj_Cds/Cd
                    L6: Cdj_Cds/Ct
                    L6: Cdj_Cds/Cb
                    L6: Cdj_Cdd/Cs
                    L6: Cdj_Cdd/Cd
                    L6: Cdj_Cdd/Ct
                    L6: Cdj_Cdd/Cb
                L5: Cdj_CdO
                    L6: Cdj_CdsO
                    L6: Cdj_CddO
            L4: Cdj_Od
                L5: Cdj_OdH
                L5: Cdj_OdC
                    L6: Cdj_OdCs
                    L6: Cdj_OdCd
                    L6: Cdj_OdCt
                    L6: Cdj_OdCb
                L5: Cdj_OdO
        L3: Ctj
            L4: Ctj_Ct
        L3: Cbj
    L2: Oj
        L3: OH
        L3: OjC
            L4: OjCs
            L4: OjCd
            L4: OjCt
            L4: OjCb
        L3: OjO
"""
)

