import math

CD = 0.2
rho = 1.225  # kg/m^3
V = 10  # m/s
A = 1  # m^2

## fffff
print("DragForce: " + str(0.5*CD*rho*math.pow(V, 2)*A))
