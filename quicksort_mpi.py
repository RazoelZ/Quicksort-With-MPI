# mpiexec -n 4 python .\quicksort_mpi.py 10

from mpi4py import MPI
import numpy as np
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


# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Generate random data
arr_size = int(sys.argv[1])
data = np.random.randint(0, 100, size=arr_size)

# Calculate time
start = MPI.Wtime()

# Split the data among the processes
local_data = np.array_split(data, size)[rank]

# Sort the local data
local_data = quicksort(local_data)

# Gather the sorted data back to the root process
sorted_data = comm.gather(local_data, root=0)
print("\n@================ Sorted Going ================@\n",
      [rank], local_data)

if rank == 0:
    # Flatten the list of arrays into a single array
    sorted_data = np.concatenate(sorted_data)

    # Final sort
    sorted_data = quicksort(sorted_data)
    print("\n@================ Random Array ================@\n", data)
    print("\n@================ Result ================@\n", sorted_data)
    print("\n@================= Time =================@\n",
          MPI.Wtime() - start, "\n")
