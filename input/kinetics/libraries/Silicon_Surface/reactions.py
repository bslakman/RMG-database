name = "Silicon_Surface"
shortDesc = u"Silicon deposition mechanism from silane"
longDesc = u"""
From  Table 1, reactions A-1--A-7, in Valente et al., J. Crystal Growth, 230 (2001) 246-257.
"""

entry(
		index = 1,
		label = "SiH4 + X + X => SiH3X + HX",
		degeneracy = 1,
                reversible = False,
                surface = True,
		kinetics = SurfaceArrhenius(A=(1.148E19, 'cm^5/(mol^2*s)'), n=0.5, Ea=(3000, 'cal/mol')),
		longDesc = u"""
		Reaction A-1 
		"""
		)

