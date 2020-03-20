import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math

# Number of sample heights, needs to be a multiple of 10
N: int = 1000

# tank characteristics
R = 0.6096
L = 3.302
LargeTankVolume = math.pi * R * R * L

# the cylinder tank
# a vector that has all the heights of the cylindrical tank
CylinderHeights = np.linspace(0.0, 1.524, N)
CylinderHeightsAvg5 = np.linspace(0.0, 1.524, int(N / 5))
CylinderHeightsAvg10 = np.linspace(0.0, 1.524, int(N / 10))
CylinderVolume = CylinderHeights * math.pi * 0.762 * 0.762

# the box tank
BoxHeights = np.linspace(0.0, 1.6764, N)
BoxHeightsAvg5 = np.linspace(0.0, 1.6764, int(N / 5))
BoxHeightsAvg10 = np.linspace(0.0, 1.6764, int(N / 10))
BoxVolume = BoxHeights * 1.5748 * 0.7366

# the horizontal cylinder
HorizontalCylinderHeights = np.linspace(0.0, 1.2192, N)
HorizontalCylinderHeightsAvg5 = np.linspace(0.0, 1.2192, int(N / 5))
HorizontalCylinderHeightsAvg10 = np.linspace(0.0, 1.2192, int(N / 10))
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
CylinderVolumeWithError = CylinderVolume.copy()
BoxVolumeWithError = BoxVolume.copy()
HorizontalCylinderWithError = HorizontalCylinderVolume.copy()


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
    CylinderVolumeWithError[k1] = CylinderVolume[k1] + np.random.normal(get_mean(l1), get_std_dvt(l1))
# single values for box tank
for k2, l2 in enumerate(BoxHeights, start=0):
    BoxVolumeWithError[k2] = BoxVolume[k2] + np.random.normal(get_mean(l2), get_std_dvt(l2))
# single values for the horizontal tank
for k3, l3 in enumerate(HorizontalCylinderHeights, start=0):
    HorizontalCylinderWithError[k3] = HorizontalCylinderVolume[k3] + np.random.normal(get_mean(l3), get_std_dvt(l3))

# Average of 5
# create the vectors to hold the averages
Average5Cylinder = np.zeros(int(N / 5))
Average5Box = np.zeros(int(N / 5))
Average5Horizontal = np.zeros(int(N / 5))

# get the average for the cylinder tank
for av_i, av_j in enumerate(Average5Cylinder, start=0):
    Average5Cylinder[av_i] = (CylinderVolumeWithError[av_i] + CylinderVolumeWithError[av_i + 1]
                              + CylinderVolumeWithError[av_i + 2] + CylinderVolumeWithError[av_i + 3]
                              + CylinderVolumeWithError[av_i + 4]) / 5
# get the average for the box tank
for av_i, av_j in enumerate(Average5Box, start=0):
    Average5Box[av_i] = (BoxVolumeWithError[av_i] + BoxVolumeWithError[av_i + 1]
                         + BoxVolumeWithError[av_i + 2] + BoxVolumeWithError[av_i + 3]
                         + BoxVolumeWithError[av_i + 4]) / 5
# get the average for horizontal tank
for av_i, av_j in enumerate(Average5Horizontal, start=0):
    Average5Horizontal[av_i] = (HorizontalCylinderWithError[av_i] + HorizontalCylinderWithError[av_i + 1]
                                + HorizontalCylinderWithError[av_i + 2] + HorizontalCylinderWithError[av_i + 3]
                                + HorizontalCylinderWithError[av_i + 4]) / 5

# Average of 10
# create the vectors to hold the averages
Average10Cylinder = np.zeros(int(N / 10))
Average10Box = np.zeros(int(N / 10))
Average10Horizontal = np.zeros(int(N / 10))

# get the average for the cylinder tank
for av_i, av_j in enumerate(Average10Cylinder, start=0):
    Average10Cylinder[av_i] = (CylinderVolumeWithError[av_i] + CylinderVolumeWithError[av_i + 1]
                               + CylinderVolumeWithError[av_i + 2] + CylinderVolumeWithError[av_i + 3]
                               + CylinderVolumeWithError[av_i + 4] + CylinderVolumeWithError[av_i + 5]
                               + CylinderVolumeWithError[av_i + 6] + CylinderVolumeWithError[av_i + 7]
                               + CylinderVolumeWithError[av_i + 8] + CylinderVolumeWithError[av_i + 9]) / 10
