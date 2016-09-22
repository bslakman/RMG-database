#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Insertion/groups"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "Si2S",
    group = 
"""
1 *3 Si ux p1 c0
""",
    distances = DistanceData(
        distances = {'d12': 1.32477, 'd13': 1.80373, 'd23': 1.53228},
        uncertainties = {'d12': 0.345576, 'd13': 0.236277, 'd23': 0.025871},
    ),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
['SiH2', 'H_H']
['SiH2', 'SiH3_Si']
['Si-Si-Si', 'H_H']
['Si-Si-H', 'H_H']
['Si2S', 'H_H']
""",
)

entry(
    index = 2,
    label = "Y_H",
    group = "OR{H_H, Si_H}",
    distances = DistanceData(distances={}),
)

entry(
    index = 5,
    label = "SiH2",
    group = 
"""
1 *3 Si u0 p1 c0 {2,S} {3,S}
2    H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""silylene""",
)

entry(
    index = 5,
    label = "Si-Si-Si",
    group = 
"""
1 *3 Si u0 p1 c0 {2,S} {3,S}
2    Si ux {1,S}
3    Si ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 5,
    label = "Si-Si-H",
    group = 
"""
1 *3 Si u0 p1 c0 {2,S} {3,S}
2    H  u0 p0 c0 {1,S}
3    Si ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 3,
    label = "H_H",
    group = 
"""
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 4,
    label = "Si_H",
    group = 
"""
1 *1 Si ux p0 c0 {2,S}
2 *2 H  u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.828111, 'd13': 0.642537, 'd23': -0.031942},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
['SiH2', 'SiH3_Si']
""",
)

entry(
    index = 4,
    label = "SiH3_R",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4    H  u0 p0 c0 {1,S}
5    R  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.828111, 'd13': 0.642537, 'd23': -0.031942},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
['SiH2', 'SiH3_Si']
""",
)

entry(
    index = 8,
    label = "SiH4",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4    H  u0 p0 c0 {1,S}
5    H  u0 p0 c0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Silane""",
)

entry(
    index = 4,
    label = "SiH3_Si",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4    H  u0 p0 c0 {1,S}
5    Si ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 4,
    label = "SiH2_R2",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4    R  ux {1,S}
5    R  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 4,
    label = "SiH_R3",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    R  ux {1,S}
4    R  ux {1,S}
5    R  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

tree(
"""
L1: Si2S
    L2: SiH2
    L2: Si-Si-Si
    L2: Si-Si-H
L1: Y_H
    L2: H_H
    L2: Si_H
        L3: SiH3_R
            L4: SiH4
            L4: SiH3_Si
        L3: SiH2_R2
        L3: SiH_R3
"""
)

