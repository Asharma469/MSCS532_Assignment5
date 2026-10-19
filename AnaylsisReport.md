# Quicksort Performance Analysis

## 1. Introduction

This report compares three versions of Quicksort: one that chooses the middle
index as its pivot, one that chooses the first element, and one that chooses a
random pivot. All three use the same in-place, three-way partition routine.
The goal is to see how pivot choice affects performance on random, sorted,
reverse-sorted, and duplicate-heavy arrays.

The results do not show one version winning every time. The middle-index
version is especially fast on the sorted and reverse-sorted arrays tested.
Randomized Quicksort is less dependent on the input's original order, which
makes its performance more predictable across different inputs, although it
does not guarantee that every run will be fast.

## 2. Implementation Details

At each step, Quicksort picks a pivot and partitions the current part of the
array into three groups: values smaller than the pivot, values equal to it,
and values larger than it. The partition changes the original array rather
than building separate arrays. Quicksort then recursively sorts only the
smaller and larger groups. Values equal to the pivot are already together, so
they do not need more recursive work.

The three versions differ in how they choose the pivot:

- **Middle-index pivot:** chooses the value at the middle index of the current
  subarray. It does not search for the median value.
- **First-element pivot:** chooses the first value in the current subarray.
- **Randomized pivot:** chooses an index at random from the current subarray.

The shared `Partition` function scans the subarray once. When it finds a
value smaller than the pivot, it swaps that value toward the left boundary;
when it finds a larger value, it swaps it toward the right boundary and checks
the newly swapped-in value. Equal values stay between those two regions. The
partition returns boundaries that let the caller recurse only on the
less-than and greater-than portions.

The deterministic functions choose either the middle index or the first
index, call `Partition`, and recursively sort the two outer portions. The
randomized function chooses an index uniformly from the current subarray and
passes it to the same partition routine. The implementations are in
`randomized_quick_sort.py`; `main.py` creates test inputs and runs the
benchmark, while `analysis.py` contains the timing helper.

## 3. Performance Analysis

Partitioning a subarray of n values takes O(n) time because each value is
examined. The total time depends on how the pivot divides the remaining
values. All three pivot strategies have the same broad best- and worst-case
bounds; the pivot rule affects how often a particular input reaches those
patterns.

| Case | Time | What must happen |
|---|---|---|
| Best | O(n log n) | Pivots divide the values into roughly equal groups, creating about log n levels of O(n) partition work. |
| Average | O(n log n) | Partitions are reasonably balanced on average. For randomized Quicksort this is expected over random pivot choices; for deterministic versions it depends on the input distribution and pivot rule. |
| Worst | O(n²) | Pivots repeatedly leave one side empty or tiny, giving T(n) = T(n - 1) + O(n). |

The deterministic middle-index and first-element versions both have O(n log
n) best-case time and O(n²) worst-case time. On random permutations of
distinct values, either fixed-position pivot has O(n log n) expected time,
but specially ordered or otherwise unfavorable data can still produce the
quadratic case. Randomized Quicksort has O(n log n) expected time regardless
of the original ordering when pivot choices are uniform, but it also retains
an O(n²) worst case.

The average or expected O(n log n) result does not require every partition
to be exactly half and half. It follows because reasonably balanced splits
produce about O(log n) levels, while the partition work across each level
sums to O(n). Random pivot selection gives a good expected balance across
many partitions, even though an individual pivot may be poor. The same
expected bound applies to the deterministic versions when the input is a
random permutation of distinct values, because the value at a fixed index
then has a random rank. It is not a guarantee for every input ordering.

Partitioning itself is in place and uses O(1) auxiliary space. The recursive
call stack is additional space: O(log n) when splits are balanced and O(n) in
the worst case. Randomized Quicksort also uses a small constant amount of
space for pivot selection; it does not allocate another array proportional
to the input size. Other overheads include Python function calls, comparisons
and swaps, and random-number generation for the randomized version.

## 4. Effect of Randomization

