########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.30.June.2017
########################################################################
#
# Print molecular weight
#
########################################################################
#
#
#
#######
#
# imports
#
from pyne.data import atomic_mass
#
########################################################################
#
#
#
#######
#
# compute atomic mass
#
print('This script uses pyne to give the atomic mass of an isotope', '\n')
print ('Type in the isotope; i.e., h2, cs137, co60')
isotope=input()
print ('The atomic mass of',isotope,'is',atomic_mass(isotope))
#
########################################################################
#
# EOF
#
########################################################################
