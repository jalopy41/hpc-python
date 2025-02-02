import numpy as np
import matplotlib.pyplot as plt

# Construct xi
dx = 0.10
xi = np.arange(0, np.pi/2, dx)
print(xi[1:-1])
# Function values
fi = np.sin(xi)
# Derivative
dfi = (fi[2:] - fi[:-2]) / (2.0*dx)

# Compare to cos. Note that derivative was not defined in end points
f_ref = np.cos(xi[1:-1])
print("Mean squared difference:")
print(np.sqrt(np.sum((dfi - f_ref)**2)))
plt.plot(xi[1:-1], dfi, label="sin'")
plt.plot(xi[1:-1], f_ref, label="cos")
plt.legend()
plt.show()