With a fixed pivot rule, an input can repeatedly put the pivot near one
extreme and cause badly unbalanced partitions. Choosing a random pivot makes
that relationship to the original input order less predictable. Across
random choices, the expected running time is O(n log n), so randomization is
a useful way to reduce the chance of consistently poor splits when input
order is unknown or controlled by someone else.

Randomization is not a promise that every run will be fast. A sequence of
unlucky pivots can still take O(n²) time and O(n) stack space. It can also be
slightly slower on easy or small inputs because selecting random pivots adds
work. The empirical results below illustrate the trade-off: randomized
Quicksort is not always fastest, but its performance is less sensitive to
sorted and reversed input than first-pivot Quicksort.

## 5. Empirical Analysis

The tests use arrays of 100, 500, and 1,000 values. For each length, the input
is random, sorted, reverse-sorted, or duplicate-heavy. Random arrays are
generated by independently choosing each value from 1 through the array
length, so random inputs can contain repeated values. The sorted and
reverse-sorted cases are ordered versions of the corresponding random array.
The duplicate-heavy arrays use values from 1 through 3. Each case is timed 30
times, and the smallest time is reported. Before each timed sort, the
benchmark prepares a fresh copy of the original array outside the timed
statement. It also checks that each algorithm sorts correctly by comparing
its result with Python's `sorted` function.

The measurements below are in milliseconds. The supplied results did not
include the computer or Python version used, so the exact times may differ on
another system.

### 5.1 Results

#### Arrays of 100 Elements

| Algorithm | Random (ms) | Sorted (ms) | Reversed (ms) | Duplicates (ms) |
|---|---:|---:|---:|---:|
| QuickSort (middle pivot) | 0.086200191 | **0.076700002** | **0.069599831** | 0.018100021 |
| QuickSort (first pivot) | **0.079700025** | 0.153000001 | 0.404499937 | **0.015700003** |
| RandomizedQuickSort | 0.094200019 | 0.090399990 | 0.088399975 | 0.016399892 |

#### Arrays of 500 Elements

| Algorithm | Random (ms) | Sorted (ms) | Reversed (ms) | Duplicates (ms) |
|---|---:|---:|---:|---:|
| QuickSort (middle pivot) | **0.657700002** | **0.492000021** | **0.478300033** | 0.089500099 |
| QuickSort (first pivot) | 0.673899893 | 1.566600055 | 9.529100033 | 0.093100127 |
| RandomizedQuickSort | 0.682399841 | 0.641099876 | 0.627200119 | **0.076500000** |

#### Arrays of 1,000 Elements

| Algorithm | Random (ms) | Sorted (ms) | Reversed (ms) | Duplicates (ms) |
|---|---:|---:|---:|---:|
| QuickSort (middle pivot) | 1.487999922 | **1.183100045** | **1.172099961** | 0.203399919 |
| QuickSort (first pivot) | **1.322599826** | 4.288499942 | 40.889600059 | 0.171900028 |
| RandomizedQuickSort | 1.625400037 | 1.521500060 | 1.503899926 | **0.150099862** |

Bold numbers mark the fastest algorithm for each input type and size. All
algorithms completed these benchmark cases, although first-pivot Quicksort was
much slower on the 1,000-element reverse-sorted input.

#### Comparing Input Types Across Sizes

Each cell lists the middle-pivot, first-pivot, and randomized timings. The
fastest successful time in each cell is bolded.

| Distribution | 100 elements | 500 elements | 1,000 elements |
|---|---|---|---|
| Random | Middle: 0.086200191<br>First: **0.079700025**<br>Randomized: 0.094200019 | Middle: **0.657700002**<br>First: 0.673899893<br>Randomized: 0.682399841 | Middle: 1.487999922<br>First: **1.322599826**<br>Randomized: 1.625400037 |
| Sorted | Middle: **0.076700002**<br>First: 0.153000001<br>Randomized: 0.090399990 | Middle: **0.492000021**<br>First: 1.566600055<br>Randomized: 0.641099876 | Middle: **1.183100045**<br>First: 4.288499942<br>Randomized: 1.521500060 |
| Reversed | Middle: **0.069599831**<br>First: 0.404499937<br>Randomized: 0.088399975 | Middle: **0.478300033**<br>First: 9.529100033<br>Randomized: 0.627200119 | Middle: **1.172099961**<br>First: 40.889600059<br>Randomized: 1.503899926 |
| Duplicates | Middle: 0.018100021<br>First: **0.015700003**<br>Randomized: 0.016399892 | Middle: 0.089500099<br>First: 0.093100127<br>Randomized: **0.076500000** | Middle: 0.203399919<br>First: 0.171900028<br>Randomized: **0.150099862** |

