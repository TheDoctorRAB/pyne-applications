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
from pyne import nucname
#
########################################################################
#
#
#
#######
#
# compute atomic mass
#
print('This script uses pyne to give the zaid of an isotope for mcnp', '\n')
print ('Type in the isotope; i.e., h2, cs137, co60')
isotope=input()
print ('The zaid of',isotope,'is',nucname.zzzaaa(isotope))
#
########################################################################
#
# EOF
#
########################################################################
