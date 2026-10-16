from randomized_quick_sort import QuickSort
from randomized_quick_sort import QuickSortFirstPivot
from randomized_quick_sort import RandomizedQuickSort

def RandomArrayCreator(size):
    import random
    return [random.randint(1, 100) for _ in range(size)]

arr = RandomArrayCreator(30)

print("Original array:", arr)

QuickSort(arr, 0, len(arr) - 1)
print("Array after QuickSort:", arr)

QuickSortFirstPivot(arr, 0, len(arr) - 1)
print("Array after QuickSortFirstPivot:", arr)

RandomizedQuickSort(arr, 0, len(arr) - 1)
print("Array after RandomizedQuickSort:", arr)