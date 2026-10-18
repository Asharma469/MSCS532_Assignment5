# Analysis Report

## Results for 100 Elements
| Distribution | Middle-Pivot | First-Pivot | Randomized |
|---|---:|---:|---:|
| Random | 0.000147100 | 0.000146200 | 0.000118800 |
| Sorted | 0.000089600 | 0.000179800 | 0.000118700 |
| Reverse | 0.000087300 | 0.000562800 | 0.000119700 |

## Results for 500 Elements
| Distribution | Middle-Pivot | First-Pivot | Randomized |
|---|---:|---:|---:|
| Random | 0.000695800 | 0.000882000 | 0.000899200 |
| Sorted | 0.000583200 | 0.001707200 | 0.000832500 |
| Reverse | 0.000557100 | 0.015800800 | 0.000789300 |

## Results for 1,000 Elements
| Distribution | Middle-Pivot | First-Pivot | Randomized |
|---|---:|---:|---:|
| Random | 0.001513800 | 0.001713400 | 0.001911700 |
| Sorted | 0.001357900 | 0.004702700 | 0.001901800 |
| Reverse | 0.001326900 | RecursionError | 0.001719500 |

> Note: On the 1,000-element reverse-sorted input, first-pivot Quicksort exceeded Python's recursion limit and raised `RecursionError`.

Each cell lists middle-pivot, first-pivot, and randomized Quicksort timings in seconds.

| Distribution | 100 elements | 500 elements | 1,000 elements |
|---|---|---|---|
| Random | Middle: 0.000147100<br>First: 0.000146200<br>Randomized: **0.000118800** | Middle: **0.000695800**<br>First: 0.000882000<br>Randomized: 0.000899200 | Middle: **0.001513800**<br>First: 0.001713400<br>Randomized: 0.001911700 |
| Sorted | Middle: **0.000089600**<br>First: 0.000179800<br>Randomized: 0.000118700 | Middle: **0.000583200**<br>First: 0.001707200<br>Randomized: 0.000832500 | Middle: **0.001357900**<br>First: 0.004702700<br>Randomized: 0.001901800 |
| Reverse | Middle: **0.000087300**<br>First: 0.000562800<br>Randomized: 0.000119700 | Middle: **0.000557100**<br>First: 0.015800800<br>Randomized: 0.000789300 | Middle: **0.001326900**<br>First: RecursionError<br>Randomized: 0.001719500 |

