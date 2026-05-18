import numpy

dm = 0.1
dM = 0.6
mass = 5.3
x1 = dm / dM
x2 = -(mass/ dM**2) * dm

dRo = numpy.sqrt((x1**2) + (x2**2))
print(dRo)