def is_palindrome(s):
	string = s.replace(" ", "")
	return string == string[::-1]

def is_palindrome_i(s):
	s = s.replace(" ", "")
	length = len(s)
	for i in range(length // 2):
		if s[i] != s[length - i - 1]:
			return False
	return True

def is_palindrome_r(s):
	s = s.replace(' ', '')
	def _is_palindrome(s):
		print(s)
		if len(s) < 2:
			return True
		if s[0] != s[len(s) - 1]:
			return False
		return _is_palindrome(s[1:len(s) - 1])
	return _is_palindrome(s)

# returns wether the string s can be made palindromic by removing at most k characters
def is_k_palindrome(s, k):
	if len(s) < 2:
		return True
	if s[0] == s[len(s) - 1]:
		return is_k_palindrome(s[1 : len(s) - 1], k)
	else:
		if k <= 0:
			return False
		return is_k_palindrome(s[0 : len(s) - 1], k - 1) or is_k_palindrome(s[1 : len(s)], k - 1)

def is_k_palindrome_dp(s, k):
	rev = s[::-1]
	len1 = len2 = len(s)
	cache = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)] 

	def _k_palindrome_dp(str1, str2, len1, len2, k):
		for i in range(len1 + 1):
			for j in range(len2 + 1):
				if i == 0:
					cache[i][j] = j
				elif j == 0:
					cache[i][j] = i
				elif str1[i - 1] == str2[j - 1]:
					cache[i][j] = cache[i - 1][j - 1]
				else:
					cache[i][j] = 1 + min(cache[i - 1][j], cache[i][j - 1])
		return cache[len1][len2]

	return _k_palindrome_dp(s, rev, len2, len2, k)





