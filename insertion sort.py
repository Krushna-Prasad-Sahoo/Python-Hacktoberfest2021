
def insertionSort(arr):

	
	for i in range(1, len(arr)):

		ind = arr[i]
		j = i-1
		while j >=0 and ind < arr[j] :
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = ind


n=int(input())
arr=[]
for i in range(n)):
	val=int(input())
	arr.append(val)

insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])

