import random
from typing import List
from analysis import FunctionAnalyzer
from randomized_quick_sort import QuickSort
from randomized_quick_sort import QuickSortFirstPivot
from randomized_quick_sort import RandomizedQuickSort


def GetRandomArray(size: int) -> List[int]:
    return random.sample(range(size), size)

def test_sorting_algorithms(arr):
    arr = GetRandomArray(30)
    print("Original array:", arr)

    QuickSort(arr, 0, len(arr) - 1)
    print("Array after QuickSort:", arr)

    QuickSortFirstPivot(arr, 0, len(arr) - 1)
    print("Array after QuickSortFirstPivot:", arr)

    RandomizedQuickSort(arr, 0, len(arr) - 1)
    print("Array after RandomizedQuickSort:", arr)



def PrintResults(analyzers: List[FunctionAnalyzer]):
    function_names = list(dict.fromkeys(
        analyzer.function_name for analyzer in analyzers if analyzer.function_name
    ))
    test_names = list(dict.fromkeys(
        analyzer.test_name
        for analyzer in analyzers
    ))
    lengths = sorted({
        length
        for analyzer in analyzers
        for length, _, _ in analyzer.results
    })

    results = {
        (analyzer.function_name, analyzer.test_name, length): (
            f"{elapsed * 1000:.9f}" if elapsed != -1 else status
        )
        for analyzer in analyzers
        for length, elapsed, status in analyzer.results
    }

    for length in lengths:
        headers = ["Algorithm"] + test_names
        rows = [
            [function_name] + [
                results.get((function_name, test_name, length), "-")
                for test_name in test_names
            ]
            for function_name in function_names
        ]
        column_widths = [
            max(len(headers[index]), *(len(row[index]) for row in rows))
            for index in range(len(headers))
        ]

        print(f"\nResults for arrays of length {length}:")
        print(" | ".join(
            value.ljust(column_widths[index])
            for index, value in enumerate(headers)
        ))
        print("-+-".join("-" * width for width in column_widths))
        for row in rows:
            print(" | ".join(
                value.ljust(column_widths[index])
                for index, value in enumerate(row)
            ))


ARRAY_SIZES = {
    "small": 100,
    "medium": 500,
    "large": 1000,
}
REPEATS = 30
SORTS = (
    ("QuickSort (middle pivot)", QuickSort),
    ("QuickSort (first pivot)", QuickSortFirstPivot),
    ("RandomizedQuickSort", RandomizedQuickSort),
)

random.seed(42)
datasets = {"random": [], "sorted": [], "reversed": []}

for length in ARRAY_SIZES.values():
    random_values = GetRandomArray(length)
    datasets["random"].append(random_values)
    datasets["sorted"].append(sorted(random_values))
    datasets["reversed"].append(sorted(random_values, reverse=True))

analyzers = []
for test_name, test_arrays in datasets.items():
    for function_name, sort_function in SORTS:
        analyzer = FunctionAnalyzer(REPEATS, test_arrays, test_name)
        analyzer.StartTest(sort_function, function_name)
        analyzers.append(analyzer)

PrintResults(analyzers)