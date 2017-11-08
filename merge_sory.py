def merge(arr1, arr2):
    """
    Assumes no duplicates
    """
    i, j = 0, 0
    result_arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result_arr.append(arr1[i])
            i += 1
        else:
            result_arr.append(arr2[j])
            j += 1
    if i != len(arr1):
        result_arr.extend(arr1[i:])
    if j != len(arr2):
        result_arr.extend(arr2[j:])
    return result_arr

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        return arr if arr[0] < arr[1] else arr[::-1]
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]
    return merge(merge_sort(left_arr), merge_sort(right_arr))

test_arr1 = [3,7,4,8,1,5,9,0,2]
test_arr2 = [3,7,4,8,1,5,9,0,2,6]
print('Testing test_arr1:', merge_sort(test_arr1))
print('Testing test_arr2:', merge_sort(test_arr2))
