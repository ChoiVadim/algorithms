def merge(gArray, low, mid1, mid2, high, destArray):
    i = low
    j = mid1
    k = mid2
    l = low

    # Choose smaller of the smallest in the three ranges
    while (i < mid1) and (j < mid2) and (k < high):
        if gArray[i] < gArray[j]:
            if gArray[i] < gArray[k]:
                destArray[l] = gArray[i]
                l += 1
                i += 1
            else:
                destArray[l] = gArray[k]
                l += 1
                k += 1
        else:
            if gArray[j] < gArray[k]:
                destArray[l] = gArray[j]
                l += 1
                j += 1
            else:
                destArray[l] = gArray[k]
                l += 1
                k += 1

    # Case where first and second ranges
    # have remaining values
    while (i < mid1) and (j < mid2):
        if gArray[i] < gArray[j]:
            destArray[l] = gArray[i]
            l += 1
            i += 1
        else:
            destArray[l] = gArray[j]
            l += 1
            j += 1

    # case where second and third ranges
    # have remaining values
    while (j < mid2) and (k < high):
        if gArray[j] < gArray[k]:
            destArray[l] = gArray[j]
            l += 1
            j += 1
        else:
            destArray[l] = gArray[k]
            l += 1
            k += 1

    # Case where first and third ranges have
    # remaining values
    while (i < mid1) and (k < high):
        if gArray[i] < gArray[k]:
            destArray[l] = gArray[i]
            l += 1
            i += 1
        else:
            destArray[l] = gArray[k]
            l += 1
            k += 1

    # Copy remaining values from the first range
    while i < mid1:
        destArray[l] = gArray[i]
        l += 1
        i += 1

    # Copy remaining values from the second range
    while j < mid2:
        destArray[l] = gArray[j]
        l += 1
        j += 1

    # Copy remaining values from the third range
    while k < high:
        destArray[l] = gArray[k]
        l += 1
        k += 1


""" Performing the merge sort algorithm on the 
given array of values in the rangeof indices 
[low, high). low is minimum index, high is 
maximum index (exclusive) """


def mergeSort3WayRec(gArray, low, high, destArray):
    # If array size is 1 then do nothing
    if high - low < 2:
        return

    # Splitting array into 3 parts
    mid1 = low + ((high - low) // 3)
    mid2 = low + 2 * ((high - low) // 3) + 1

    # Sorting 3 arrays recursively
    mergeSort3WayRec(destArray, low, mid1, gArray)
    mergeSort3WayRec(destArray, mid1, mid2, gArray)
    mergeSort3WayRec(destArray, mid2, high, gArray)

    # Merging the sorted arrays
    merge(destArray, low, mid1, mid2, high, gArray)


def mergeSort3Way(gArray, n):
    # if array size is zero return null
    if n == 0:
        return

    # creating duplicate of given array
    fArray = []

    # copying elements of given array into
    # duplicate array
    fArray = gArray.copy()

    # sort function
    mergeSort3WayRec(fArray, 0, n, gArray)

    # copy back elements of duplicate array
    # to given array
    gArray = fArray.copy()

    # return the sorted array
    return gArray


"""
T(n) = 3T(n/3) + O(n) 
By solving it using Master method, we get its complexity as O(n log3n). 
"""