### 5.2 Discussion of Results

#### Why the Middle Pivot Does Well on Ordered Inputs

The middle-index version is the fastest on all sorted and reverse-sorted
cases in these results. The random arrays are made by choosing each value from
1 through the array length, so they may contain duplicates. The sorted and
reverse-sorted cases are ordered versions of the same values. With repeated
values, the value at the middle index is around the middle rank but need not
split the distinct values evenly. Even so, these results show that this pivot
works well for these ordered inputs, especially compared with selecting the
first value.

The middle pivot is not always the fastest on random-order data. First-pivot
is fastest on the 100- and 1,000-element random inputs, and middle-pivot is
fastest at 500. For 100 elements, first-pivot is also fastest for duplicates;
randomized Quicksort is fastest for duplicates at 500 and 1,000. These
differences are specific to this generated data and timing run, not a
guarantee that one method wins for every array of that size.

#### Why First-Pivot Quicksort Struggles

On a sorted array, the first value is the smallest; on a reverse-sorted array,
it is the largest. These are extreme pivot choices, so most of the remaining
distinct values fall on one side. The recursive calls can then repeatedly
process nearly the whole remaining array.

The reverse-sorted timings show this slowdown: first-pivot Quicksort takes
0.404499937 ms for 100 values, 9.529100033 ms for 500, and 40.889600059 ms
for 1,000. It completes these tests, but the growth is much steeper than for
the other implementations and is consistent with repeatedly unbalanced
partitions and the O(n²) worst case. The arrays can contain repeated values,
which the three-way partition groups together, so the exact recursion pattern
depends on both the extreme pivot values and the duplicates in the data.
Middle-index pivoting avoids much of this slowdown on these ordered inputs.

#### Why Randomized Quicksort Is Not Always the Fastest

Randomized Quicksort does extra work to choose a random pivot. On small or
already easy inputs, that overhead can take a noticeable share of the total
time. Also, a random pivot is not guaranteed to be the best pivot on a
particular call; it may produce a less balanced split than the middle-index
choice.

The benefit of randomization is not that every measured run must be the
fastest. Instead, it makes performance less dependent on how the input was
originally arranged. On average, it is less likely to keep selecting extreme
pivots, even when the input is sorted or reversed. This makes it a more
robust general-purpose strategy when the input order is unknown or could be
chosen to make a fixed pivot perform badly. In these results, randomized
Quicksort is not fastest on most random or ordered inputs, but it completes
all tested cases without the extreme slowdown seen for first-pivot on
reverse-sorted inputs. That makes this run behavior more consistent across
distributions. It is still not an absolute guarantee: an unlucky series of
random choices can produce O(n²) work or deep recursion.

#### What the Duplicate Results Show

All three algorithms use three-way partitioning, so values equal to the pivot
are grouped together and skipped by later recursive calls. This is especially
useful for the duplicate-heavy arrays, which are generated using only three
possible values. Randomized Quicksort is fastest on duplicate-heavy inputs at
500 and 1,000 elements, while first-pivot is fastest at 100. This suggests
the shared three-way partition handles many equal values efficiently, though
these timings do not establish a universal ranking.

#### Time and Space Complexity in the Standout Cases

The three versions have the same asymptotic bounds; changing the pivot rule
does not change Quicksort's theoretical best, average, or worst cases. It
changes how likely a particular input is to produce balanced partitions.
Partitioning itself takes O(n) time and O(1) extra space in all three
versions. Excluding the recursion stack, each sort is in-place and uses no
additional array proportional to the input size.

