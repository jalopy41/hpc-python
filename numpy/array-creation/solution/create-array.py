import numpy as np

a = [4, 6, 21.12, 11, 0.23]
b = np.array(a)
print(b)

c = np.arange(-2.0, 2.01, 0.2)
print(c)
print(c[1:11:2])

d = np.linspace(0.5, 1.5, 11)
print(d)

dna = 'ACGAATGCAACCGATC'
e = np.array(dna, dtype='c')
print(e)
#type 'b' is binary, reverse compatability with python2?
