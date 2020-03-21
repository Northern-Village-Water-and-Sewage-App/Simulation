import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math

# Number of sample heights, needs to be a multiple of 10
N: int = 1000

# statistical
# number of times the test is run
M: int = 1
# holds the variance, C for cylinder, B for box, h for horizontal cylinder, 1 for regular
VarC1 = 0
VarB1 = 0
VarH1 = 0
# average of 5
VarC5 = 0
VarB5 = 0
VarH5 = 0
# average of 10
VarC10 = 0
VarB10 = 0
VarH10 = 0
# best of 3 of 5
VarC3 = 0
VarB3 = 0
VarH3 = 0
# median
VarCM = 0
VarBM = 0
VarHM = 0
# worst case
# regular
WCC1 = 0
WCB1 = 0
WCH1 = 0
# average of 5
WCC5 = 0
WCB5 = 0
WCH5 = 0
# average of 10
WCC10 = 0
WCB10 = 0
WCH10 = 0
# best of 3 of 5
WCC3 = 0
WCB3 = 0
WCH3 = 0
# median
WCCM = 0
WCBM = 0
WCHM = 0

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

# create the vectors to hold the averages
Average5Cylinder = np.zeros(int(N / 5))
Average5Box = np.zeros(int(N / 5))
Average5Horizontal = np.zeros(int(N / 5))

# create the vectors to hold the averages
Average10Cylinder = np.zeros(int(N / 10))
Average10Box = np.zeros(int(N / 10))
Average10Horizontal = np.zeros(int(N / 10))

# Min and max removed, plus the average of 3 and median of 5
# create the vectors to hold results
threeOf5Cylinder = np.zeros(int(N / 5))
threeOf5Box = np.zeros(int(N / 5))
threeOf5Horizontal = np.zeros(int(N / 5))
medianOf5Cylinder = np.zeros(int(N / 5))
medianOf5Box = np.zeros(int(N / 5))
medianOf5Horizontal = np.zeros(int(N / 5))

# for the bubble sort
bubbleSort = np.zeros(5)

# enumerate makes 2 variables, i is the index, and j is the value inside the vector HorizontalCylinderHeights
for i, j in enumerate(HorizontalCylinderHeights, start=0):

    # if the tank is less than half empty one equation is used
    if j < R:
        AreaOfSector = math.pi * R * R * (math.acos((R - j) / R)) / (2 * math.pi)
        AreaOfTriangle = 0.5 * math.sqrt(R * R - (R - j) * (R - j)) * (R - j)
        HorizontalCylinderVolume[i] = (AreaOfSector - AreaOfTriangle) * L * 2

    # if the tank is more than half empty the other equation is used
    else:
        AreaOfSector = math.pi * R * R * (math.acos((j - R) / R)) / (2 * math.pi)
        AreaOfTriangle = 0.5 * math.sqrt(R * R - (j - R) * (j - R)) * (j - R)
        HorizontalCylinderVolume[i] = LargeTankVolume - (AreaOfSector - AreaOfTriangle) * L * 2

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


# this is where the for loop should start

