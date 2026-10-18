import timeit
from typing import Callable, List, Tuple

SortFunction = Callable[[List[int], int, int], List[int]]


class FunctionAnalyzer:
    def __init__(self, repeats: int, test_arrays: List[List[int]], test_name: str):
        self.repeats = repeats
        self.test_arrays = test_arrays
        self.test_name = test_name
        self.function_name = ""
        self.results: List[Tuple[int, float, str]] = []

    def StartTest(self, functionToBeBenchmarked: SortFunction, function_name: str):
        self.function_name = function_name
        self.results = []

        for input_values in self.test_arrays:
            expected = sorted(input_values)
            validation_values = input_values.copy()

            try:
                result = functionToBeBenchmarked(
                    validation_values, 0, len(validation_values) - 1
                )
            except RecursionError:
                self.results.append((len(input_values), -1, "RecursionError"))
                continue

            if result != expected:
                raise AssertionError(
                    f"{function_name} did not sort the input correctly"
                )

            timer = timeit.Timer(
                stmt="sort(values, 0, len(values) - 1)",
                setup="values = original.copy()",
                globals={
                    "sort": functionToBeBenchmarked,
                    "original": input_values,
                },
            )
            try:
                samples = timer.repeat(repeat=self.repeats, number=1)
            except RecursionError:
                self.results.append((len(input_values), -1, "RecursionError"))
                continue

            self.results.append(
                (len(input_values), min(samples), "ok")
            )

    def PrintResult(self):
        print(f"\n{self.function_name} on {self.test_name} arrays:")
        for length, elapsed, status in self.results:
            if elapsed == -1:
                print(f"  Length {length}: {status}")
            else:
                print(f"  Length {length}: {elapsed * 1000:.6f} ms")