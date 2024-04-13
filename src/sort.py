def bubble_sort(arr: list, reverse: bool = False) -> list:
    """
    Complexity: O(n^2)
    Space Complexity: O(1)
    """
    if len(arr) <= 1:
        return arr
    
    if reverse:
        for i in range(len(arr)):
            for j in range(len(arr) - 1, i, -1):
                if arr[j] > arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]

    else:
        for i in range(len(arr)):
            for j in range(len(arr) - 1, i, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr

def selection_sort(arr: list) -> list:
    """
    Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr: list) -> list:
    """
    Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr: list) -> list:
    """
    Complexity: O(n log n), Worth O(n^2) if the list is already sorted
    Space Complexity: O(log n)
    """
    # Base case: if the list has 1 or fewer elements, return it as is
    if len(arr) <= 1:
        return arr

    # Pick a pivot element from the list
    pivot = arr[len(arr) // 2]

    # Divide the list into three parts: elements less than the pivot,
    # elements equal to the pivot, and elements greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the three parts and concatenate them
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr: list) -> list:
    """
    Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Base case: if the list has 1 or fewer elements, return it as is
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves   
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left: list, right: list) -> list:
    merged = []
    i = j = 0

    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements
    merged += left[i:]
    merged += right[j:]

    return merged


def heap_sort(arr: list) -> list:
    """
    Complexity: O(n log n)
    Space Complexity: O(1)
    """
    # Build the heap
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))

    # Sort the heap
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    return arr

def heapify(arr: list, i: int, length: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < length and arr[left] > arr[largest]:
        largest = left
    if right < length and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, length)


def main():
    return 0

if __name__ == "__main__":
    main()


