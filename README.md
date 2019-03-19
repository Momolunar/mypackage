# RecSort

RecSort is a python library package that contains the following functions:
  sum_array
  reverse
  fibonacci
  factorial
  bubble_sort
  merge_sort
  quick_sort

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mypackage.
```bash
pip install --upgrade git+https://github.com/momolunar/mypackage.git
pip install --upgrade git+https://github.com/momolunar/mypackage.git #to install a later version
```

## Usage
```python
from recsort.recursion import sum_array, fibonacci, factorial, reverse
from recsort.sorting import bubble_sort, merge_sort, quick_sort

merge_sort([10, 100, 5, 12, 55]) # returns [5, 10, 12, 55, 100]
factorial(5) # returns 120
fibonacci(14) # returns 377
