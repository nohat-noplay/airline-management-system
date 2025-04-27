# DSASorts.py
#
# Custom implementations of Merge Sort, Quick Sort, and Heap Sort algorithms in Python.
# Designed for performance testing on large datasets, including handling of recursion limits for Quick Sort.
#
# Author: Saf Flatters
# Year: 2024


import numpy as np


########################    MERGE SORT    ######################################################################


def mergeSort(array):
    if len(array) < 2:          #base case if array is 1 or less
        return array
    
    # if len(array) >= 2:          #if array is greater or equal to 2
    mid = len(array) // 2       #find middle
    left = np.array(array[:mid])          #left is 0 to middle      #this needs to be an array!! not a list!
    right = np.array(array[mid:])        #right is middle to end    #this needs to be an array!! not a list!
                                                                    #send array to inplace

    mergeSort(left)
    mergeSort(right)
    merge(array, left, right)     #recursively sort both halves and return result of merge 

    return array                


def merge(result, leftside, rightside):                                 #result is original array, so it updates the OG rather than a new one
    left = 0            #index pointer for left array
    right = 0           #index pointer for right array  
    pointer = 0         #index pointer for result array

    while left < len(leftside) and right < len(rightside):      #merge elements until both sides are complete
        if leftside[left] <= rightside[right]:                  #compare sides - if left is smaller
            result[pointer] = leftside[left]                    #put it into results
            left += 1                                           
        else:
            result[pointer] = rightside[right]                  #if right is smaller, put right into results
            right += 1
        pointer += 1

    #for larger element remaining on the left
    while left < len(leftside):                 
        result[pointer] = leftside[left]
        left += 1
        pointer += 1        

    #for larger element remaining on the right
    while right < len(rightside):
        result[pointer] = rightside[right]
        right += 1
        pointer += 1

    # return result



    
########################    QUICK SORT    ######################################################################
def pivot(array, leftIdx, rightIdx):       #choose median element out of 3 elements for it's index to be pivot
    midIdx = (leftIdx + rightIdx) // 2
    leftelement = array[leftIdx]           
    rightelement = array[rightIdx]
    midelement = array[midIdx]

    if leftelement <= midelement <= rightelement or rightelement <= midelement <= leftelement:
        return midIdx
    
    elif midelement <= leftelement <= rightelement or rightelement <= leftelement <= midelement:
        return leftIdx
    
    else:
        return rightIdx
    
def quickSort(array):               #wrapper
    # print(f"Starting quickSort: {array}")       ###
    quickSortRecurse(array, 0, len(array)-1)
    # print(f"Ending quickSort: {array}")         ###
    return array        #returns sorted array


def quickSortRecurse(array, leftIdx, rightIdx):     
    if rightIdx > leftIdx:
        pivotIdx = pivot(array, leftIdx, rightIdx)          #find best pivot (out of 3 elements)
        # print(f"Pivot selected: {array[pivotIdx]} at index {pivotIdx}")
        newpivotIdx = doPartitioning(array, leftIdx, rightIdx, pivotIdx)    
        # print(f"Array after partitioning: {array}")
        quickSortRecurse(array, leftIdx, newpivotIdx-1)     #recurse left partition
        quickSortRecurse(array, newpivotIdx+1, rightIdx)    #recurse right partition


def doPartitioning(array, leftIdx, rightIdx, pivotIdx):
    pivotVal = array[pivotIdx]                  #pivot value/element
    array[pivotIdx] = array[rightIdx]           #swap the pivotVal with right-most element
    array[rightIdx] = pivotVal

    currIdx = leftIdx                           #pointer

    for ii in range(leftIdx, rightIdx):         #iterate from left to right 
        if array[ii] < pivotVal:                # if element is less than pivot element, swap element with currentIdx element
            temp = array[ii]
            array[ii] = array[currIdx]
            array[currIdx] = temp
            currIdx = currIdx + 1

    newPivIdx = currIdx                        # index of where the pivot should be placed now
    array[rightIdx] = array[newPivIdx]          #swap pivot back to correct position
    array[newPivIdx] = pivotVal

    return newPivIdx                            #return index of pivot after partitioning

########################    HEAP SORT    ######################################################################

def heapSort(heapArray):
    numItems = len(heapArray)
    heapify(heapArray)          #heapify the array - complete sorted heap

    for ii in range(numItems-1,  0, -1):     #range(count - 1 (last item), stop: 0, backwards) 
        heapArray[0], heapArray[ii] = heapArray[ii], heapArray[0]  # swap root (always max) with last element
        trickledown(0, ii, heapArray)             #trickledown new root using new count (so it doesn't delete sorted back of array)

    return heapArray


def heapify(heapArray):   #swaps unsorted array (unsorted tree) into a sorted MAX heap using same array - inPlace
    numItems = len(heapArray)
    for i in range(int(numItems / 2) - 1, -1, -1):       # starts last non-leaf node (floor div count/2) and goes backwards (stopping before root)
        trickledown(i, numItems, heapArray)  #complete trickle down for every sub root 
        #  self.trickleup(i)


def trickledown(currIdx, numItems, heapArray):           
    LchildIdx = currIdx * 2 + 1
    RchildIdx = LchildIdx + 1

    if LchildIdx < numItems:        #ensures Lchild is within bounds of array
        largeIdx = LchildIdx        #left child is largest child (for now)

        if RchildIdx < numItems:        #ensures Rchild is within bounds of array
                if heapArray[LchildIdx] < heapArray[RchildIdx]:    #WHo is larger? LChild or Rchild?
                    largeIdx = RchildIdx    
        
        if heapArray[largeIdx] > heapArray[currIdx]:  #if selected child is bigger than current item
                temp = heapArray[currIdx]        #copy current item 
                heapArray[currIdx] = heapArray[largeIdx] #make current index now selected child 
                heapArray[largeIdx] = temp      #make old child item index now current item
                trickledown(largeIdx, numItems, heapArray)           #current Item to be trickled down (and currently in old child index)
