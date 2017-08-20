def expand_around_center(
    first,
    last,
    current_len,
    longest_len,
    longest_indices,
):
    while first >= 0 and last < len_s:
        if s[first] != s[last]:
            break
        current_len += 2
        if current_len >= longest_len:
            longest_len = current_len
            longest_indices = (first, last)
        first, last = first - 1, last + 1
    return (longest_len, longest_indices)


def longestPalindrome(s):
    """
    :type s: str
    """
    longest_len = 1
    longest_indices = (0,0)
    len_s = len(s)

    for i in range(len_s):
        # handle single center palindrome case
        first, last = i - 1, i + 1
        current_len = 1
        longest_len, longest_indices = expand_around_center(
            first, last,
            current_len,
            longest_len,
            longest_indices,
        )

        # check for dual centers
        if i + 1 >= len_s or s[i] != s[i + 1]:
            continue

        # else handle dual center palindrome case
        current_len = 2
        if current_len >= longest_len:
            longest_len = current_len
            longest_indices = (i, i + 1)
        first, last = i - 1, i + 2
        longest_len, longest_indices = expand_around_center(
            first,
            last,
            current_len,
            longest_len,
            longest_indices,
        )

    return s[longest_indices[0] : longest_indices[1] + 1]
