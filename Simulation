import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math

# Number of sample heights
N = 100

# tank characteristics
R = 0.6096
L = 3.302
LargeTankVolume = math.pi * R * R * L

# Statistics
Mean = 0
StandardDeviation = 0.05
RandomArray = np.random.normal(Mean, StandardDeviation, N)

# the cylinder tank
# a vector that has all the heights of the cylindrical tank
CylinderHeights = np.linspace(0.0, 1.524, N)
CylinderVolume = CylinderHeights*math.pi*0.762*0.762

# the box tank
BoxHeights = np.linspace(0.0, 1.6764, N)
BoxVolume = BoxHeights*1.5748*0.7366

# the horizontal cylinder
HorizontalCylinderHeights = np.linspace(0.0, 1.2192, N)
HorizontalCylinderHeightsyaxis = np.linspace(0.0, 1.2192, N)
HorizontalCylinderVolume = HorizontalCylinderHeights

# enumerate makes 2 variables, i is the index, and j is the value inside the vector HorizontalCylinderHeights
for i, j in enumerate(HorizontalCylinderHeights, start=0):

    # if the tank is less than half empty one equation is used
    if j < R:
        AreaOfSector = math.pi*R*R*(math.acos((R-j)/R))/(2 * math.pi)
        AreaOfTriangle = 0.5 * math.sqrt(R*R-(R-j)*(R-j))*(R-j)
        HorizontalCylinderVolume[i] = (AreaOfSector - AreaOfTriangle) * L * 2
        print(i, j, AreaOfSector, AreaOfTriangle)

    # if the tank is more than half empty the other equation is used
    else:
        AreaOfSector = math.pi * R * R * (math.acos((j - R) / R)) / (2 * math.pi)
        AreaOfTriangle = 0.5 * math.sqrt(R * R - (j - R) * (j - R)) * (j - R)
        HorizontalCylinderVolume[i] = LargeTankVolume - (AreaOfSector - AreaOfTriangle) * L * 2
        print(i, j, AreaOfSector, AreaOfTriangle)


# plots
plt.subplot(131)
plt.plot(CylinderHeights, CylinderVolume)
matplotlib.pyplot.title("Cylinder volume")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

plt.subplot(132)
plt.plot(BoxHeights, BoxVolume)
matplotlib.pyplot.title("Box volume")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

plt.subplot(133)
plt.plot(HorizontalCylinderHeightsyaxis, HorizontalCylinderVolume, "o")
matplotlib.pyplot.title("Horizontal Cylinder volume")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

plt.show()

