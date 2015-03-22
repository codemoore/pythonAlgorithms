import sys



#Sort a data array by the insertion method
# param data should be an array of comparable objects
def insertionSort (data): 
	for i in range(1, len(data)):
		temp = data[i]
		j = i - 1
		#shift items greater than a[i] to the right
		while (j >= 0) and (data[j] > temp):
			data[j + 1] = data[j]
			j = j - 1
		# insert temp into place
		data[j + 1] = temp 
