# assumes s is an ordered set (list, in python)
# time: O(n * 2^n) where n is the length of the set
def powersets(s):
	P = []
	N = 1 << len(s) # save length of the powerset
	for i in range(N): # iterate through all permutations 
		subset = [s[bit] for bit in range(len(s)) if (i & (1 << bit))]
		P.append(subset)
	return P

# time: O(s) where s is the number of set bits 
def number_of_ones(a):
	count = 0;
	while a != 0:
		count += 1; 
		a = a & (a - 1) # remove least significant flipped bit
	return count

# time: O(n * 2^n) where n is the length of the set
def k_sets(s, k):
	P = []
	N = 1 << len(s) 
	for i in range(N): 
		if number_of_ones(i) != k: # check if the i'th permutation includes k elements 
			continue
		subset = [s[bit] for bit in range(len(s)) if (i & (1 << bit))]
		P.append(subset)
	return P

# NOT CORRECT CURRENTLY
def powersets_2(s):
	if len(s) == 0:
		return [[]]
	end = s.pop()
	remainder = powersets_2(s)
	return [[end] + [subset] for subset in remainder] + [remainder]

# time: let max depth be d, and max length at any depth be l. 
#       then O(l^d)
def flatten(ls):
	vals = []
	def _flatten(ls):
		if len(ls) == 0:
			return
		for elem in ls:
			if type(elem) == list:
				_flatten(elem)
			else:
				vals.append(elem)
	_flatten(ls)
	return vals




