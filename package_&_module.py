
#================================
#          Using Package
#================================

from MyPakage import msmath
from MyPakage import msstring

print(msmath.sum(4, 2))
print(msmath.subtract(4, 2))
print(msmath.multiplication(4, 2))
print(msstring.full_name('Hello', 'World'))
print(msstring.print_characters('hello_world'))

#------------------ Othre way ---------------
from MyPakage.msmath import *
print(sum(4, 2))
print(subtract(4, 2))
print(multiplication(4, 2))

#================ Python Standard library ===============



