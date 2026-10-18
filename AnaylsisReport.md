# Analysis Report

## Results for 100 Elements
| Distribution | Middle-Pivot (ms) | First-Pivot (ms) | Randomized (ms) |
|---|---:|---:|---:|
| Random | 0.147100 | 0.146200 | 0.118800 |
| Sorted | 0.089600 | 0.179800 | 0.118700 |
| Reverse | 0.087300 | 0.562800 | 0.119700 |

## Results for 500 Elements
| Distribution | Middle-Pivot (ms) | First-Pivot (ms) | Randomized (ms) |
|---|---:|---:|---:|
| Random | 0.695800 | 0.882000 | 0.899200 |
| Sorted | 0.583200 | 1.707200 | 0.832500 |
| Reverse | 0.557100 | 15.800800 | 0.789300 |

## Results for 1,000 Elements
| Distribution | Middle-Pivot (ms) | First-Pivot (ms) | Randomized (ms) |
|---|---:|---:|---:|
| Random | 1.513800 | 1.713400 | 1.911700 |
| Sorted | 1.357900 | 4.702700 | 1.901800 |
| Reverse | 1.326900 | RecursionError | 1.719500 |

> Note: On the 1,000-element reverse-sorted input, first-pivot Quicksort exceeded Python's recursion limit and raised `RecursionError`.

Each cell lists middle-pivot, first-pivot, and randomized Quicksort timings in milliseconds.

| Distribution | 100 elements | 500 elements | 1,000 elements |
|---|---|---|---|
| Random | Middle: 0.147100<br>First: 0.146200<br>Randomized: **0.118800** | Middle: **0.695800**<br>First: 0.882000<br>Randomized: 0.899200 | Middle: **1.513800**<br>First: 1.713400<br>Randomized: 1.911700 |
| Sorted | Middle: **0.089600**<br>First: 0.179800<br>Randomized: 0.118700 | Middle: **0.583200**<br>First: 1.707200<br>Randomized: 0.832500 | Middle: **1.357900**<br>First: 4.702700<br>Randomized: 1.901800 |
| Reverse | Middle: **0.087300**<br>First: 0.562800<br>Randomized: 0.119700 | Middle: **0.557100**<br>First: 15.800800<br>Randomized: 0.789300 | Middle: **1.326900**<br>First: RecursionError<br>Randomized: 1.719500 |
