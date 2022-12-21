# python .\quicksort_cpu.py 10

import numpy as np
import time
import sys

np.random.seed(1234)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Test the quicksort function
arr_size = int(sys.argv[1])
arr = np.random.randint(0, 100, size=arr_size)

start = time.time()
sorted_arr = quicksort(arr)
end = time.time()

print("\n@================ Random Array ================@\n", arr)
print("\n@================ Result ================@\n", sorted_arr)
print("\n@================= Time =================@\n", end - start, "\n")