for p in range(0, M):
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
                                     + HorizontalCylinderWithError[av_i + 8] + HorizontalCylinderWithError[
                                         av_i + 9]) / 10

    # best 3 of 5 and median
    # Cylinder tank
    for av_i, av_j in enumerate(threeOf5Cylinder, start=0):
        # gets variables ready for bubble sorting
        bubbleSort[0] = CylinderVolumeWithError[av_i]
        bubbleSort[1] = CylinderVolumeWithError[av_i + 1]
        bubbleSort[2] = CylinderVolumeWithError[av_i + 2]
        bubbleSort[3] = CylinderVolumeWithError[av_i + 3]
        bubbleSort[4] = CylinderVolumeWithError[av_i + 4]
        # bubble sorts to get the values in order
        for bi in bubbleSort:
            for bj in range(0, int(4 - bi)):
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
            for bj in range(0, int(4 - bi)):
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
            for bj in range(0, int(4 - bi)):
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
            for bj in range(0, int(4 - bi)):
                if bubbleSort[bj] > bubbleSort[bj + 1]:
                    bx = bubbleSort[bj]
                    bubbleSort[bj] = bubbleSort[bj + 1]
                    bubbleSort[bj + 1] = bx
        # puts the average of the middle three, aka it removes the min and max and finds the average of the rest
        threeOf5Horizontal[av_i] = (bubbleSort[2] + bubbleSort[3] + bubbleSort[4]) / 3
        medianOf5Horizontal[av_i] = bubbleSort[3]

    # Finding the variation                                          This doesn't work I need to make the vectors match
    for r, q in enumerate(Average5Horizontal, start=0):
        # Variance
        VarC1 += (CylinderVolume[r * 5] - q) * (CylinderVolume[r * 5] - q)
        VarC5 += (CylinderVolume[r * 5] - Average5Cylinder[r]) * (CylinderVolume[r * 5] - Average5Cylinder[r])
        VarC3 += (CylinderVolume[r * 5] - threeOf5Cylinder[r]) * (CylinderVolume[r * 5] - threeOf5Cylinder[r])
        VarCM += (CylinderVolume[r * 5] - medianOf5Cylinder[r]) * (CylinderVolume[r * 5] - medianOf5Cylinder[r])
        VarB1 += (BoxVolume[r * 5] - BoxVolumeWithError[r]) * (BoxVolume[r * 5] - BoxVolumeWithError[r])
        VarB5 += (BoxVolume[r * 5] - Average5Box[r]) * (BoxVolume[r * 5] - Average5Box[r])
        VarB3 += (BoxVolume[r * 5] - threeOf5Box[r]) * (BoxVolume[r * 5] - threeOf5Box[r])
        VarBM += (BoxVolume[r * 5] - medianOf5Box[r]) * (BoxVolume[r * 5] - medianOf5Box[r])
        VarH1 += math.pow((HorizontalCylinderVolume[r * 5] - HorizontalCylinderWithError[r]), 2)
        VarH5 += math.pow((HorizontalCylinderVolume[r * 5] - Average5Horizontal[r]), 2)
        VarH3 += math.pow((HorizontalCylinderVolume[r * 5] - threeOf5Horizontal[r]), 2)
        VarHM += math.pow((HorizontalCylinderVolume[r * 5] - medianOf5Horizontal[r]), 2)
        # Worst case
        # Cylinders
        if (CylinderVolume[r * 5] - Average5Cylinder[r]) * (CylinderVolume[r * 5] - Average5Cylinder[r]) > WCC1:
            WCC1 = (CylinderVolume[r * 5] - Average5Cylinder[r]) * (CylinderVolume[r * 5] - Average5Cylinder[r])
        if (CylinderVolume[r * 5] - Average5Cylinder[r]) * (CylinderVolume[r * 5] - Average5Cylinder[r]) > WCC5:
            WCC5 = (CylinderVolume[r * 5] - Average5Cylinder[r]) * (CylinderVolume[r * 5] - Average5Cylinder[r])
        if (CylinderVolume[r * 5] - threeOf5Cylinder[r]) * (CylinderVolume[r * 5] - threeOf5Cylinder[r]) > WCC3:
            WCC3 = (CylinderVolume[r * 5] - threeOf5Cylinder[r]) * (CylinderVolume[r * 5] - threeOf5Cylinder[r])
        if (CylinderVolume[r * 5] - medianOf5Cylinder[r]) * (CylinderVolume[r * 5] - medianOf5Cylinder[r]) > WCCM:
            WCCM = (CylinderVolume[r * 5] - medianOf5Cylinder[r]) * (CylinderVolume[r * 5] - medianOf5Cylinder[r])
        # Boxes
        if (BoxVolume[r * 5] - BoxVolumeWithError[r]) * (BoxVolume[r] - BoxVolumeWithError[r]) > WCB1:
            WCB1 = (BoxVolume[r * 5] - BoxVolumeWithError[r]) * (BoxVolume[r] - BoxVolumeWithError[r])
        if (BoxVolume[r * 5] - Average5Box[r]) * (BoxVolume[r * 5] - Average5Box[r]) > WCB5:
            WCB5 = (BoxVolume[r * 5] - Average5Box[r]) * (BoxVolume[r * 5] - Average5Box[r])
        if (BoxVolume[r * 5] - threeOf5Box[r]) * (BoxVolume[r * 5] - threeOf5Box[r]) > WCB3:
            WCB3 = (BoxVolume[r * 5] - threeOf5Box[r]) * (BoxVolume[r * 5] - threeOf5Box[r])
        if (BoxVolume[r * 5] - medianOf5Box[r]) * (BoxVolume[r * 5] - medianOf5Box[r]) > WCBM:
            WCBM = (BoxVolume[r * 5] - medianOf5Box[r]) * (BoxVolume[r * 5] - medianOf5Box[r])
        # Horizontal
        if math.pow((HorizontalCylinderVolume[r * 5] - HorizontalCylinderWithError[r]), 2) > WCH1:
            WCH1 = math.pow((HorizontalCylinderVolume[r * 5] - HorizontalCylinderWithError[r]), 2)
        if math.pow((HorizontalCylinderVolume[r * 5] - Average5Horizontal[r]), 2) > WCH5:
            WCH5 = math.pow((HorizontalCylinderVolume[r * 5] - Average5Horizontal[r]), 2)
        if math.pow((HorizontalCylinderVolume[r * 5] - threeOf5Horizontal[r]), 2) > WCH3:
            WCH3 = math.pow((HorizontalCylinderVolume[r * 5] - threeOf5Horizontal[r]), 2)
        if math.pow((HorizontalCylinderVolume[r * 5] - medianOf5Horizontal[r]), 2) > WCHM:
            WCHM = math.pow((HorizontalCylinderVolume[r * 5] - medianOf5Horizontal[r]), 2)

    for r,q in enumerate(Average10Box, start=0):
        VarC10 += (CylinderVolume[r * 10] - Average10Cylinder[r]) * (CylinderVolume[r * 10] - Average10Cylinder[r])
        VarB10 += (BoxVolume[r * 10] - Average10Box[r]) * (BoxVolume[r * 10] - Average10Box[r])
        VarH10 += math.pow((HorizontalCylinderVolume[r * 10] - Average10Horizontal[r]), 2)
        # Find the worst case
        if (CylinderVolume[r * 10] - Average10Cylinder[r]) * (CylinderVolume[r * 10] - Average10Cylinder[r]) > WCC10:
            WCC10 = (CylinderVolume[r * 10] - Average10Cylinder[r]) * (CylinderVolume[r * 10] - Average10Cylinder[r])
        if (BoxVolume[r * 10] - Average10Box[r]) * (BoxVolume[r * 10] - Average10Box[r]) > WCB10:
            WCB10 = (BoxVolume[r * 10] - Average10Box[r]) * (BoxVolume[r * 10] - Average10Box[r])
        if math.pow((HorizontalCylinderVolume[r * 10] - Average10Horizontal[r]), 2) > WCH10:
            WCH10 = math.pow((HorizontalCylinderVolume[r * 10] - Average10Horizontal[r]), 2)

