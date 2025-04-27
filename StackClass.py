# StackClass.py
#
# Custom implementation of a stack (LIFO) in Python, using a doubly linked list backend.
# Supports:
# - Standard stack operations (push, pop, top, isEmpty)
# - Dynamic resizing through linked list structure
#
# Author: Saf Flatters
# Year: 2024

from DoubleLinkedListClass import *

# Stack Class - LIFO, Last In First Out - built using Pseudocode on Lecture Slides

class DSAStack: 

    
    #Constructor
    def __init__(self):
        self.stackarray = DoubleLinked()
        self.count = 0

    #Accessors
        
    def getCount(self):
        return self.count

    def isEmpty(self):
        return self.stackarray.isEmpty()


    def top(self):
        return self.stackarray.peekFirst()
        
    def printit(self):
        try: 
            if self.stackarray.isEmpty() == True: 
                raise ValueError("Linked List is Empty")
        except ValueError as err:
                print("Invalid!", err)
        else: 
            checknode = self.stackarray.head
            while checknode != None: 
                print(checknode.getValue())
                checknode = checknode.getNext()


    #Mutators

    def push(self, value):
        self.stackarray.insertFirst(value)
        self.count += 1

    def pop(self):
        popped = self.stackarray.peekFirst()
        self.stackarray.removeFirst()
        if self.count != 0:
            self.count -= 1
        return popped