The clearest time-complexity outlier is first-pivot Quicksort on reversed
input. At 1,000 elements, it takes 40.889600059 ms, compared with 1.172099961
ms for middle-pivot and 1.503899926 ms for randomized Quicksort. This is
consistent with first-pivot repeatedly producing uneven partitions, which
can make its work approach O(n²). The timing alone does not prove the exact
partition sizes, but its steep increase relative to the other variants is
what the worst-case analysis predicts. The same unbalanced recursion can
require O(n) stack space; the other two variants' faster times on this input
are consistent with shallower, more balanced recursion and about O(log n)
stack space.

The ordered inputs are a contrasting case. On these arrays, middle-index
pivoting stays close to the best-case pattern: the selected value is around
the middle rank, so partitions are much more balanced. That gives O(n log n)
time and O(log n) recursion stack in this tested arrangement. First-pivot
Quicksort has the same O(n log n) best case in theory, but its choice is poor
for ordered arrays, so it does not realize that best case here.

The duplicate-heavy arrays contain only three possible values. With the
shared three-way partition, all values equal to a selected pivot are grouped
and removed from further recursion. Since there are at most three distinct
values, the sort needs only a small number of partition levels; the total
partition work is therefore close to linear in n for this data, rather than
the usual O(n log n) pattern. The reported duplicate times are correspondingly
low. At 500 and 1,000 elements, randomized Quicksort is fastest; at 100,
first-pivot is fastest. Those small differences reflect implementation
overhead and measurement variation more than a meaningful difference in
asymptotic complexity. For this bounded-key input, recursion depth is also
bounded by the number of distinct values, so stack use is small for all three
versions.

Randomized Quicksort has O(n log n) expected time and expected O(log n)
recursion depth, but still has O(n²) worst-case time and O(n) worst-case
stack use. Its advantage is that a fixed input order is less likely to
repeatedly force bad splits. Random-number generation adds a small constant
cost, which helps explain why it is not fastest on every case.

#### Interpreting Small Timing Differences

These arrays are small, and many measured runs take less than a millisecond.
At that scale, a small delay from the operating system, other running
programs, or the Python interpreter can noticeably affect the result. CPU
cache state may also contribute if arrays or code have been accessed before
timing, because recently used data or instructions may remain in cache. This
could affect a short run, but the measurements do not prove caching caused a
particular timing difference.

There is also an important distinction between printing an array and sorting
it for display. Quicksort changes its input in place. The optional
`TestSortingAlgorithms()` routine previously passed the benchmark's original
arrays to the sorting functions, so running that routine before the benchmark
could leave those inputs sorted. That changes what the later benchmark
measures and is a more direct explanation than cache effects alone. The
routine now sorts a copy, preserving the original test arrays. The benchmark
itself also prepares a fresh copy for each timed run, although this cannot
eliminate all cache or system effects.

The benchmark reports the minimum of 30 samples, which is useful for
seeing a relatively uninterrupted run but tends to make times look faster
than typical performance. For that reason, small differences—such as the
random-array results at 100 and 500 elements—should be interpreted
cautiously. The very large slowdown for first-pivot on reversed inputs is
more persuasive because it matches the algorithm's predicted worst-case
behavior.

## 6. Conclusion

The tests show that pivot selection affects both speed and reliability across
different input arrangements. The middle-index pivot is particularly
effective on the sorted and reverse-sorted arrays used here. First-pivot
Quicksort is fastest on the 1,000-element random input, but its performance
degrades sharply on reversed data: it takes 40.889600059 ms at 1,000 elements,
although it completes this run. Three-way partitioning helps all three
versions handle duplicates, and randomized Quicksort has the lowest measured
time on duplicate-heavy inputs at sizes 500 and 1,000.

Randomized Quicksort may not win the timing contest on every small test
because selecting random pivots has overhead. Its strength is that it is
less tied to one predictable input order and has O(n log n) expected time.
That makes it a robust choice when input order is unknown, though no
randomized run is guaranteed to avoid the worst case. Overall, these
measurements illustrate a general lesson: algorithm performance depends on
the input, the implementation, and how the benchmark is run.
