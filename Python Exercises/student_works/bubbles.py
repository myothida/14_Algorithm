import time
import matplotlib.pyplot as plt

def OptimizedBubbleSort(MyArray):
    StartTime = time.time()
    Length = len(MyArray)
    for Index in range(0, Length-1):
        if MyArray[Index] > MyArray[Index+1]:
            for Index2 in range(0,Index+1):
                if MyArray[Index2] > MyArray[Index2+1]:
                    MyArray[Index2],MyArray[Index2+1] = MyArray[Index2 +1], MyArray[Index2 ]
    EndTime = time.time()
    return(EndTime-StartTime)

MaxNumber = 11
Points = []
PointsY = []
PointsY2 = []
CurrentIndex = 1
for _ in range(0,MaxNumber):
    CurrentIndex*=2
    WorstArray = []
    BestArray = []
    Points.append(CurrentIndex)
    for MaxNumberTemporary in range(0,CurrentIndex):
        WorstArray.append(CurrentIndex-MaxNumberTemporary)
        BestArray.append(MaxNumberTemporary)
    WorstTime = OptimizedBubbleSort(WorstArray)*1000
    BestTime = OptimizedBubbleSort(BestArray)*1000
    PointsY.append(BestTime)
    PointsY2.append(WorstTime)
plt.scatter(Points,PointsY)
plt.scatter(Points,PointsY2)
plt.show()