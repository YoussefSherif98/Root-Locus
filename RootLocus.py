import numpy as num
from matplotlib import pyplot as plotter

# Initializing the grid
plotter.axhline(y=0, linewidth=0.25, color='k')
plotter.axvline(x=0, linewidth=0.25, color='k')




# Drawing the poles
real = [0, -25, -50, -50]
imag = [0, 0, 10, -10]
plotter.scatter(real, imag, marker='D')




# Drawing the Root Locus
x = []
y = []

for i in range(0, 99999999, 1000):
    coefficients = [1, 125, 5100, 65000, i]
    roots = num.roots(coefficients)
    x.append(num.real(roots))
    y.append(num.imag(roots))

plotter.plot(x, y, linewidth=0.8, color='k')
coefficients = [1, 125, 5100, 65000, 0]




# Drawing centroid and asymptotes
centroid = 0
for r in real:
    centroid = centroid + (r/4)

plotter.scatter(centroid, 0, marker='.', color='b')

x = []
y1 = []
y2 = []
for i in range (-100,40,1):
    x.append(i)
    y1.append(i-centroid)
    y2.append(centroid-i)

plotter.plot(x, y1, linestyle='-.', color='b', linewidth='0.8')
plotter.plot(x, y2, linestyle='-.', color='b', linewidth='0.8')




# Finding and plotting the breakaway point
derivCoefficients = []
power = len(coefficients)
for coeff in coefficients:
    derivCoefficients.append(coeff * (power-1))
    power = power - 1

derivRoots = num.roots(derivCoefficients)
# Since we have 2 real poles, then we have only one breakaway point between -25 and 0
for d in derivRoots:
    if -25 < d < 0:
        plotter.scatter(d, 0, color='y', marker='<')
        break



# Finding and plotting the angle of departure for the complex poles
poles = num.roots(coefficients)
angle1 = 180 - \
         90 - \
         (num.arctan(num.imag(poles[0]) / num.real(poles[0]))) * 180 / num.pi - \
         (num.arctan(num.imag(poles[0]) / (num.real(poles[0]) + 25))) * 180 / num.pi
plotter.text(-50, 10, str (int(angle1)), fontsize=10)
angle2 = -angle1
plotter.text(-50, -10, str (int(angle2)), fontsize=10)



# Finding and plotting the intersection with the imaginary axis
# The computed value for k marginally stable was found to be 2381600
r = num.roots([(125 * 5100 - 65000) / 125, 0, 2381600])
im = num.imag(r)
plotter.scatter([0, 0], im, color='g', marker='x')



plotter.show()
