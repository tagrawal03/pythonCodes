#Code to count number of inversions
#Author: Taruna Agrawal

countInv = 0
# Merge Sort
def mergeSort( num ):
	n = len(num)//2
	if len(num) < 2:
		return
	else:
		leftArr = num[:n]
		rightArr = num[n:]
		mergeSort( leftArr )
		mergeSort( rightArr)
		def merge():
			nL = len(leftArr)
			nR = len(rightArr)
			i = 0; j = 0; k = 0
			while i < nL and j < nR:
				if leftArr[i] < rightArr[j]:
					num[k] = leftArr[i]
					i += 1
				else:
					num[k] = rightArr[j]
					j += 1
					global countInv
					countInv = countInv + nL-i
				k += 1
			while i < nL:
				num[k] = leftArr[i]
				i += 1
				k += 1
			while j < nR:
				num[k] = rightArr[j]
				j += 1
				k += 1
		merge()
		return

num = []
#Read from file
f = open('IntegerArray.txt', 'r')
for line in f:
	num.append(int(line))
f.close()
mergeSort(num)
print ("Number of inversions are ", int(countInv))
