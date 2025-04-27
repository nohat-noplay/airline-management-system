# DoubleLinkedListClass.py
# 
# A custom implementation of a Doubly Linked List in Python, 
# supporting node insertion, deletion, traversal, and copying.
# 
# Built as part of a portfolio project simulating an airline management system.
# All data structures were developed from scratch for learning and demonstration purposes.
#
# Author: Saf Flatters
# Year: 2024



class DSAListNode():    #allows us to add and remove nodes at different positions

    def __init__(self):     #initially only one node with no next
        self.value = None
        self.next = None
        self.prev = None

    def getValue(self):     #returns value stored in node
        return self.value
    
    def getEdgename(self):
        return self.value[0]

    def setValue(self, inValue):    #sets a value of the node
        self.value = inValue

    def getNext(self):      #returns the node that the pointer is pointing to
        return self.next
    
    def setNext(self, newNext):     #sets the "next pointer" to point to the node "newNext"
        self.next = newNext

   
    def getPrev(self):      #returns node that 'previous' pointer is pointing to
        return self.prev
    
    def setPrev(self, newPrev):     #sets the "previous pointer" to point to the node "newPrev"
        self.prev = newPrev





class DoubleLinked():

    def __init__(self):
        self.head = None
        self.tail = None

#Mutators: Insert
#Four possible scenarios for node insertion: 
# (1) List empty and setting first node
# (2) Inserting before head node
# (3) Inserting after tail of the list
# (4) Inserting somewhere in the middle of list
        
# (1) else (2)
    def insertFirst(self, newValue):
        newND = DSAListNode()       #creates a new instance: a new node to be added
        newND.setValue(newValue)    #sets the new nodes value

        if self.isEmpty():          #if linked list empty: 
            self.head = newND       #direct head to point to this new node
            self.tail = newND       #DOUBLE

            # print("Set", self.head.getValue(), "to Head Node (It is the only Node)")
        
        else:                       #if not empty: 
            newND.setNext(self.head)    #set new nodes pointer to the current head
            self.head.setPrev(newND)    #DOUBLE
            self.head = newND           #Makes new node the new head

            # print("Set", self.head.getValue(), "to Head Node that points to the next node: ", self.head.getNext().getValue())
            # print("New Tail: ", self.tail.getValue())    #DOUBLE
# (3)
    def insertLast(self, newValue):
        newND = DSAListNode() 
        newND.setValue(newValue)

        if self.isEmpty():
            self.head = newND
            self.tail = newND   #DOUBLE

            # print("Set", self.head.getValue(), "to Head and Tail Node (It is the only Node)")

        else:                       #if list not empty: DOUBLE
            self.tail.setNext(newND)    #Find tail and set it's pointer to new Node
            newND.setPrev(self.tail)    #New node's prev pointer to point to tail
            self.tail = newND           #Set the new Node as the tail
            
            # print("Set", self.tail.getValue(), "as new Tail Node")

#Accessors  
    def isEmpty(self):
        if self.head == None:
            return True
        
    def peekFirst(self):
        try:
            if self.isEmpty():
                raise ValueError("Linked List is Empty")
        except ValueError as err:
            print("Invalid!", err)
        else: 
            nodeValue = self.head.getValue()
            # print("Head Node: ", nodeValue)
            return nodeValue
        
    def peekLast(self):
        try:
            if self.isEmpty():
                raise ValueError("Linked List is Empty")
        except ValueError as err:
            print("Invalid!", err)
        else: 
            nodeValue = self.tail.getValue()
            # print("Last Node: ", nodeValue)
            return nodeValue
        
    def previousNode(self, node):       #my own add on to access previous nodes
        try: 
            if node == self.head:
                raise ValueError("There is no Previous Node from the Head Node")
        except ValueError as err:
            print("Invalid!", err)
        else: 
            return node.getPrev()
        
    def previousNodePrint(self, node):
        prevnode = self.previousNode(node)
        if prevnode != None:
            print(prevnode.getValue())
        
#Mutators: remove
    def removeFirst(self):
        try:
            if self.isEmpty():
                raise ValueError("Linked List is Empty")
        except ValueError as err:
            print("Invalid!", err)
        else: 
            nodeValue = self.head.getValue()    #set head value to variable nodeValue

            if self.head.getNext() is not None: #if there is more than one Node 
                self.head = self.head.getNext()     #set the node head points to as the new head
                self.head.setPrev(None)             #DOUBLE - sets previous pointer of new head to none
            else:                               #if this is the last node:
                self.head = None                #set head and tail back to not point at anything
                self.tail = None

            # print("Removed: ", nodeValue)
            return nodeValue

    def removeLast(self):                       
        try:
            if self.isEmpty():
                raise ValueError("Linked List is Empty")
        except ValueError as err:
            print("Invalid!", err)
        
        else: 
            if self.head.getNext() == None:       #if the head value is the only item, remove head
                nodeValue = self.head.getValue()    
                self.head = None
                self.tail = None        #DOUBLE
                # print("Removed: ", nodeValue)
            else: 
                nodeValue = self.tail.getValue()
                prevND = self.previousNode(self.tail)   #easily access using PreviousNode Function 
                self.tail = prevND

                self.tail.setNext(None)              #set tail to last node to point to none

                # print("Removed: ", nodeValue)

    def returnHead(self):
        return self.head
    
    def printit(self):
        try: 
            if self.isEmpty() == True: 
                raise ValueError("Linked List is Empty")
        except ValueError as err:
                print("Invalid!", err)
        else: 
            checknode = self.head
            output = ""
            while checknode != None: 
                output += str(checknode.getValue()) + " "
                checknode = checknode.getNext()
            return output
        
    def LLcopy(self):
        newlist = DoubleLinked()
        current = self.head
        while current:
            newlist.insertLast(current.getValue())
            current = current.getNext()
        return newlist
    
    def deleteNode(self, node):
        current = self.head
    # Find node
        while current is not None:
            if current.getValue() == node:
                # if node == self.head
                if current == self.head:
                    self.head = current.getNext()
                    if current.getNext() is not None:
                        current.getNext().setPrev(None)
                    else:
                        self.tail = None  # If the list had only one node

                # If node = tail
                elif current == self.tail:
                    self.tail = current.getPrev()
                    current.getPrev().setNext(None)
                else:
                    current.getPrev().setNext(current.getNext())
                    current.getNext().setPrev(current.getPrev())
                return
            current = current.getNext()


        # If node doesn't exist:
        print("Node with value", node, "not found.")

    def deleteEdgeNode(self, node):
        current = self.head
    # Find node
        while current is not None:
            if current.getEdgename() == node:
                # if node == self.head
                if current == self.head:
                    self.head = current.getNext()
                    if current.getNext() is not None:
                        current.getNext().setPrev(None)
                    else:
                        self.tail = None  # If the list had only one node

                # If node = tail
                elif current == self.tail:
                    self.tail = current.getPrev()
                    current.getPrev().setNext(None)
                else:
                    current.getPrev().setNext(current.getNext())
                    current.getNext().setPrev(current.getPrev())
                return
            current = current.getNext()


        # If node doesn't exist:
        print("Node with value", node, "not found.")
    
    def getCount(self):
        count = 0
        try: 
            if self.isEmpty() == True: 
                raise ValueError("Linked List is Empty")
        except ValueError as err:
                print("Invalid!", err)
        else: 
            checknode = self.head
            while checknode != None: 
                count +=1
                checknode = checknode.getNext()
            return count