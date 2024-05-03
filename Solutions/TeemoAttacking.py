from typing import List



def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
    totalPoisonedTime = 0
    for i in range(len(timeSeries)):
        print(totalPoisonedTime, timeSeries[i])
        if ((timeSeries[i] - timeSeries[i - 1]) < duration) and ((timeSeries[i] - timeSeries[i - 1]) > 0):
            totalPoisonedTime += timeSeries[i] - timeSeries[i - 1]
        else:
            totalPoisonedTime += duration
    return totalPoisonedTime


print(findPoisonedDuration([1, 3, 5, 7], 2))
