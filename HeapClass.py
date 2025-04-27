# HeapClass.py
#
# Custom implementation of a min-heap in Python, supporting:
# - Heap insertion, removal, and dynamic resizing
# - Heap sort for organizing flight routes by layovers or distance
# - Exporting sorted heap contents to CSV
#
# Author: Saf Flatters
# Year: 2024

import numpy as np 


class DSAHeapEntry():
    #Priority, Value, 

    def __init__ (self, inPriority, inValue):
        self._priority = inPriority
        self._value = inValue

    def getPriority(self):
        return self._priority
    
    def setPriority(self, inPriority):
         self._priority = inPriority

    def getValue(self):
        return self._value
    
    def setValue(self, inValue):
         self._value = inValue

    def __str__ (self):
        print("Priority:",self._priority," Value:", self._value)

    def __sortstr__(self):
        print("Key: ",self._priority," Value:", self._value)
    

class DSAHeap():
     
    def __init__ (self, OGsize):
        self.heapArray = np.empty(OGsize, dtype=object)         #need size of array in initialisation
        self.count = 0

###Not Required for HeapSort
        self.sorted = np.empty(OGsize, dtype=object)
        self.sortedcount = 0

##REQUIRED
    def add(self, inPriority, inValue):
        self.heapArray[self.count] = DSAHeapEntry(int(inPriority), inValue)  #add to end of array
        self.count +=1

        currIdx = int(self.count -1)        # NEW ITEM:  count minus 1 because count included root

        #THIS NEEDS TO BE COMMENTED OUT IF USING HEAPIFY
        # self.trickleup(currIdx)

###Not Required for HeapSort
    def trickleup(self, currIdx):       #recursive 
        parentIdx = int((currIdx-1)/2)       # Item above is parent

        if currIdx > 0:                 #if not root
            if self.heapArray[currIdx].getPriority() > self.heapArray[parentIdx].getPriority():     #if NEW item key is greater than parent key
                temp = self.heapArray[parentIdx]        #copy parent item 
                self.heapArray[parentIdx] = self.heapArray[currIdx] #make parent index now NEW item 
                self.heapArray[currIdx] = temp      #make old new item index now parent item
                self.trickleup(parentIdx)           #new Item to be trickled up (and currently in old Parent index)

###Not Required for HeapSort
    def remove(self):       
        # print("count:", self.count)
        self.sorted[self.sortedcount] = self.heapArray[0]            #take a copy of root node (and store it in sorted array)
        self.sortedcount +=1

        self.heapArray[0] = self.heapArray[self.count-1]                       #make last item in heap the root item
        # print(self.heapArray[0].getPriority(), "becomes root")
        
        self.heapArray[self.count -1] = None                                       #make last item of array - None
        self.count -= 1
        # self.printHeap()
        self.trickledown(0, self.count)

###REQUIRED
    def trickledown(self, currIdx, numItems):           
        LchildIdx = currIdx * 2 + 1
        RchildIdx = LchildIdx + 1

        if LchildIdx < numItems:        #ensures Lchild is within bounds of array
            largeIdx = LchildIdx        #left child is largest child (for now)

            if RchildIdx < numItems:        #ensures Rchild is within bounds of array
                    if self.heapArray[LchildIdx].getPriority() < self.heapArray[RchildIdx].getPriority():    #WHo is larger? LChild or Rchild?
                        largeIdx = RchildIdx    
            
            if self.heapArray[largeIdx].getPriority() > self.heapArray[currIdx].getPriority():  #if selected child is bigger than current item
                    temp = self.heapArray[currIdx]        #copy current item 
                    self.heapArray[currIdx] = self.heapArray[largeIdx] #make current index now selected child 
                    self.heapArray[largeIdx] = temp      #make old child item index now current item
                    self.trickledown(largeIdx, numItems)           #current Item to be trickled down (and currently in old child index)

###REQUIRED
    def printHeap(self):
        print("Heap:")
        for entry in self.heapArray:
            if entry is not None:
                entry.__str__()

###Not Required for HeapSort
    def printSort(self):
        print("\nSorted:")
        for entry in self.sorted:
            if entry is not None:
                entry.__sortstr__()

##REQUIRED
    def export(self):
        count = 1
        with open('heaproutes.csv', 'w') as heapoutput:
            for entry in self.heapArray:
                if entry is not None:
                            
                    heapoutput.write(f"{count},{entry.getPriority()},{entry.getValue()},\n")  #sorted number, amount of layovers/distance, flightroute
                    count +=1

        # print("Exported to heapout.csv")
              

#################### HEAPSORT QUESTION 2 ##########################3
    # Heapify - sorts within it's own array (unsorted tree) by sorting second last level and up, 
                # by putting each item (non-leaf) into root and then trickling down


    def heapify(self):   #swaps unsorted array (unsorted tree) into a sorted MAX heap using same array - inPlace
        numItems = self.count
        for i in range(int(numItems / 2) - 1, -1, -1):       # starts last non-leaf node (floor div count/2) and goes backwards (stopping before root)
             self.trickledown(i, numItems)  #complete trickle down for every sub root 
            #  self.trickleup(i)


    # HeapSort - results in a sorted array (min to max)
    # 1. Call heapify
    # 2. Swaps root with last item, changes number items to one less (so it doesnt include new end item)
    # 3. New root to be sorted via trickledown - making new new root the new maximum 
    
    def heapSort(self):
        numItems = self.count
        self.heapify()          #heapify the array - complete sorted heap

        for ii in range(numItems-1,  0, -1):     #range(count - 1 (last item), stop: 0, backwards) 
            self.heapArray[0], self.heapArray[ii] = self.heapArray[ii], self.heapArray[0]  # swap root (always max) with last element
            self.trickledown(0, ii)             #trickledown new root using new count (so it doesn't delete sorted back of array)
