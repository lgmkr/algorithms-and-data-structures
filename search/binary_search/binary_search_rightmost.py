def binary_search_leftmost(sorted_haystack, needle):
    print sorted_haystack
    print 'needle: ', needle

    left = 0
    right = len(sorted_haystack) - 1

    while right - left > 1:

        middle = left + (right - left) / 2

        print '--------------'
        print 'left: ', left
        print 'right: ', right
        print 'middle: ', middle

        if sorted_haystack[middle] <= needle:
            left = middle
            print 'new-left: ', left
        else:
            right = middle
            print 'new-right: ', right

        print '--------------'

        if sorted_haystack[left] == needle:
            return left

    return None


def binary_search_rightmost(sorted_haystack, needle):
    print sorted_haystack
    print 'needle: ', needle

    left = 0
    right = len(sorted_haystack) - 1

    while right - left > 1:

        middle = left + (right - left) / 2

        print '--------------'
        print 'left: ', left
        print 'right: ', right
        print 'middle: ', middle

        if sorted_haystack[middle] >= needle:
            right = middle
            print 'new-right: ', right
        else:
            left = middle
            print 'new-left: ', left

        print '--------------'

        if sorted_haystack[right] == needle:
            return right

    return None

print 'LEFTMOST'
print binary_search_leftmost([1, 2, 2, 3, 3, 4], 2)

print 'RIGHTMOST'
print binary_search_rightmost([1, 2, 2, 3, 3, 4], 2)
