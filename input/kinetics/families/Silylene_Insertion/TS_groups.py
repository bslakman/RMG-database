#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Insertion/TS_groups"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "Si2S",
    group = 
"""
1 *3 Si u0 p1 c0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 2,
    label = "Y_H",
    group = "OR{H_H, Si_H, Cl_H}",
    distances = DistanceData(distances={}),
)

entry(
    index = 3,
    label = "SiH2",
    group = 
"""
1 *3 Si u0 p1 c0 {2,S} {3,S}
2    H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 4,
    label = "SiHR",
    group = 
"""
1 *3 Si  u0 p1 c0 {2,S} {3,S}
2    H   u0 p0 c0 {1,S}
3    R!H ux px c0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 5,
    label = "SiRR",
    group = 
"""
1 *3 Si  u0 p1 c0 {2,S} {3,S}
2    R!H ux px c0 {1,S}
3    R!H ux px c0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 6,
    label = "H_H",
    group = 
"""
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 7,
    label = "Si_H",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S}
2 *2 H  u0 p0 c0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 8,
    label = "Cl_H",
    group = 
"""
1 *1 Cl u0 p3 c0 {2,S}
2 *2 H  u0 p0 c0 {1,S}
""",
    distances = DistanceData(distances={}),
)

tree(
"""
L1: Si2S
    L2: SiH2
    L2: SiHR
    L2: SiRR
L1: Y_H
    L2: H_H
    L2: Si_H
    L2: Cl_H
"""
)