# get the average for the box tank
for av_i, av_j in enumerate(Average10Box, start=0):
    Average10Box[av_i] = (BoxVolumeWithError[av_i] + BoxVolumeWithError[av_i + 1]
                          + BoxVolumeWithError[av_i + 2] + BoxVolumeWithError[av_i + 3]
                          + BoxVolumeWithError[av_i + 4] + BoxVolumeWithError[av_i + 5]
                          + BoxVolumeWithError[av_i + 6] + BoxVolumeWithError[av_i + 7]
                          + BoxVolumeWithError[av_i + 8] + BoxVolumeWithError[av_i + 9]) / 10
# get the average for horizontal tank
for av_i, av_j in enumerate(Average10Horizontal, start=0):
    Average10Horizontal[av_i] = (HorizontalCylinderWithError[av_i] + HorizontalCylinderWithError[av_i + 1]
                                 + HorizontalCylinderWithError[av_i + 2] + HorizontalCylinderWithError[av_i + 3]
                                 + HorizontalCylinderWithError[av_i + 4] + HorizontalCylinderWithError[av_i + 5]
                                 + HorizontalCylinderWithError[av_i + 6] + HorizontalCylinderWithError[av_i + 7]
                                 + HorizontalCylinderWithError[av_i + 8] + HorizontalCylinderWithError[av_i + 9]) / 10

# Min and max removed, plus the average of 3 and median of 5
# create the vectors to hold results
threeOf5Cylinder = np.zeros(int(N / 5))
threeOf5Box = np.zeros(int(N / 5))
threeOf5Horizontal = np.zeros(int(N / 5))
medianOf5Cylinder = np.zeros(int(N / 5))
medianOf5Box = np.zeros(int(N / 5))
medianOf5Horizontal = np.zeros(int(N / 5))

# Cylinder tank
bubbleSort = np.zeros(5)
for av_i, av_j in enumerate(threeOf5Cylinder, start=0):
    # gets variables ready for bubble sorting
    bubbleSort[0] = CylinderVolumeWithError[av_i]
    bubbleSort[1] = CylinderVolumeWithError[av_i + 1]
    bubbleSort[2] = CylinderVolumeWithError[av_i + 2]
    bubbleSort[3] = CylinderVolumeWithError[av_i + 3]
    bubbleSort[4] = CylinderVolumeWithError[av_i + 4]
    # bubble sorts to get the values in order
    for bi in bubbleSort:
        for bj in range(0, int(4-bi)):
            if bubbleSort[bj] > bubbleSort[bj + 1]:
                bx = bubbleSort[bj]
                bubbleSort[bj] = bubbleSort[bj + 1]
                bubbleSort[bj + 1] = bx
    # puts the average of the middle three, aka it removes the min and max and finds the average of the rest
    threeOf5Cylinder[av_i] = (bubbleSort[2] + bubbleSort[3] + bubbleSort[4]) / 3
    medianOf5Cylinder[av_i] = bubbleSort[3]
for av_i, av_j in enumerate(threeOf5Cylinder, start=0):
    # gets variables ready for bubble sorting
    bubbleSort[0] = CylinderVolumeWithError[av_i]
    bubbleSort[1] = CylinderVolumeWithError[av_i + 1]
    bubbleSort[2] = CylinderVolumeWithError[av_i + 2]
    bubbleSort[3] = CylinderVolumeWithError[av_i + 3]
    bubbleSort[4] = CylinderVolumeWithError[av_i + 4]
    # bubble sorts to get the values in order
    for bi in bubbleSort:
        for bj in range(0, int(4-bi)):
            if bubbleSort[bj] > bubbleSort[bj + 1]:
                bx = bubbleSort[bj]
                bubbleSort[bj] = bubbleSort[bj + 1]
                bubbleSort[bj + 1] = bx
    # puts the average of the middle three, aka it removes the min and max and finds the average of the rest
    threeOf5Cylinder[av_i] = (bubbleSort[2] + bubbleSort[3] + bubbleSort[4]) / 3
    medianOf5Cylinder[av_i] = bubbleSort[3]

# Box tank
for av_i, av_j in enumerate(threeOf5Box, start=0):
    # gets variables ready for bubble sorting
    bubbleSort[0] = BoxVolumeWithError[av_i]
    bubbleSort[1] = BoxVolumeWithError[av_i + 1]
    bubbleSort[2] = BoxVolumeWithError[av_i + 2]
    bubbleSort[3] = BoxVolumeWithError[av_i + 3]
    bubbleSort[4] = BoxVolumeWithError[av_i + 4]
    # bubble sorts to get the values in order
    for bi in bubbleSort:
        for bj in range(0, int(4-bi)):
            if bubbleSort[bj] > bubbleSort[bj + 1]:
                bx = bubbleSort[bj]
                bubbleSort[bj] = bubbleSort[bj + 1]
                bubbleSort[bj + 1] = bx
    # puts the average of the middle three, aka it removes the min and max and finds the average of the rest
    threeOf5Box[av_i] = (bubbleSort[2] + bubbleSort[3] + bubbleSort[4]) / 3
    medianOf5Box[av_i] = bubbleSort[3]

