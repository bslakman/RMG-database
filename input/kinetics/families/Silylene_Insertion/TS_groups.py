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
        distances = {'d12': 1.33429, 'd13': 1.84642, 'd23': 1.55661},
        uncertainties = {'d12': 0.298522, 'd13': 0.224441, 'd23': 0.043822},
    ),
    shortDesc = u"""Fitted to 11 distances.
""",
    longDesc = 
u"""
['Si-Si-Si', 'H_H']
['Si2S', 'H_H']
['SiH2', 'SiH3_Si']
['Si-Si-H', 'H_H']
['SiH2', 'H_H']
['Si2S', 'SiH4']
['SiH2', 'Si_H']
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
        distances = {'d12': 0.700808, 'd13': 0.581526, 'd23': -0.046723},
        uncertainties = {'d12': 1.37619, 'd13': 0.936298, 'd23': 0.078425},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
['Si2S', 'SiH4']
['SiH2', 'Si_H']
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
        distances = {'d12': 0.700808, 'd13': 0.581526, 'd23': -0.046723},
        uncertainties = {'d12': 1.37619, 'd13': 0.936298, 'd23': 0.078425},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
['Si2S', 'SiH4']
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

