# QuickSort with a middle pivot. Partitioning is in place and takes O(n);
# average time is O(n log n), worst-case time is O(n^2).
def QuickSort(arr, low, high):
    if low < high:
        # For a simple quicksort, the Array is partitioned with pivot as middle element value.
        # we get index of where first part of array ends, and where the second part of array starts.
        # so we have:
            # 0 to left_end, 
            # left_end + 1 to right_start - 1,
            # right_start to high
        # as 3 arrays
        left_end, right_start = Partition(arr, low, high, (low + high) // 2)
        QuickSort(arr, low, left_end)
        QuickSort(arr, right_start, high)

    return arr


# QuickSort variant that chooses the first element as the pivot.
# Time complexity: Just like center pivot: Average case: O(n log n) and Worst case: O(n^2)
# Meanwhile Recurrence: T(n) = T(n-1) + O(n) in the worst case.
# The first-element pivot can produce O(n^2) worst-case time and recursion depth.
def QuickSortFirstPivot(arr, low, high):
    if low < high:
        left_end, right_start = Partition(arr, low, high, low)
        QuickSortFirstPivot(arr, low, left_end)
        QuickSortFirstPivot(arr, right_start, high)

    return arr

# Quick Swap helper function to swap two elements in an array.
def Swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# Randomized QuickSort
# Time complexity: Average case: O(n log n) and the worst case: O(n^2)
# The random pivot makes worst-case behavior unlikely, so average performance is much better in practice
#   - Recurrence (average case): T(n) = 2T(n/2) + O(n) -> O(n log n)
#   - Recurrence (worst case): T(n) = T(n-1) + O(n) -> O(n^2)
def RandomizedQuickSort(arr, low, high):
    if low < high:
        # Selects a random index and partitions the array around that pivot.
        # I was only using 1 value as middle pivot, but this is a 3-way partitioning that handles duplicates better.
        left_end, right_start = RandomizedPartition(arr, low, high)

        # Recurse on values below and above the pivot's equal-value partition.
        # The partitioning cost is O(high - low + 1), and the average total is O(n log n).
        RandomizedQuickSort(arr, low, left_end)
        RandomizedQuickSort(arr, right_start, high)

    return arr

# Three-way partitioning helper function that partitions an array into three parts.
# Using this function for all 3 QuickSorts by passing in the pivot index.
# Returns last index of the left partition and first index of the right partition.
def Partition(arr, low, high, pivot_index):
    pivot = arr[pivot_index]
    left = current = low
    right = high

    # Iterate from the left to the right of the array
    while current <= right:
        if arr[current] < pivot: # Comparing the current element with the pivot
            # We will keep swapping elements all the way left if smaller than the pivot
            Swap(arr, left, current)
            # Increment the left pointer since we know left one already has a value smaller than the pivot
            left += 1
            # Increment the current pointer to continue checking the next element.
            current += 1
        elif arr[current] > pivot:
            # And we move elements all the way right if larger than the pivot
            Swap(arr, current, right)
            # Then we decrement the right pointer to continue checking the next element
            right -= 1
            # current stays same since a new element has been swapped in from the right side and needs to be checked
        else:
            # else we move on to the next value as current regardless.
            current += 1

    return left - 1, right + 1 
# Randomly select a pivot and use the three-way Partition helper.
# Time complexity: O(n) for a given subarray because every element is examined once.
# Space complexity: O(1) extra space because the swap-based partition is done in place.
# This function is the main reason each recursion level costs linear time.

def RandomizedPartition(arr, low, high):
    import random

    pivot_index = random.randint(low, high)
    # Just getting a random index value from the array and passing it to the Partition function to do the actual partitioning.
    return Partition(arr, low, high, pivot_index)
