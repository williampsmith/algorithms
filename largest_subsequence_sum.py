
def largest_suybsequence_sum(array):
	if not array:
		return 
	largest_interval = (0,0)
	largest_sum = array[0]

	length = len(array)
	for i in range(length):
		for j in range(i, length):
			new_sum = sum(array[i: j + 1]) 
			if new_sum > largest_sum:
				largest_sum = new_sum
				largest_interval = (i,j)

	return largest_interval

def largest_subsequence_sum_dp(array):
	if not array:
		return 
	largest_interval = [0,0]
	largest_sum = 0
	length = len(array)

	for i in range(len(array)):
		if largest_sum + array[i] < 0:
			largest_interval = [i,i]
			largest_sum = array[i]
		else:
			largest_interval[1] = i
			largest_sum += array[i]
	return largest_sum
