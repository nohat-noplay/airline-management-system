# QueueClass.py
#
# Custom implementation of a basic queue and circular queue in Python, using a doubly linked list backend.
# Supports:
# - Standard queue operations (enqueue, dequeue, peek)
# - Circular queue behavior with refresh functionality
#
# Author: Saf Flatters
# Year: 2024

from DoubleLinkedListClass import *

# Queue Class: 
# Parent Class (everything except deQueue)

class DSAQueue(): 


    #Constructor
    def __init__(self):
        self.queuearray = DoubleLinked()
        self.front = 0 
        self.rear = 0 

    #Accessors
        
    def getCount(self):
        return self.rear - self.front

    def isEmpty(self):
        return self.queuearray.isEmpty()

    
    def Peek(self): 
        return self.queuearray.peekFirst()
        
        
    def printit(self):
        try: 
            if self.queuearray.isEmpty() == True: 
                raise ValueError("Linked List is Empty")
        except ValueError as err:
                print("Invalid!", err)
        else: 
            checknode = self.queuearray.head
            while checknode != None: 
                print(checknode.getValue())
                checknode = checknode.getNext()


    #Mutators
    def enQueue(self, value): #just add it to tbe end of the queue
        self.queuearray.insertLast(value)
        self.rear += 1



#Circular Queue child class
            
class CircularQueue(DSAQueue):   #Child class

    def __init__(self):
        super().__init__()

    def deQueue(self): 
        peek = self.queuearray.peekFirst()
        self.queuearray.removeFirst()
        self.front += 1
        return peek
    
    def refresh(self):
        self.front = 0