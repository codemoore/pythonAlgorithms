
# given a input data array, returns the index of key if it exist
# returns -1 if it does not exist
def binarySearch (data, key): 
	return binarySearchHelper(data, key, 0, len(data) - 1)

def binarySearchHelper(data, key, min, max):
	if (min > max):
		#key does not exist in data
		return -1;
	else:
		mid = min + int (((max - min) / 2))

		if (data[mid] > key):
			#the key is in the first half
			return binarySearchHelper(data, key, min, mid - 1)
		elif (data[mid] < key):
			#the key is in the last half
			return binarySearchHelper(data, key, mid + 1, max)
		else:
			#mid is the key
			return mid