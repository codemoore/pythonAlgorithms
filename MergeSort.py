
#divide and conquer recursive algorithm that Sorts an array of data 
#splits data in half until each part is size 1 and merge them back together in order
#uses indicies to divide list 
def mergeSort(data):
	#when there are 1 or 0 elements int the array
	if (len(data) <= 1):
		return data
	mid = int(len(data) / 2)
	#intialize 2 parts of size mid with all 0's
	left = [0]*mid
	right = [0]*(len(data) - mid)
	#fill left with the left side of the list
	for i in range(0, mid):
		left[i] = data[i]
	#fill part 2 with the right side
	for j in range(mid, len(data)):
		right[j - mid] = data[j]
	#sort each side recursively
	left = mergeSort(left)
	right = mergeSort(right)
	#merge 2 parts into one sorted list
	return merge(left, right)	


#take 2 sorted lists and merge them into one sorted list
def merge (left, right):
	result = [0]*(len(left)+len(right))
	#intialize index iterators
	i = 0
	j = 0
	k = 0
	while ((i < len(left)) or (j < len(right))):
		#if both parts have elements left
		if ((i < len(left)) and (j < len(right))):
			#add from left if that element is smaller
			if(left[i] <= right[j]):
				result[k] = left[i]
				k = k+1
				i = i+1
			#if the next element in left is bigger, add from right
			else:
				result[k] = right[j]
				k = k+1
				j = j+1
 		#if only part 1 has elements left add rest to result
		elif ((i < len(left))):
			result[k] = left[i]
			k = k+1
			i = i+1
 		#if only right has elements left add rest to result
		elif ((j < len(right))):
			result[k] = right[j]
			k = k+1
			j = j+1	
	return result

