def binary_search(sorted_haystack, needle):
    left = 0
    right = len(sorted_haystack) - 1

    # print right

    while left <= right:

        middle = (left + right) // 2

        if sorted_haystack[middle] == needle:
            return middle

        if sorted_haystack[middle] > needle:
            right = middle - 1
        else:
            left = middle + 1

    return None

def binary_search_leftmost(sorted_haystack, needle):
    '''wrong implementation'''

    left = 0
    right = len(sorted_haystack) - 1

    while right - left > 1:

        middle = left + (right - left) / 2

        if sorted_haystack[middle] <= needle:
            left = middle
        else:
            right = middle

        if sorted_haystack[left] == needle:
            return left

    return None

def binary_search_rightmost(sorted_haystack, needle):
    '''wrong implementation'''

    left = 0
    right = len(sorted_haystack) - 1

    while right - left > 1:

        middle = left + (right - left) / 2

        if sorted_haystack[middle] >= needle:
            right = middle
        else:
            left = middle

        if sorted_haystack[right] == needle:
            return right

    return None

def bs_rightmost(array, needle):
    ''' we are sure that array is already sorted ASC'''

    left = 0
    right = len(array) - 1

    while left <= right:

        mid = (left + right) / 2
        if array[mid] > needle:
            right = mid - 1
        else:
            left = mid + 1

    return left
