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

# the cylinder tank
# a vector that has all the heights of the cylindrical tank
CylinderHeights = np.linspace(0.0, 1.524, N)
CylinderVolume = CylinderHeights * math.pi * 0.762 * 0.762

# the box tank
BoxHeights = np.linspace(0.0, 1.6764, N)
BoxVolume = BoxHeights * 1.5748 * 0.7366

# the horizontal cylinder
HorizontalCylinderHeights = np.linspace(0.0, 1.2192, N)
HorizontalCylinderVolume = HorizontalCylinderHeights.copy()

# enumerate makes 2 variables, i is the index, and j is the value inside the vector HorizontalCylinderHeights
for i, j in enumerate(HorizontalCylinderHeights, start=0):

    # if the tank is less than half empty one equation is used
    if j < R:
        AreaOfSector = math.pi * R * R * (math.acos((R - j) / R)) / (2 * math.pi)
        AreaOfTriangle = 0.5 * math.sqrt(R * R - (R - j) * (R - j)) * (R - j)
        HorizontalCylinderVolume[i] = (AreaOfSector - AreaOfTriangle) * L * 2
        print(i, j, AreaOfSector, AreaOfTriangle)

    # if the tank is more than half empty the other equation is used
    else:
        AreaOfSector = math.pi * R * R * (math.acos((j - R) / R)) / (2 * math.pi)
        AreaOfTriangle = 0.5 * math.sqrt(R * R - (j - R) * (j - R)) * (j - R)
        HorizontalCylinderVolume[i] = LargeTankVolume - (AreaOfSector - AreaOfTriangle) * L * 2
        print(i, j, AreaOfSector, AreaOfTriangle)

# lets make some vectors to store this shit, need to use copy to make them different
CylinderVolumeSingleValues = CylinderVolume.copy()
BoxVolumeSingleValues = BoxVolume.copy()
HorizontalCylinderVolumeSV = HorizontalCylinderVolume.copy()

# a couple of functions for getting the random variation accurate for the given height
# gets the average mean for that height, it's not the same, there is an offset
def get_mean(height):
    return height * 1.03 - 0.0162


# gets the standard deviation for the height, it's not the same, there is an offset
def get_std_dvt(height):
    return height * 0.0000636 + 0.00643


# finding the heights after a random variables is added
# single values added to vertical cylinder
for k1, l1 in enumerate(CylinderHeights, start=0):
    CylinderVolumeSingleValues[k1] = CylinderVolume[k1] + np.random.normal(get_mean(l1), get_std_dvt(l1))

# single values for box tank
for k2, l2 in enumerate(BoxHeights, start=0):
    BoxVolumeSingleValues[k2] = BoxVolume[k2] + np.random.normal(get_mean(l2), get_std_dvt(l2))

# single values for the horizontal tank
for k3, l3 in enumerate(HorizontalCylinderHeights, start=0):
    HorizontalCylinderVolumeSV[k3] = HorizontalCylinderVolume[k3] + np.random.normal(get_mean(l3), get_std_dvt(l3))

# plots
# Vertical Cylinder plot
plt.figure(1)
plt.subplot(131)
plt.plot(CylinderHeights, CylinderVolume)
matplotlib.pyplot.title("Cylinder volume")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Box plot
plt.subplot(132)
plt.plot(BoxHeights, BoxVolume)
matplotlib.pyplot.title("Box volume")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Horizontal Cylinder plot
plt.subplot(133)
plt.plot(HorizontalCylinderHeights, HorizontalCylinderVolume)
matplotlib.pyplot.title("Horizontal Cylinder volume")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")


# plots with random error added
# Vertical Cylinder with error plot
plt.figure(2)
plt.subplot(131)
plt.plot(CylinderHeights, CylinderVolumeSingleValues)
matplotlib.pyplot.title("Cylinder volume with random variation")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

plt.subplot(132)
plt.plot(BoxHeights, BoxVolumeSingleValues)
matplotlib.pyplot.title("Box volume with random variation")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Horizontal Cylinder plot
plt.subplot(133)
plt.plot(HorizontalCylinderHeights, HorizontalCylinderVolumeSV)
matplotlib.pyplot.title("Horizontal Cylinder volume with random variation")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# displays the plots

plt.show()