# Horizontal tank
for av_i, av_j in enumerate(threeOf5Horizontal, start=0):
    # gets variables ready for bubble sorting
    bubbleSort[0] = HorizontalCylinderWithError[av_i]
    bubbleSort[1] = HorizontalCylinderWithError[av_i + 1]
    bubbleSort[2] = HorizontalCylinderWithError[av_i + 2]
    bubbleSort[3] = HorizontalCylinderWithError[av_i + 3]
    bubbleSort[4] = HorizontalCylinderWithError[av_i + 4]
    # bubble sorts to get the values in order
    for bi in bubbleSort:
        for bj in range(0, int(4-bi)):
            if bubbleSort[bj] > bubbleSort[bj + 1]:
                bx = bubbleSort[bj]
                bubbleSort[bj] = bubbleSort[bj + 1]
                bubbleSort[bj + 1] = bx
    # puts the average of the middle three, aka it removes the min and max and finds the average of the rest
    threeOf5Horizontal[av_i] = (bubbleSort[2] + bubbleSort[3] + bubbleSort[4]) / 3
    medianOf5Horizontal[av_i] = bubbleSort[3]



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
plt.plot(CylinderHeights, CylinderVolumeWithError)
matplotlib.pyplot.title("Cylinder volume with random variation")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Box cylinder with errors
plt.subplot(132)
plt.plot(BoxHeights, BoxVolumeWithError)
matplotlib.pyplot.title("Box volume with random variation")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Horizontal Cylinder plot
plt.subplot(133)
plt.plot(HorizontalCylinderHeights, HorizontalCylinderWithError)
matplotlib.pyplot.title("Horizontal Cylinder volume with random variation")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# plots for the average of 5
# the cylinder tank
plt.figure(3)
plt.subplot(131)
plt.plot(CylinderHeightsAvg5, Average5Cylinder)
matplotlib.pyplot.title("Cylinder Average of 5")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Box cylinder with errors
plt.subplot(132)
plt.plot(BoxHeightsAvg5, Average5Box)
matplotlib.pyplot.title("Box Average of 5")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Horizontal Cylinder plot
plt.subplot(133)
plt.plot(HorizontalCylinderHeightsAvg5, Average5Horizontal)
matplotlib.pyplot.title("Horizontal Cylinder Average of 5")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# plots for the average of 10
# the cylinder tank
plt.figure(4)
plt.subplot(131)
plt.plot(CylinderHeightsAvg10, Average10Cylinder)
matplotlib.pyplot.title("Cylinder Average of 10")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Box cylinderaverage of 10
plt.subplot(132)
plt.plot(BoxHeightsAvg10, Average10Box)
matplotlib.pyplot.title("Box Average of 10")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Horizontal Cylinder average of 10
plt.subplot(133)
plt.plot(HorizontalCylinderHeightsAvg10, Average10Horizontal)
matplotlib.pyplot.title("Horizontal Cylinder Average of 10")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# plots for best 3 of 5
# the cylinder tank
plt.figure(5)
plt.subplot(131)
plt.plot(CylinderHeightsAvg5, threeOf5Cylinder)
matplotlib.pyplot.title("Best 3 of 5 Cylinder")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Box cylinderaverage of 10
plt.subplot(132)
plt.plot(BoxHeightsAvg5, threeOf5Box)
matplotlib.pyplot.title("Best 3 of 5 Box")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Horizontal Cylinder average of 10
plt.subplot(133)
plt.plot(HorizontalCylinderHeightsAvg5, threeOf5Horizontal)
matplotlib.pyplot.title("Best 3 of 5 Horizontal Cylinder")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# plots the median of 5
# the cylinder tank median of 5
plt.figure(6)
plt.subplot(131)
plt.plot(CylinderHeightsAvg5, medianOf5Cylinder)
matplotlib.pyplot.title("Median of 5 Cylinder")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Box median of 5
plt.subplot(132)
plt.plot(BoxHeightsAvg5, medianOf5Box)
matplotlib.pyplot.title("Median of 5 Box")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# Horizontal Cylinder median of 5
plt.subplot(133)
plt.plot(HorizontalCylinderHeightsAvg5, medianOf5Horizontal)
matplotlib.pyplot.title("Median of 5 C Horizontal Cylinder")
matplotlib.pyplot.xlabel("Height")
matplotlib.pyplot.ylabel("Volume")

# shows plots
plt.show()
