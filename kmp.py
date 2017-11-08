# Compute temporary array to maintain size of suffix which is same as prefix
# Time/space complexity is O(size of pattern)
def compute_temporary_arry(pattern):
    lps = []
    index = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[index]:
            lps[i] = index + 1;
            index, i = index + 1, i + 1
        else:
            if index != 0:
                index = lps[index - 1]
            else:
                lps[i] = 0;
                i += 1
    return lps


# KMP algorithm of pattern matching.
def KMP(text, pattern):
    lps = compute_temporary_arry(pattern)
    i, j = 0, 0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i, j = i + 1, j + 1
        else:
            if j:
                j = lps[j - 1]
            else:
                i += 1
    return j == len(pattern)
}
