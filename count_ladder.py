# returns the number of ways to get to the top of a ladder of 
# size n by taking steps between 0 and m.
def count_ladder(n, m):
	n = n + 1

	#base cases
	counts = {s:s for s in range(3)} 

	for i in range(3, n):
		counts[i] = 0
		steps = 1
		while steps <= m and steps <= i:
			counts[i] = counts[i] + counts[i - steps]
			steps = steps + 1
	return counts[n - 1]