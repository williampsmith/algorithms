def two_sum(ls, k):
    """
    Given a list ls and integer k, return whether there exists a set
    of 2 distinct elements of ls that sum to k.
    """
    ls.sort()
    i, j = 0, len(ls) - 1   # iterators
    while i <= j:
        if ls[i] + ls[j] == k:
            return True
        elif ls[i] + ls[j] < k:
            i += 1
        elif ls[i] + ls[j] > k:
            j -= 1
    return False

def three_sum(ls, k):
    """
    Given a list ls and integer k, return whether there exists a set
    of 3 not necessarily distinct elements of ls that sum to k.
    """
    ls.sort()
    return any([two_sum(ls, k - i) for i in ls])
