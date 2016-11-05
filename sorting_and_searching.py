# assumes we are given a sorted array
def binary_search(a, k):
	length = len(a)
	if length <= 0:
		return False
	left, right = 0, length - 1
	center = (left + right) // 2

	while left < right:
		print(left, right)
		if k > a[right] or k < a[left]:
			return False
		elif a[center] == k:
			return center
		elif a[left] == k:
			return left
		elif a[right] == k:
			return right
		elif k > a[center]:
			left = center
		else:
			right = center
		center = (left + right) // 2
	return False

def quicksort(a):
	def _quicksort(a, low, high):
		i = partition(a, low, high)
		_quicksort(a, low, i)
		_quicksort(a, i, high)
		return a
	_quicksort(a, 0, len(a))

def mergesort(a):
	if len(a) < 2:
		return a
	center = len(a) // 2
	left, right = a[:center], a[center:]
	left = mergesort(left)
	right = mergesort(right)
	merged = merge(left, right)
	return merged


def merge(a, b):
	a_len, b_len = len(a), len(b)
	i, j = 0,0
	new_array = []

	while i < a_len and j < b_len:
		if a[i] < b[j]:
			new_array.append(a[i])
			i += 1
		else:
			new_array.append(b[j])
			j += 1
	if i < a_len:
		new_array.extend(a[i:])
	elif j < b_len:
		new_array.extend(b[j:])
	return new_array













