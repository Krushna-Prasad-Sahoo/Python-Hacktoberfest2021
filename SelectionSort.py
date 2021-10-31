def SelectionSort(array):
    for i in range(len(array)-1):
        minElementIndex=i
        for j in range(i, len(array)):
            if(array[j]<array[minElementIndex]):
                minElementIndex=j
        array[i], array[minElementIndex]=array[minElementIndex], array[i]
    return array

array=[9, 3, 1, 7, 4, 10, 53, 23, 12, 44]
result=SelectionSort(array)
print(result)
