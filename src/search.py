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
The worst-case time complexity of ternary search is O(log3 n)
T(n) = T(n/3) + 4, T(1) = 1
T(n) ≤ 4clog3 n + O(1)
"""
