import numpy
Q = 10**(-1*6)
rod_len = 1.0
N = 6.0

rY = numpy.linspace(rod_len*(N-1)/(2*N), -1*rod_len*(N-1)/(2*N), N)
print (rY)

trial = numpy.linspace(0.5, 0.6, 4)
print (trial)

ry2 = []
for i in range(0,int(N)):
    end = -1*rod_len*(N-1)/(2*N)
    start = rod_len*(N-1)/(2*N)

    increment = (end - start)/(N-1)
    p = start + (increment*i)
    ry2.append(p)

print (ry2)



