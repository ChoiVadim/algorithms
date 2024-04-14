def ThreeWayMergeSort(array, left, right):
    if right - left <= 1:
        return

    third = (right - left) / 3
    mid1 = left + third
    mid2 = mid1 + third

    ThreeWayMergeSort(array, left, mid1)
    ThreeWayMergeSort(array, mid1, mid2)
    ThreeWayMergeSort(array, mid2, right)

    MergeThreeWay(array, left, mid1, mid2, right)

def MergeThreeWay(array, left, mid1, mid2, right):
    leftArray = array[left:mid1]
    middleArray = array[mid1:mid2]
    rightArray = array[mid2:right]

    i = j = k = 0
    index = left

    while i < len(leftArray) and j < len(middleArray) and k < len(rightArray):
        minElement = min(leftArray[i], middleArray[j], rightArray[k])

        if minElement == leftArray[i]:
            array[index] = leftArray[i]
            i += 1
        elif minElement == middleArray[j]:
            array[index] = middleArray[j]
            j += 1
        else:
            array[index] = rightArray[k]
            k += 1
        index += 1

    return array


import unittest

class TestThreeWayMergeSort(unittest.TestCase):

    def test_sort_array_of_three(self):
        array = [3, 2, 1]
        left = 0
        right = 3
        ThreeWayMergeSort(array, left, right)
        self.assertEqual(array, [1, 2, 3])

    def test_sort_array_of_five(self):
        array = [5, 4, 3, 2, 1]
        left = 0
        right = 5
        ThreeWayMergeSort(array, left, right)
        self.assertEqual(array, [1, 2, 3, 4, 5])

    def test_sort_array_of_seven(self):
        array = [7, 6, 5, 4, 3, 2, 1]
        left = 0
        right = 7
        ThreeWayMergeSort(array, left, right)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7])

    def test_sort_array_of_ten(self):
        array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        left = 0
        right = 10
        ThreeWayMergeSort(array, left, right)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()