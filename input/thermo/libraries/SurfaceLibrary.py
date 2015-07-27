#!/usr/bin/env python
# encoding: utf-8

name = "SurfaceLibrary"
shortDesc = u"Library of adsorption thermo for silicon hydrides on silicon(100)"
longDesc = u"""
Values are from Gardeniers et al., J. Crystal Growth 104 (1990) 727-743. These are from table 3, which are values for singly bound silicon hydrides to Si(111). For reasons explained in the paper, these values are adequate to describe singly bound species on Si(100), but there are different values for some 2- bond and 4- bond bound species that are not included here yet.
"""

entry(
		index = 1,
		label = 'HX',
		molecule = 
		"""
		1 H u0 p0 c0 {2,S}
		2 X u0 p0 c0 {1,S}
		""",
		thermo = SurfaceThermoData(
		    H_ads = (-338, 'kJ/mol'),
                    S_ads = (-117, 'J/mol/K')	
                ),
		shortDesc = u"",
		longDesc = u"""
		""",
		)

entry(
		index = 2, 
		label = 'SiX',
		molecule = 
		"""
		1 Si u1 p1 c0 {2,S}
		2 X u0 p0 c0 {1,S}
		""",
		thermo = SurfaceThermoData(
		    H_ads = (-221, 'kJ/mol'),
                    S_ads = (-118, 'J/mol/K')	
                ),
		shortDesc = u"",
		longDesc = u"""
		""",
		)

entry(
		index = 3,
		label = 'SiHX',
		molecule = 
		"""
		1 Si u0 p1 c0 {2,S} {3,S}
		2 H u0 p0 c0 {1,S}
                3 X u0 p0 c0 {1,S}
		""",
		thermo = SurfaceThermoData(
		    H_ads = (-241, 'kJ/mol'),
                    S_ads = (-127, 'J/mol/K')	
                ),
		shortDesc = u"",
		longDesc = u"""
		""",
		)

entry(
		index = 4,
		label = 'SiH2X',
		molecule = 
		"""
		1 Si u1 p0 c0 {2,S} {3,S} {4,S}
		2 H u0 p0 c0 {1,S}
                3 H u0 p0 c0 {1,S}
                4 X u0 p0 c0 {1,S}
		""",
		thermo = SurfaceThermoData(
		    H_ads = (-189, 'kJ/mol'),
                    S_ads = (-129, 'J/mol/K')	
                ),
		shortDesc = u"",
		longDesc = u"""
		""",
		)

entry(
		index = 5,
		label = 'SiH3X',
		molecule = 
		"""
		1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
		2 H u0 p0 c0 {1,S}
		3 H u0 p0 c0 {1,S}
		4 H u0 p0 c0 {1,S}
                5 X u0 p0 c0 {1,S}
		""",
		thermo = SurfaceThermoData(
		    H_ads = (-281, 'kJ/mol'),
                    S_ads = (-155, 'J/mol/K')	
                ),
		shortDesc = u"",
		longDesc = u"""
		""",
		)

entry(
		index = 6,
		label = 'Si2H5X',
		molecule = 
		"""
		1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
		2 H u0 p0 c0 {1,S}
		3 H u0 p0 c0 {1,S}
		4 H u0 p0 c0 {1,S}
                5 Si u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
                6 H u0 p0 c0 {5,S}
                7 H u0 p0 c0 {5,S}
                8 X u0 p0 c0 {5,S}
		""",
		thermo = SurfaceThermoData(
		    H_ads = (-266, 'kJ/mol'),
                    S_ads = (-191, 'J/mol/K')	
                ),
		shortDesc = u"",
		longDesc = u"""
		""",
		)

entry(
		index = 7,
		label = 'H3SiSiHX',
		molecule = 
		"""
		1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
		2 H u0 p0 c0 {1,S}
		3 H u0 p0 c0 {1,S}
		4 H u0 p0 c0 {1,S}
                5 Si u1 p0 c0 {1,S} {6,S} {7,S}
                6 H u0 p0 c0 {5,S}
                7 X u0 p0 c0 {5,S}
		""",
		thermo = SurfaceThermoData(
		    H_ads = (-205, 'kJ/mol'),
                    S_ads = (-176, 'J/mol/K')	
                ),
		shortDesc = u"",
		longDesc = u"""
		""",
		)

entry(
		index = 8,
		label = 'H2SiSiH2',
		molecule = 
		"""
		1 Si u1 p0 c0 {2,S} {3,S} {4,S}
		2 H u0 p0 c0 {1,S}
		3 H u0 p0 c0 {1,S}
                4 Si u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
                5 H u0 p0 c0 {4,S}
                6 H u0 p0 c0 {4,S}
                7 X u0 p0 c0 {4,S}
		""",
		thermo = SurfaceThermoData(
		    H_ads = (-120, 'kJ/mol'),
                    S_ads = (-179, 'J/mol/K')	
                ),
		shortDesc = u"",
		longDesc = u"""
		""",
		)
