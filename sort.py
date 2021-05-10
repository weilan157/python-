# coding = utf-8


def bubbleSort(arr):
    # 冒泡排序
    dataLength = len(arr)
    for i in range(dataLength):
        for j in range(i, dataLength):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def selectionSort(arr):
    # 选择排序
    dataLength = len(arr)
    for i in range(dataLength):
        minData = i
        for j in range(i, dataLength):
            if arr[j] < arr[minData]:
                minData = j
        if minData != i:
            arr[i], arr[minData] = arr[minData], arr[i]
    return arr


def insertionSort(arr):
    # 插入排序
    dataLength = len(arr)
    for perIndex in range(dataLength):
        while perIndex > 0 and arr[perIndex-1] > arr[perIndex]:
            arr[perIndex-1], arr[perIndex] = arr[perIndex], arr[perIndex-1]
            perIndex -= 1
    return arr


def shellSort(arr):
    # 希尔排序
    dataLength = len(arr)
    gap = dataLength // 2
    while gap > 0:
        for i in range(gap, dataLength):
            while i > 0 and arr[i-gap] > arr[i]:
                arr[i-gap], arr[i] = arr[i], arr[i-gap]
                i -= gap
        gap //= 2
    return arr


def mergeSort(arr):
    # 归并排序
    dataLength = len(arr)
    if dataLength <= 1:
        return arr
    mid = dataLength // 2
    leftList = mergeSort(arr[:mid])
    rightList = mergeSort(arr[mid:])
    leftCursor, rightCursor = 0, 0
    outputList = []
    while leftCursor < len(leftList) and rightCursor < len(rightList):
        if leftList[leftCursor] < rightList[rightCursor]:
            outputList.append(leftList[leftCursor])
            leftCursor += 1
        else:
            outputList.append(rightList[rightCursor])
            rightCursor += 1
    outputList += leftList[leftCursor:]
    outputList += rightList[rightCursor:]
    return outputList


def quickSort(arr, first=0, last=0):
    # 快速排序
    low = first
    high = last
    midValue = arr[first]
    if not high:
        dataLength = len(arr)
        high = dataLength-1
    if low >= high:
        return

    while low < high:
        while low < high and arr[high] >= midValue:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] < midValue:
            low += 1
        arr[high] = arr[low]

    arr[low] = midValue
    quickSort(arr, first, high-1)
    quickSort(arr, low+1, last)
    return arr


if __name__ == "__main__":
    arr = [3, 2, 1, 4, 5, 6, 9, 8, 7, 10, 0]
    print(arr)
    # print(bubbleSort(arr))
    # print(selectionSort(arr))
    # print(insertionSort(arr))
    # print(shellSort(arr))
    # print(mergeSort(arr))
    print(quickSort(arr))
