# assumes we are given a sorted array
def binary_search(a, k):
	length = len(a)
	if length <= 0:
		return False
	left, right = 0, length - 1
	center = (left + right) // 2

	while left < right:
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
	def _quicksort(a, start, end):
		if start < end:
			# partition the list
			pivot = partition(a, start, end)
			# sort both halves
			_quicksort(a, start, pivot - 1)
			_quicksort(a, pivot + 1, end)
		return a

def partition(a, start, end):
	pivot = a[start]
	left = start + 1
	right = end
	done = False

	while not done:
		while left <= right and a[left] <= pivot:
			left = left + 1
		while right >= left and a[right] >= pivot:
			right = right - 1
		if right < left:
			done = True
		else:
			# swap
			a[left], a[right] = a[right], a[left]
	# place pivot in proper place
	a[start], a[right] = a[right], a[start]
	return right

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













