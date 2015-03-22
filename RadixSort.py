from math import log

#returns the max amount of digits in the list
def maxDigits(data, base):
	return int(round(log(max(abs(num) for num in data)), base) + 1)

#gets the selected digit from num
def getDigit(num, base, digit):
	return (num // (base ** digit)) % base

#sorts the data into buckets
def split(list, base, digit):
	buckets = [[] for _ in range(base)]
	for num in list:
		buckets[getDigit(num, base, digit)].append(num)
	return buckets

#takes an arrary of bnucket arrays and merge them into an ordered list
def merge(buckets):
	result = []
	for bucket in buckets:
		result.extend(bucket)
	return result


#Input: a list of numbers data, and an integer base
#Output: a sorted version of data
#Looks at least significant number first
def lsdRadixSort(data, base):
	#number of sorting passes, based on base 
	#and the amount of digits in the longest number
	passes = maxDigits(data, base)
	result = data[:]
	for digit in range(passes):
		result = merge(split(result, base, digit))
	return result