# for loop ends here
# output the results

print("Number of simulation: " + str(M))
print("Variation in Cylinder with error: " + str(math.sqrt(VarC1 / (M * N / 5))))
print("Variation in Cylinder Average of 5: " + str(math.sqrt(VarC5 / (M * N / 5))))
print("Variation in Cylinder Average of 10: " + str(math.sqrt(VarC10 / (M * N / 10))))
print("Variation in Cylinder Best 3 of 5: " + str(math.sqrt(VarC3 / (M * N / 5))))
print("Variation in Cylinder Median of 5: " + str(math.sqrt(VarCM / (M * N / 5))))
print("Variation in Box with error: " + str(math.sqrt(VarB1 / (M * N / 5))))
print("Variation in Box Average of 5: " + str(math.sqrt(VarB5 / (M * N / 5))))
print("Variation in Box Average of 10: " + str(math.sqrt(VarB10 / (M * N / 10))))
print("Variation in Box Best 3 of 5: " + str(math.sqrt(VarB3 / (M * N / 5))))
print("Variation in Box Median of 5: " + str(math.sqrt(VarBM / (M * N / 5))))
print("Variation in Horizontal with error: " + str(math.sqrt(VarH1 / (M * N / 5))))
print("Variation in Horizontal Average of 5: " + str(math.sqrt(VarH5 / (M * N / 5))))
print("Variation in Horizontal Average of 10: " + str(math.sqrt(VarH10 / (M * N / 10))))
print("Variation in Horizontal Best 3 of 5: " + str(math.sqrt(VarH3 / (M * N / 5))))
print("Variation in Horizontal Median of 5: " + str(math.sqrt(VarHM / (M * N / 5))))
print("\nWorst Case")
print("Worst Case Cylinder: " + str(WCC1) + ", " + str(WCC5) + ", " + str(WCC10) + ", " + str(WCC3) + ", " + str(WCCM))
print("Worst Case Box: " + str(WCB1) + ", " + str(WCB5) + ", " + str(WCB10) + ", " + str(WCB3) + ", " + str(WCBM))
print("Worst Case Horizontal: " + str(WCH1) + ", " + str(WCH5) + ", " + str(WCH10) + ", " + str(WCH3) + ", " +str(WCHM))
