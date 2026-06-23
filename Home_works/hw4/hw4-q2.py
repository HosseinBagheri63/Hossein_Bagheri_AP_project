import numpy
hi = numpy.array([[96, 15, 80, 4], [49, 43, 96, 85], [81, 92, 66, 94]])
bye = numpy.transpose(hi.reshape(-1,2))
print(bye)