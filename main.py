import random
from typing import List
from analysis import FunctionAnalyzer
from randomized_quick_sort import QuickSort
from randomized_quick_sort import QuickSortFirstPivot
from randomized_quick_sort import RandomizedQuickSort

# helper functions
def GetRandomArray(size: int) -> List[int]:
    return [random.randint(1, size) for _ in range(size)]

# generate an array with duplicate values randomly placed in the array
def GenShuffledDuplicateArray(size: int, values: int) -> List[int]:
    return [random.randint(1, values) for _ in range(size)]


ARRAY_SIZES = {
    "small": 100,
    "medium": 500,
    "large": 1000,
}
REPEATS = 30
SORTS = (
    ("QuickSort (middle pivot)", QuickSort),
    ("QuickSort (first pivot)", QuickSortFirstPivot),
    ("RandomizedQuickSort", RandomizedQuickSort)
)

random.seed(42)
datasets = {"random": [], "sorted": [], "reversed": [], "duplicates": []}

for length in ARRAY_SIZES.values():
    random_values = GetRandomArray(length)
    datasets["random"].append(random_values)
    datasets["sorted"].append(sorted(random_values))
    datasets["reversed"].append(sorted(random_values, reverse=True))
    datasets["duplicates"].append(GenShuffledDuplicateArray(length, 3))


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



def RunSortingBenchmarks():
    analyzers = []
    for test_name, test_arrays in datasets.items():
        for function_name, sort_function in SORTS:
            analyzer = FunctionAnalyzer(REPEATS, test_arrays, test_name)
            analyzer.StartTest(sort_function, function_name)
            analyzers.append(analyzer)

    PrintResults(analyzers)

def TestSortingAlgorithms():
    print("\nTesting sorting algorithms on sample arrays of length 100:")
    for name, arrays in datasets.items():
        for function_name, sort_function in SORTS:
            print(f"\nTesting {function_name} on {name} arrays:")
            test_array = arrays[0].copy()
            print(sort_function(test_array, 0, len(test_array) - 1))
    print("\n Done printing the results\n")



# --------- Main Code. ---------

if __name__ == "__main__":
    # Run the sorting benchmarks and print the results.
    #TestSortingAlgorithms()  # Uncomment this line to test sorting algorithms on sample arrays.

    RunSortingBenchmarks()