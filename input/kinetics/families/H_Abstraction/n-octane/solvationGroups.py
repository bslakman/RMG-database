#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/solvationGroups"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "X_H_or_Xrad_H_Xbirad_H_Xtrirad_H",
    group = "OR{X_H, Xrad_H, Xbirad_H, Xtrirad_H}",
    correction = BarrierCorrection(
        correction = (1373.009962164701, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 47 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=74 label="C/H3/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=60 label="Cs_H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=261 label="C_methyl">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=64 label="C_alkane">, <Entry index=261 label="C_methyl">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=87 label="C/H2/NonDeC_6ring">, <Entry index=261 label="C_methyl">]
[<Entry index=60 label="Cs_H">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C_alkane">, <Entry index=193 label="O_pri_rad">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=64 label="C_alkane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 2,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_2centeradjbirad, Y_1centerbirad, Y_rad, Y_1centertrirad, Y_1centerquadrad}",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "Xrad_H",
    group = 
"""
1 *1 R u1 {2,S}
2 *2 H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 444,
    label = "Xbirad_H",
    group = "OR{CH2_triplet_H, CH2_singlet_H, NH_triplet_H, NH_singlet_H}",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 476,
    label = "CH2_triplet_H",
    group = 
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 477,
    label = "CH2_singlet_H",
    group = 
"""
1 *1 C u0 p1 {2,S} {3,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 478,
    label = "NH_triplet_H",
    group = 
"""
1 *1 N u2 p1 {2,S}
2 *2 H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 479,
    label = "NH_singlet_H",
    group = 
"""
1 *1 N u0 p2 {2,S}
2 *2 H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 474,
    label = "Xtrirad_H",
    group = "OR{C_quartet_H, C_doublet_H}",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 480,
    label = "C_quartet_H",
    group = 
"""
1 *1 C u3 p0 {2,S}
2 *2 H u0 p0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 481,
    label = "C_doublet_H",
    group = 
"""
1 *1 C u1 p1 {2,S}
2 *2 H u0 p0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "X_H",
    group = 
"""
1 *1 R u0 {2,S}
2 *2 H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (-2.0652113706151138e-12, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 47 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=74 label="C/H3/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=60 label="Cs_H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=261 label="C_methyl">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=64 label="C_alkane">, <Entry index=261 label="C_methyl">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=87 label="C/H2/NonDeC_6ring">, <Entry index=261 label="C_methyl">]
[<Entry index=60 label="Cs_H">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C_alkane">, <Entry index=193 label="O_pri_rad">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=64 label="C_alkane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 4,
    label = "O_H",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    R u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (1282.2011790237714, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 9 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 5,
    label = "O_sec",
    group = 
"""
1 *1 O   u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    R!H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (1282.201179023768, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 9 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 6,
    label = "O/H/NonDeC",
    group = 
"""
1 *1 O  u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (1282.2011790237698, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 9 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 7,
    label = "O/H/Cs\H3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O  u0 {1,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6 *2 H  u0 {2,S}
""",
    correction = BarrierCorrection(
        correction = (1443.127592317363, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 3 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
""",
)

entry(
    index = 8,
    label = "O/H/Cs\Cs|H3",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cs u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7 *2 H  u0 {3,S}
""",
    correction = BarrierCorrection(
        correction = (-179.39404762033018, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 3 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=195 label="O_rad/NonDeO">]
""",
)

entry(
    index = 9,
    label = "O/H/Cs\Cs|Cs/H3",
    group = 
"""
1    Cs u0 {2,S} {5,S} {6,S} {7,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4 *1 O  u0 {3,S} {8,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8 *2 H  u0 {4,S}
""",
    correction = BarrierCorrection(
        correction = (2582.86999237429, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 3 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 60,
    label = "Cs_H",
    group = 
"""
1 *1 C u0 {2,S}
2 *2 H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (-312.53653738704156, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 38 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=74 label="C/H3/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=60 label="Cs_H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=261 label="C_methyl">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=64 label="C_alkane">, <Entry index=261 label="C_methyl">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=87 label="C/H2/NonDeC_6ring">, <Entry index=261 label="C_methyl">]
[<Entry index=60 label="Cs_H">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C_alkane">, <Entry index=193 label="O_pri_rad">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=64 label="C_alkane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 64,
    label = "C_alkane",
    group = 
"""
1 *1 C      u0 {2,S} {3,S} {4,S} {5,S}
2    [Cs,H] u0 {1,S}
3    H      u0 {1,S}
4    H      u0 {1,S}
5 *2 H      u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (-1259.6261263228612, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 13 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=61 label="C_methane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=64 label="C_alkane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=64 label="C_alkane">, <Entry index=193 label="O_pri_rad">]
[<Entry index=64 label="C_alkane">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 61,
    label = "C_methane",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (-900.5002051829048, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 2 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=61 label="C_methane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 62,
    label = "C/H3/Cs\H3",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
""",
    correction = BarrierCorrection(
        correction = (-1627.169607619633, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 3 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 63,
    label = "C/H3/Cs\Cs|H3",
    group = 
"""
1 *1 C  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3    Cs u0 {1,S} {2,S}
4 *2 H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
""",
    correction = BarrierCorrection(
        correction = (-2222.6611113912695, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 2 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 72,
    label = "C/Hx/O",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
4    O u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (612.306512394671, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 9 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=195 label="O_rad/NonDeO">]
""",
)

entry(
    index = 73,
    label = "C/H3/O",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    O u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (509.04779239697734, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 3 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=74 label="C/H3/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=195 label="O_rad/NonDeO">]
""",
)

entry(
    index = 74,
    label = "C/H3/O\H",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2    O u0 {1,S} {6,S}
3 *2 H u0 {1,S}
4    H u0 {1,S}
5    H u0 {1,S}
6    H u0 {2,S}
""",
    correction = BarrierCorrection(
        correction = (509.0477923969793, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 3 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=74 label="C/H3/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=195 label="O_rad/NonDeO">]
""",
)

entry(
    index = 75,
    label = "C/H2/Cs/O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
5    O  u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (663.9358723935186, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 6 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 76,
    label = "C/H2/Cs/O\H",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    O  u0 {1,S} {6,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
6    H  u0 {2,S}
""",
    correction = BarrierCorrection(
        correction = (663.9358723935192, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 6 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 77,
    label = "C/H2/O/Cs\Cs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    O  u0 {1,S}
6    Cs u0 {2,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "C/H2/O|H/Cs\Cs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S} {6,S}
5    O  u0 {1,S} {7,S}
6    Cs u0 {4,S}
7    H  u0 {5,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "C/Hx/Cs\O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S} {5,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    O  u0 {2,S}
""",
    correction = BarrierCorrection(
        correction = (1165.2841923589017, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 3 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=195 label="O_rad/NonDeO">]
""",
)

entry(
    index = 66,
    label = "C/H3/Cs\O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    O  u0 {2,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "C/H3/Cs\O|H",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {6,S}
2    Cs u0 {1,S} {5,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    O  u0 {2,S} {7,S}
6    H  u0 {1,S}
7    H  u0 {5,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "C/H2/Cs/Cs\O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
6    O  u0 {2,S}
""",
    correction = BarrierCorrection(
        correction = (1165.2841923589021, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 3 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=195 label="O_rad/NonDeO">]
""",
)

entry(
    index = 69,
    label = "C/H2/Cs/Cs\O|H",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cs u0 {1,S} {3,S}
3    O  u0 {2,S} {7,S}
4 *2 H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {1,S}
7    H  u0 {3,S}
""",
    correction = BarrierCorrection(
        correction = (1165.2841923589008, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 3 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=195 label="O_rad/NonDeO">]
""",
)

entry(
    index = 70,
    label = "C/H3/Cs\Cs|O",
    group = 
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {7,S}
4 *2 H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    O  u0 {3,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "C/H3/Cs\Cs|O/H",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S} {7,S}
7    O  u0 {6,S} {8,S}
8    H  u0 {7,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "C/H2/NonDeC_6ring",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {7,S} {8,S}
2    Cs u0 {1,S} {4,S}
3    Cs u0 {1,S} {5,S}
4    Cs u0 {2,S} {6,S}
5    Cs u0 {3,S} {6,S}
6    Cs u0 {4,S} {5,S}
7 *2 H  u0 {1,S}
8    H  u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (1633.972182140471, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 1 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=87 label="C/H2/NonDeC_6ring">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 40,
    label = "Cb_H",
    group = 
"""
1 *1 Cb u0 {2,S}
2 *2 H  u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "Cb/H/Cb",
    group = 
"""
1 *1 Cb u0 {2,S} {3,B}
2 *2 H  u0 {1,S}
3    Cb u0 {1,B}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "Cb/H/Cb/Cb",
    group = 
"""
1 *1 Cb u0 {2,S} {3,B} {4,B}
2 *2 H  u0 {1,S}
3    Cb u0 {1,B}
4    Cb u0 {1,B}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "Cb/H/Cb/Cb\O",
    group = 
"""
1 *1 Cb u0 {2,S} {3,B} {4,B}
2 *2 H  u0 {1,S}
3    Cb u0 {1,B}
4    Cb u0 {1,B} {5,S}
5    O  u0 {4,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "Cb/H/Cb/Cb\Nb",
    group = 
"""
1 *1 Cb  u0 {2,S} {3,B} {4,B}
2 *2 H   u0 {1,S}
3    Cb  u0 {1,B}
4    Cb  u0 {1,B} {5,B}
5    N3b u0 {4,B}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "Cb/H/Cb/Cb\Cb|Nb",
    group = 
"""
1 *1 Cb  u0 {2,S} {3,B} {4,B}
2 *2 H   u0 {1,S}
3    Cb  u0 {1,B}
4    Cb  u0 {1,B} {5,B}
5    Cb  u0 {4,B} {6,B}
6    N3b u0 {5,B}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "Cb/H/Cb/Cb\N_pyrrole",
    group = 
"""
1 *1 Cb  u0 {2,S} {3,B} {4,B}
2 *2 H   u0 {1,S}
3    Cb  u0 {1,B}
4    Cb  u0 {1,B} {5,S}
5    N3s u0 {4,S} {6,S} {7,S}
6    Cb  u0 {5,S}
7    H   u0 {5,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "Cd/H/Cb",
    group = 
"""
1 *1 C u0 {2,D} {3,S}
2    C u0 {1,D}
3 *2 H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "Cd/H/Cb/O",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    C u0 {1,D}
3 *2 H u0 {1,S}
4    O u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "Cd/H/Cb/Nb",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    C   u0 {1,D}
3 *2 H   u0 {1,S}
4    N3s u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "Cd/H/Cb/N_pyrrole",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,D}
2    C   u0 {1,D}
3 *2 H   u0 {1,S}
4    N3s u0 {1,D} {5,S} {6,S}
5    H   u0 {4,S}
6    C   u0 {4,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 409,
    label = "N3_H",
    group = 
"""
1 *1 [N3s,N3d] u0 {2,S}
2 *2 H         u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 410,
    label = "N3s_H",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 411,
    label = "N3s/H/Cb/Cb",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S}
4    C   u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 475,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet}",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 482,
    label = "C_quintet",
    group = 
"""
1 *3 C u4 p0
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 483,
    label = "C_triplet",
    group = 
"""
1 *3 C u2 p1
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 419,
    label = "Y_1centertrirad",
    group = "OR{N_atom_quartet, N_atom_doublet, CH_quartet, CH_doublet}",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 485,
    label = "N_atom_quartet",
    group = 
"""
1 *3 N u3 p1
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 486,
    label = "N_atom_doublet",
    group = 
"""
1 *3 N u1 p2
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 487,
    label = "CH_quartet",
    group = 
"""
1 *3 C u3 p0 {2,S}
2    H u0 p0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 487,
    label = "CH_doublet",
    group = 
"""
1 *3 C u1 p1 {2,S}
2    H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 [Cs,Cd,CO,CS,O,S,N] u2
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "Y_rad",
    group = 
"""
1 *3 R u1
""",
    correction = BarrierCorrection(
        correction = (-7.691625114603085e-13, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 47 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=74 label="C/H3/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=60 label="Cs_H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=261 label="C_methyl">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=64 label="C_alkane">, <Entry index=261 label="C_methyl">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=87 label="C/H2/NonDeC_6ring">, <Entry index=261 label="C_methyl">]
[<Entry index=60 label="Cs_H">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C_alkane">, <Entry index=193 label="O_pri_rad">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=64 label="C_alkane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 193,
    label = "Y_2centeradjbirad",
    group = 
"""
1 *3 [Ct,Os,Ss] u1 {2,[S,T]}
2    [Ct,Os,Ss] u1 {1,[S,T]}
""",
    correction = BarrierCorrection(
        correction = None,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    label = "O_rad",
    group = 
"""
1 *3 O u1 {2,S}
2    R u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (234.04087514270662, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 28 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=60 label="Cs_H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=64 label="C_alkane">, <Entry index=193 label="O_pri_rad">]
[<Entry index=64 label="C_alkane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=193 label="O_pri_rad">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 193,
    label = "O_pri_rad",
    group = 
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (-272.8879841534819, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 17 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=60 label="Cs_H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=64 label="C_alkane">, <Entry index=193 label="O_pri_rad">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=193 label="O_pri_rad">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=193 label="O_pri_rad">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=193 label="O_pri_rad">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=193 label="O_pri_rad">]
""",
)

entry(
    index = 194,
    label = "O_sec_rad",
    group = 
"""
1 *3 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (909.9460208709534, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 11 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=64 label="C_alkane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=195 label="O_rad/NonDeO">]
""",
)

entry(
    index = 195,
    label = "O_rad/NonDeO",
    group = 
"""
1 *3 O u1 {2,S}
2    O u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (909.9460208709528, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 11 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=64 label="C_alkane">, <Entry index=195 label="O_rad/NonDeO">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=195 label="O_rad/NonDeO">]
""",
)

entry(
    index = 260,
    label = "Cs_rad",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (-385.47908847034324, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 19 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=87 label="C/H2/NonDeC_6ring">, <Entry index=261 label="C_methyl">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=261 label="C_methyl">]
[<Entry index=60 label="Cs_H">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C_alkane">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 261,
    label = "C_methyl",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    correction = BarrierCorrection(
        correction = (-385.4790884703434, 'J/mol'),
    ),
    shortDesc = u"""Fitted to 19 solvation corrections.
""",
    longDesc = 
u"""
[<Entry index=76 label="C/H2/Cs/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=87 label="C/H2/NonDeC_6ring">, <Entry index=261 label="C_methyl">]
[<Entry index=8 label="O/H/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=74 label="C/H3/O\H">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O/H/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H2/Cs/Cs\O|H">, <Entry index=261 label="C_methyl">]
[<Entry index=60 label="Cs_H">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/Cs\Cs|Cs/H3">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs\Cs|H3">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C_alkane">, <Entry index=261 label="C_methyl">]
""",
)

tree(
"""
L1: X_H_or_Xrad_H_Xbirad_H_Xtrirad_H
    L2: Xrad_H
    L2: Xbirad_H
        L3: CH2_triplet_H
        L3: CH2_singlet_H
        L3: NH_triplet_H
        L3: NH_singlet_H
    L2: Xtrirad_H
        L3: C_quartet_H
        L3: C_doublet_H
    L2: X_H
        L3: O_H
            L4: O_sec
                L5: O/H/NonDeC
                    L6: O/H/Cs\H3
                    L6: O/H/Cs\Cs|H3
                    L6: O/H/Cs\Cs|Cs/H3
        L3: Cs_H
            L4: C_alkane
                L5: C_methane
                L5: C/H3/Cs\H3
                L5: C/H3/Cs\Cs|H3
            L4: C/Hx/O
                L5: C/H3/O
                    L6: C/H3/O\H
                L5: C/H2/Cs/O
                    L6: C/H2/Cs/O\H
                    L6: C/H2/O/Cs\Cs
                        L7: C/H2/O|H/Cs\Cs
            L4: C/Hx/Cs\O
                L5: C/H3/Cs\O
                    L6: C/H3/Cs\O|H
                L5: C/H2/Cs/Cs\O
                    L6: C/H2/Cs/Cs\O|H
            L4: C/H3/Cs\Cs|O
                L5: C/H3/Cs\Cs|O/H
            L4: C/H2/NonDeC_6ring
        L3: Cb_H
            L4: Cb/H/Cb
                L5: Cb/H/Cb/Cb
                    L6: Cb/H/Cb/Cb\O
                    L6: Cb/H/Cb/Cb\Nb
                    L6: Cb/H/Cb/Cb\Cb|Nb
                    L6: Cb/H/Cb/Cb\N_pyrrole
        L3: Cd/H/Cb
            L4: Cd/H/Cb/O
            L4: Cd/H/Cb/Nb
            L4: Cd/H/Cb/N_pyrrole
        L3: N3_H
            L4: N3s_H
                L5: N3s/H/Cb/Cb
L1: Y_rad_birad_trirad_quadrad
    L2: Y_1centerquadrad
        L3: C_quintet
        L3: C_triplet
    L2: Y_1centertrirad
        L3: N_atom_quartet
        L3: N_atom_doublet
        L3: CH_quartet
        L3: CH_doublet
    L2: Y_1centerbirad
    L2: Y_rad
        L3: Y_2centeradjbirad
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDeO
        L3: Cs_rad
            L4: C_methyl
"""
)

