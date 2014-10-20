#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Elimination/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Y_Si2S_R_H2"], products=["Y_H", "Si2S_R_H"], ownReverse=False)

#reverse = "Silylene_Insertion"

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*3'],
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*2'],
    ['GAIN_PAIR', '*3', '1'],])

entry(
    index = 1,
    label = "Y_Si2S_R_H2",
    group = 
"""
1 *3 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *1 R  u0 p0 c0 {1,S}
5    R  u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "H_Si2S_R_H2",
    group = 
"""
1 *3 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *1 H  u0 p0 c0 {1,S}
5    R  u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Si_Si2S_R_H2",
    group = 
"""
1 *3 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *1 Si u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5    R  u0 p0 c0 {1,S}
6    R  u0 p0 c0 {4,S}
7    R  u0 p0 c0 {4,S}
8    R  u0 p0 c0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "SiH4",
    group = 
"""
1 *3 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *1 H  u0 p0 c0 {1,S}
5    H  u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "Si2H6_H",
    group = 
"""
1 *3 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *1 H  u0 p0 c0 {1,S}
5    Si  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6    H  u0 p0 c0 {5,S}
7    H  u0 p0 c0 {5,S}
8    H  u0 p0 c0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "Si3H8_H",
    group = 
"""
1 *3 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *1 H  u0 p0 c0 {1,S}
5    Si  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6    H  u0 p0 c0 {5,S}
7    H  u0 p0 c0 {5,S}
8    Si  u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9    H  u0 p0 c0 {8,S}
10   H  u0 p0 c0 {8,S}
11   H  u0 p0 c0 {8,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "Si4H10_H",
    group = 
"""
1 *3 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *1 H  u0 p0 c0 {1,S}
5    Si  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6    H  u0 p0 c0 {5,S}
7    H  u0 p0 c0 {5,S}
8    Si  u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9    H  u0 p0 c0 {8,S}
10   H  u0 p0 c0 {8,S}
11   Si  u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12   H  u0 p0 c0 {11,S}
13   H  u0 p0 c0 {11,S}
14   H  u0 p0 c0 {11,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "Si2H6_Si",
    group = 
"""
1 *3 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *1 Si u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5    H  u0 p0 c0 {1,S}
6    H  u0 p0 c0 {4,S}
7    H  u0 p0 c0 {4,S}
8    H  u0 p0 c0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "Si3H8_Si",
    group = 
"""
1 *3 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *1 Si u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5    H  u0 p0 c0 {1,S}
6    H  u0 p0 c0 {4,S}
7    H  u0 p0 c0 {4,S}
8    Si  u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
9    H  u0 p0 c0 {8,S}
10   H  u0 p0 c0 {8,S}
11   H  u0 p0 c0 {8,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Si4H10_Si",
    group = 
"""
1 *3 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *1 Si u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5    H  u0 p0 c0 {1,S}
6    H  u0 p0 c0 {4,S}
7    H  u0 p0 c0 {4,S}
8    Si  u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
9    H  u0 p0 c0 {8,S}
10   H  u0 p0 c0 {8,S}
11   Si  u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12   H  u0 p0 c0 {11,S}
13   H  u0 p0 c0 {11,S}
14   H  u0 p0 c0 {11,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: Y_Si2S_R_H2
	L2: H_Si2S_R_H2
		L3: SiH4
		L3: Si2H6_H
		L3: Si3H8_H
		L3: Si4H10_H
	L2: Si_Si2S_R_H2
		L3: Si2H6_Si
		L3: Si3H8_Si
		L3: Si4H10_Si
"""
)

