# SortsTest.py
#
# Python script to benchmark Merge Sort, Quick Sort, and Heap Sort algorithms
# on randomly generated distance and layover datasets for airline route data.
# Results are used to analyze algorithm performance across varying input sizes.
# This is an edited version of Maxville & Richards Python Code 2017, 2018 - Curtin Uni
#
# Author: Saf Flatters
# Year: 2024




#** Testharness to generate various different types of arrays of integers
#** and then sort them using various sorts.
#**
#** Each sort is run REPEATS times, with the first result discarded,
#** and the last REPEATS-1 runs averaged to give the running time.


import numpy as np
import sys
import timeit
import DSAsorts



REPEATS = 3           #No times to run sorts to get mean time
NEARLY_PERCENT = 0.10 #% of items to move in nearly sorted array
RANDOM_TIMES = 100    #No times to randomly swap elements in array


def doSort(n, sortType, arrayType):
        # A = np.arange(1, n+1, 1)   #create array with values from 1 to n
        
        if arrayType == 'd':
            A = np.random.randint(1, 10000, n)   #create array with values from 1 to n
            # print("Random distances: ", A)

        elif arrayType == "l":
            A = np.random.randint(1, 11, n)   #create array with values from 1 to 10
            # print("Random layovers: ", A)        

        else:
            print("Unsupported array type")

        if sortType == "m":
            DSAsorts.mergeSort(A)
        elif sortType == "q":
            DSAsorts.quickSort(A)
        elif sortType == "h":
            DSAsorts.heapSort(A)
        else:
            print("Unsupported sort algorithm")

        for i in range(n-2):
            if (A[i] > A[i+1]):
                raise ValueError("Array not in order")

#main program

if len(sys.argv) < 3:
    ...
else:
    for aa in range(2, len(sys.argv)):
        
        n = int(sys.argv[1])
        sortType = sys.argv[aa][0]
        arrayType = sys.argv[aa][1]

        runningTotal = 0

        for repeat in range(REPEATS):
             startTime = timeit.default_timer()
             doSort(n, sortType, arrayType)
             endTime = timeit.default_timer()

             runningTotal += (endTime - startTime)
    
        print(sortType + arrayType + " " + str(n) + " " + str(runningTotal/(REPEATS - 1)))
