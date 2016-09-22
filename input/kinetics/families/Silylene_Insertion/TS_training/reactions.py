entry(
    index = 1,
    label = "H2 + H2Si <=> H4Si",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.14234, 'd13': 1.63115, 'd23': 1.52108},
        method = 'm062x/mg3s',
    ),
    rank = 3,
    shortDesc = u"""Manual M06-2X/MG3S calculation.""",
)

entry(
    index = 2,
    label = "H2 + H4Si2 <=> H6Si2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.11196, 'd13': 1.62865, 'd23': 1.54411},
        method = 'm062x/mg3s',
    ),
    rank = 3,
    shortDesc = u"""Manual M06-2X/MG3S calculation.""",
)

entry(
    index = 3,
    label = "H2 + H6Si3 <=> H8Si3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.03580, 'd13': 1.63907, 'd23': 1.56433},
        method = 'm062x/mg3s',
    ),
    rank = 3,
    shortDesc = u"""Manual M06-2X/MG3S calculation.""",
)

#entry(
#    index = 4,
#    label = "CHN + H2Si <=> CH3NSi",
#    degeneracy = 1,
#    distances = DistanceData(
#        distances = {'d12': 1.34749, 'd13': 1.87265, 'd23': 1.69676},
#        method = 'm062x/mg3s',
#    ),
#    rank = 3,
#    shortDesc = u"""Manual M06-2X/MG3S calculation.""",
#)
#
#entry(
#    index = 5,
#    label = "ClHSi + H2 <=> ClH3Si",
#    degeneracy = 1,
#    distances = DistanceData(
#        distances = {'d12': 1.19488, 'd13': 1.64983, 'd23': 1.50694},
#        method = 'm062x/mg3s',
#    ),
#    rank = 3,
#    shortDesc = u"""Manual M06-2X/MG3S calculation.""",
#)
entry(
    index = 4,
    label = "H2Si2 + H2 <=> H4Si2-1",
    degeneracy = 2,
    distances = DistanceData(
        distances = {'d12': 0.97188, 'd13': 1.68122, 'd23': 1.65256},
        method = 'm062x/gen',
    ),
    shortDesc = u"""M06-2X/MG3S calculation via group additive TS generator.""",
)

entry(
    index = 5,
    label = "HSi + H2 <=> H3Si",
    degeneracy = 2,
    distances = DistanceData(
        distances = {'d12': 1.28463, 'd13': 1.54121, 'd23': 1.61921},
        method = 'm062x/gen',
    ),
    shortDesc = u"""M06-2X/MG3S calculation via group additive TS generator.""",
)

entry(
    index = 6,
    label = "H6Si3-5 + H2 <=> H8Si3-1",
    degeneracy = 2,
    distances = DistanceData(
        distances = {'d12': 1.10646, 'd13': 1.63128, 'd23': 1.54355},
        method = 'm062x/gen',
    ),
    shortDesc = u"""M06-2X/MG3S calculation via group additive TS generator.""",
)

entry(
    index = 7,
    label = "H2Si + H6Si2-1 <=> H8Si3-1",
    degeneracy = 6,
    distances = DistanceData(
        distances = {'d12': 2.23149, 'd13': 2.4995, 'd23': 1.49275},
        method = 'm062x/gen',
    ),
    shortDesc = u"""M06-2X/MG3S calculation via group additive TS generator.""",
)

