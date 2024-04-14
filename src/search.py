def ternary_search(array, left, right, x):
    if right >= left:
        mid1 = int(left + (right - left) / 3)
        mid2 = int(right - (right - left) / 3)

        if array[mid1] == x:
            return mid1
        if array[mid2] == x:
            return mid2

        if x < array[mid1]:
            return ternary_search(array, left, mid1 - 1, x)
        elif x > array[mid2]:
            return ternary_search(array, mid2 + 1, right, x)
        else:
            return ternary_search(array, mid1 + 1, mid2 - 1, x)

    return -1

"""

The worst-case time complexity of ternary search is O(logn)
where n is the length of the input array. To analyze the 
worst-case time complexity, we can use the recurrence relation:

T(n) = 2 + T((2/3) * n) + T((1/3) * n)

The recursion bottoms out when T(1/3 * n) and T((2/3) * n)
have a length of 1, which gives us:

T(k * n) ≤ 2 + k * T(n)

Solving for T(n), we get:

T(n) ≤ 2 * log(n)

Therefore, the worst-case time complexity of ternary search is O(logn).
Note: This analysis assumes a balanced distribution of elements in the
array. In practice, the constant factors and small differences in 
performance might very depending on the data.

"""
