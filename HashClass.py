# HashClass.py
#
# Custom implementation of an open-addressing hash table in Python, using double hashing for collision resolution.
# Supports:
# - Insert, search, delete, and dynamic resizing based on load factor thresholds
# - Exporting hash table contents to CSV
# - Tracking performance metrics like duplicate entries and maximum collision attempts
#
# Author: Saf Flatters
# Year: 2024

import math as math
import numpy as np

   
class DSAHashEntry():

    def __init__(self, inKey, inValue, hashindex, state):

            self.inKey = inKey
            self.inValue = inValue
            self.state = state
            self.index = hashindex

    def getKey(self):
        return self.inKey

    def getValue(self): 
        return self.inValue
    
    def getIndex(self):
        return self.index
    
    def getState(self):
        return self.state

    def removeKey(self):
            self.inKey = ""
            self.inValue = None
            self.state = -1      # 0 = neverused, 1 = used, -1 = formerly-used
            self.index = self.index



class DSAHashTable():      

    def __init__(self, tablesize):

        self.actualsize = self._nextPrime(tablesize)    #round up to a prime number - important for Double Hashing
        self.hashArray = np.empty(self.actualsize, dtype=object)      #make an array (table)
        self.count = 0                                  #number of entries
        self.duplicatecount = 0
        
        self.entryhashmax = 0       #entry with the largest amount of hashes - help with Big(O) of hash functions

        for i in range(self.actualsize):
            self.hashArray[i] = DSAHashEntry("", None, i, 0)


    def put(self, inKey, inValue):

        duplicate = False
        self.entryhashes = 0        #updates each entry input with that entries hash amount
        trytime = 0
        hashindex = self._hash(inKey)                                      #find where to put entry (sum of ascii % table size)
        # print(inKey, "Hash Index = ", hashindex, "    from Hash Function: Ascii sum: ", sum(ord(char) for char in inKey), " % Hash Table size: ", self.actualsize)   #list comprehension taken from forum - only for presentation purposes   
        

        while self.hashArray[hashindex].getState() == 1 and not duplicate:                             #if there is already an entry at that location
            if self.hashArray[hashindex].getKey() != inKey:     #if this is not a duplicate
                trytime += 1
                hashindex = self._stepHash(inKey, trytime)                              #hashindex + stepsize 
                # print(trytime, "Double Hash Function: ASCII of last char * try:", (ord(inKey[-1]) * trytime) , " % Hash Table size:", self.actualsize, "=", hashindex)
            
            else: 
                print("Duplicate Entry", inKey, "not completed")
                self.duplicatecount +=1
                duplicate = True


        # EXIT WHILE: if no entry at that/new location and not a duplicate
        if not duplicate:
            self.hashArray[hashindex] = DSAHashEntry(inKey, inValue, hashindex, 1)       # put new hash entry at that location
            self.count += 1
            self.entryhashes = trytime + 1      #amount of double hashes + first hash

            print("Inputted", inKey, "and", inValue, "into final hash index:", hashindex, "- Load Factor", self.getLoadFactor(), "\n")

            if self.getLoadFactor() > 0.75:      #stops filling up hashtable over 75% resulting in more collisions
                self._resize("1")

            if self.entryhashes > self.entryhashmax:        #keep track of entry with the largest amount of hashes - help with Big(O) of hash functions
                self.entryhashmax = self.entryhashes


    def get(self, searchKey): 
        trytime = 0
        hashindex = self._hash(searchKey)                                      #where to look for searched entry (sum of ascii % table size) (WHY +1?)
        # print(searchKey, "Hash Index = ", hashindex, "    from Hash Function: Ascii sum: ", sum(ord(char) for char in searchKey), " % Hash Table size: ", self.actualsize)
        
        while self.hashArray[hashindex].getState() != 0:                #check if the index exists
            if self.hashArray[hashindex].getState() == 1:                   #if there is an entry at that location

                if self.hashArray[hashindex].getKey() == searchKey:              #check if entry key is searched key
                    # print(searchKey, "found!", self.hashArray[hashindex].getKey(), ":" ,self.hashArray[hashindex].getValue(), "at Index:", self.hashArray[hashindex].getIndex())
                    print(self.hashArray[hashindex].getKey(), ":" ,self.hashArray[hashindex].getValue()) #FOR ASSIGNMENT

                    return self.hashArray[hashindex].getIndex()
                
                else: 
                    trytime += 1
                    hashindex = self._stepHash(searchKey, trytime)                             #hashindex + stepsize
                    # print("double hash get", hashindex)                                                                 #if it is not - update location with _stephash (hashindex + stepsize) 
           
            elif self.hashArray[hashindex].getState() == -1:                #if entry was at location but has been deleted
                # print("old location")
                trytime += 1
                hashindex = self._stepHash(searchKey, trytime)     #not at location but could still exist - update location with _stephash (hashindex + stepsize)


        # EXIT WHILE: if hashindex is none
        print(searchKey, "does not exist")

        return None


    def remove(self, itemtodelete):
        
        try:
            if self.get(itemtodelete) == None:
                raise ValueError("HashTabled item does not exist")
        except ValueError as err:
                print("\nInvalid!", err)
        else:
            rmindex = self.get(itemtodelete)
            print(rmindex)
            self.hashArray[rmindex].removeKey()
            self.count -= 1
            print("Removed", itemtodelete, "at Index:", rmindex)

            if self.getLoadFactor() < 0.25:      #stops table from being too big (75% wasted space)
                self._resize("0")


    def getLoadFactor(self):        #determine how full a hashtable is

        loadfactor = self.count / self.actualsize
        # print("Load Factor", loadfactor, "\n")
        return loadfactor           #upperbound = 0.7, lowerbound = 0.3
    

    def export(self):
        with open('hashout.csv', 'w') as hashoutput:
            for item in self.hashArray:
                if item is not None and item.getState() == 1: 
                    hashoutput.write(f"{item.getIndex()},{item.getKey()},{item.getValue()}")
        print("Exported to hashout.csv")


    def _resize(self, size):    #if size is 1, increase. if size is 0, decrease. 

        print("RESIZE REQUIRED! Current Load Factor", self.getLoadFactor(), "\n")
        previous = self.actualsize
        previousLF = self.getLoadFactor()
        oldcount = self.count

        if size == "1":   #increase by 30%
            increase = int(self.actualsize * 1.3) #round up to integer
            tempnew = DSAHashTable(increase)

            for i in self.hashArray:
                if i.getState() == 1:
                    tempnew.put(i.getKey(), i.getValue())

            self.actualsize = tempnew.actualsize
            self.hashArray = tempnew.hashArray

        elif size == "0": #decrease by 30%
            decrease = int(self.actualsize * 0.7) #round up to integer
            tempnew = DSAHashTable(decrease)

            for i in self.hashArray:
                if i.getState() == 1:
                    tempnew.put(i.getKey(), i.getValue())
                    # print(i.getIndex(), i.getKey(), i.getValue()) 
                     
            self.actualsize = tempnew.actualsize
            self.hashArray = tempnew.hashArray

        # self.printHashTable()
        print("Previous table size:", previous, "- with", oldcount, "entries & Previous Load Factor", previousLF)
        print("New table size:", self.actualsize, "- with", self.count, "entries & New Load Factor:", self.getLoadFactor())



    def _hash(self, inKey):

        hashindex = 0
        for char in inKey:
            hashindex += ord(char)

        #my hash function is the sum of ascii worth of all characters % size of hash table
        goodhashy = hashindex % self.actualsize   # find a the modulus of table length (an round up to prime)    

        return goodhashy


    def _stepHash(self, inKey, trytime):          #double hashing - secondary hash function when collision

        #My double hash function is the ascii worth of the final character * amount of double hashes % size of hash table
        doublehashy = (((ord(inKey[-1])) * trytime)) % self.actualsize 

        return doublehashy


    def _nextPrime(self, startVal):     #PROPERTY 1

        if startVal % 2 == 0:           #prime numbers are never even
            primeVal = startVal -1      #-1 ensures it's odd
        else: 
            primeVal = startVal         #its already odd

        #test if isPrime is a Prime number
        isPrime = False

        while not isPrime:
            primeVal += 2
            ii = 3
            isPrime = True                                           #issue with math.sqrt on school computers. Tutor advised to use **(0.5)
            rootVal = int(primeVal**(0.5))              #https://www.w3schools.com/python/ref_math_sqrt.asp#:~:text=The%20math.sqrt()%20method,than%20or%20equal%20to%200.

            while ii <= rootVal and isPrime:
                if primeVal % ii == 0:
                    isPrime = False
                else: 
                    ii += 2

        return primeVal
    
    
    def printHashTable(self): #to check how spaced out it is

        for i in self.hashArray:
            if i is not None and i.getState() == 1: 

                print(i.getIndex(), ":", i.getKey(), i.getValue())

            elif i.getState() == -1:
                print(i.getIndex(), ": FREE BUT FORMALLY USED")

            else:   
                print(i.getIndex(), ":", i.getKey(), i.getValue())      #prints index : None

        print("Number of Entries", self.count)
        print("Load Factor", self.getLoadFactor())
        print("Duplicate Entry Attempts:", self.duplicatecount)
        print("Maximum Double Hashes of an entry:", self.entryhashmax)













