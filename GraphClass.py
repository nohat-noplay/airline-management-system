# GraphClass.py
#
# Custom implementation of a Graph data structure in Python, using doubly linked lists for adjacency storage.
# Supports:
# - Adding and deleting vertices and edges
# - Adjacency list and adjacency matrix displays
# - Breadth-First Search (BFS) with maximum layover and maximum distance filtering
# - Depth-First Search (DFS)
# - Exporting viable routes to CSV for further analysis
#
# Author: Saf Flatters
# Year: 2024

import numpy as np

from DoubleLinkedListClass import *
from QueueClass import *
from StackClass import *
from HashClass import *

class DSAGraphVertex():

    def __init__(self, label, value=None):
        self.label = label
        self.value = value
        self.edgelist = None
        self.visited = False

        if self.edgelist is None:
            self.edgelist = DoubleLinked()
        
        print("Adding", label, "as a Vertex to Graph")

    def getLabel(self):
        return self.label
    
    # def getValue(self):
    #     return self.value

    def getAdjacent(self):
        return self.edgelist.printit()      #might need to display list function
    
    def addVEdge(self, neighbour, weight):
        print("Adding Flight Path between", self.label, "and", neighbour, ": ", weight, "km")    
        self.edgelist.insertLast((neighbour, weight))

    def delVEdge(self, label):
        self.edgelist.deleteEdgeNode(label)      #make it a label for LL (not a tuple)

    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False
    
    def getVisited(self):
        return self.visited
    


class DSAGraph():
    vcount = 0
    ecount = 0

    def __init__(self, bothdirections):
        self.graphLL = None
        self.bothdirections = bothdirections


    def addVertex(self, label):
        if self.graphLL is None:
            self.graphLL = DoubleLinked()
        try:
            if self.hasVertex(label) is True:
                raise ValueError("Vertex already exists.")
        except ValueError as err:
            print(err)
        else: 
            newvertex = DSAGraphVertex(label)
            self.graphLL.insertLast(newvertex)
            self.vcount +=1
       

    def delVertex(self, label):
        try:
            if self.hasVertex(label) is False:
                raise ValueError("Vertex does not exist.")
        except ValueError as err:
            print("Invalid!", err)
        else: 
            vertex = self.getVertex(label)
            # print(vertex.getValue().getLabel())
            #iterate through edgelist linkedlist of ALL VERTEX to find DELETED VERTEX and remove it
            edgevertex = self.graphLL.returnHead()      #LL
            while edgevertex is not None: 
                # print(edgevertex.getValue().getLabel())
                if self.isAdjacent(edgevertex.getValue().getLabel(), vertex.getValue().getLabel()) == True: #stop it from printing exception handling
                    self.delEdge(edgevertex.getValue().getLabel(), vertex.getValue().getLabel())    #Vertex
                # print(vertex) #LL
                edgevertex = edgevertex.getNext()           #LL

            #then delete the vertex itself
            self.graphLL.deleteNode(vertex.getValue())
            self.vcount -=1

  
    def addEdge(self, label1, label2, weight):
        vertex1 = self.getVertex(label1)
        vertex2 = self.getVertex(label2)

        try: 
            if label1 == label2:
                raise ValueError("You can't add an Edge inside a Vertex")
        except ValueError as err:
            print("Invalid!", err)
    
        else: 
            try:
                if self.isAdjacent(label1, label2):
                    raise ValueError("Edge already exists.")
            except ValueError as err:
                print("Invalid!", err)
        
            else: 
                try:
                    if vertex1 is None or vertex2 is None:
                    # Check if both vertices exist
                        raise ValueError("")
                except ValueError as err:
                    print("", err)
                else:
                        # Add edge between the vertices
                        vertex1.getValue().addVEdge(label2, weight)
                        self.ecount +=1
                        if self.bothdirections == True:
                            vertex2.getValue().addVEdge(label1, weight)
                            self.ecount +=1
        
    def delEdge(self, label1, label2, printoutput=True):
        vertex1 = self.getVertex(label1)
        vertex2 = self.getVertex(label2)

        try: # Check if both vertices exist
            if vertex1 is None or vertex2 is None:                    
                    raise ValueError("Atleast one Vertex does not exist.")
        except ValueError as err:
                print("Invalid!", err)
        else:
            try: #check if the edge exists
                if self.isAdjacent(label1, label2) == False:
                    raise ValueError("Edge does not exist.")
            except ValueError as err:
                print("Invalid!", err)
            else:
                #iterate through edgelist linkedlist of vertex 1 to find vertex 2 label and remove it
                vertex1.getValue().delVEdge(label2)
                self.ecount -=1
                
                if self.bothdirections:
                #iterate through edgelist linkedlist of vertex 2 to find vertex 1 label and remove it
                    vertex2.getValue().delVEdge(label1)
                    self.ecount -=1
                print("Deleting Edge between", label1, "and", label2,"...")

                    
            
    def hasVertex(self, label):
        try: 
            if self.graphLL.returnHead() == False:
                raise ValueError("Graph is empty!")
        except ValueError as err:
                print("\nInvalid!", err)     
        else:        
            current = self.graphLL.returnHead()
            while current is not None:
                if current.getValue().getLabel() == label:
                    return True
                current = current.getNext()
            return False

    def getVertex(self, label):
        try: 
            if self.graphLL.returnHead() == False:
                raise ValueError("Graph is empty!")
        except ValueError as err:
                print("\nInvalid!", err)     
        else:        
            current = self.graphLL.returnHead()
            while current is not None:
                if current.getValue().getLabel() == label:
                    return current
                current = current.getNext()
            return None


    def getAdjacent(self, label):       
        vertex = self.getVertex(label)
        # Check if vertix exists
        try:
            if vertex is None:
                raise ValueError("Vertex does not exist.")
        except ValueError as err:
                print("Invalid!", err)
        else:
            # Add edge between the vertices
            print(vertex.getValue().getAdjacent())
 


    def isAdjacent(self, label1, label2):
        vertex1 = self.getVertex(label1)
        vertex2 = self.getVertex(label2)
        # Check if both vertices exist
        try:
            if vertex1 is None or vertex2 is None:
                # Check if both vertices exist
                raise ValueError("Atleast one Vertex does not exist.")
        except ValueError as err:
                print("Invalid!", err)
        else:
            if not vertex1.getValue().edgelist.isEmpty(): #if vertex has no edges (common if graph is directional)

            # check is vertex2 is in vertex1's edge list
                if vertex2.getValue().getLabel() in vertex1.getValue().getAdjacent():
                    return True
                else:
                    return False
            else: 
                return False

    def getVertexCount(self):
        # print(self.vcount) 
        return self.vcount
    
    def getEdgeCount(self):
        if self.bothdirections is True:
            edgecount = int(self.ecount/2)
            # print(edgecount)
            return edgecount
        else:
            # print(self.ecount)
            return self.ecount

    def adjacencyList(self, printAdj=True):
        AQueue = CircularQueue()
        try: 
            if self.graphLL.isEmpty() == True: 
                raise ValueError("Graph is Empty")
        except ValueError as err:
                print("Invalid!", err)
        else: 
            if printAdj is True:
                    
                print("\nAdjacency List: ")
            current = self.graphLL.returnHead()
            while current is not None: 
                if not current.getValue().edgelist.isEmpty(): #if vertex has no edges (common if graph is directional)
                    vlabel = current.getValue().getLabel()
                    alabels = current.getValue().getAdjacent()
                else:
                    vlabel = current.getValue().getLabel()
                    alabels = None
                
                if printAdj is True:
                    print("Vertex", vlabel + ":", alabels)
                AQueue.enQueue(vlabel)          #for display enture list purposes
                current = current.getNext()
            return AQueue
            

    def displayAsMatrix(self):

        vertexcount = self.getVertexCount()
        edgecount = self.getEdgeCount()

        #label lookup
        labellookup = np.zeros((vertexcount, 2), dtype=object)

        for i in range(len(labellookup)):
            labellookup[i, 0] = i 

        current = self.graphLL.returnHead()
        while current is not None: 
            for j in range(len(labellookup)):
                vlabel = current.getValue().getLabel()
                labellookup[j, 1] = vlabel
                current = current.getNext()

        #matrix
        matrix = np.zeros(((vertexcount+1), (vertexcount+1)), dtype=int)
        for i in range(vertexcount+1):
            matrix[i, 0] = i-1 
            matrix[0, i] = i-1
        matrix[0, 0] = 0

        for j in range(vertexcount):    #for each vertex
            for k in range(vertexcount): #for each vertex that could be within vertex edgelist
                if self.isAdjacent(labellookup[j, 1], labellookup[k, 1]):
                    matrix[k+1, j+1] = 1 #make it 1 if vertex is in vertex's edge list
                else: 
                    matrix[k+1, j+1] = 0

        print("\nLabel Lookup:")            
        print(labellookup)
        print("\nDisplay as Matrix: ")
        print(matrix)


    def breadthFirstSearch(self, dest, dep):
        T = CircularQueue()
        Q = CircularQueue()

        # make sure all verticies are not visited
        vertex = self.graphLL.returnHead()      #LL
        while vertex is not None: 
            vertex.getValue().clearVisited()    #Vertex
            # print(vertex) #LL
            vertex = vertex.getNext()           #LL
        # from the departure vertex (instead of starting at head)
        departV = self.getVertex(dep)
        vertexV = departV     #LL - start at departure Vertex NOT head

        while vertexV is not None:
            vertexV.getValue().setVisited()     # v = old   #Vertex
            Q.enQueue(vertexV.getValue())       # insert (Q, v) #Vertex

            while not Q.isEmpty():              # while Q is not empty do
                vertexV = Q.deQueue()        # v = dequeue(Q)    #LL  
                # print(vertexV.getLabel(), "edgelist:", vertexV.edgelist.printit())
                if vertexV.getLabel() == dest:  #####stops routes leaving from destination airport
                    edgelistcopy = None
                else:
                    edgelistcopy = vertexV.edgelist.LLcopy()
                # print(vertexV.getLabel(), "edgelist:", edgelistcopy.printit())

                    while not edgelistcopy.isEmpty():
                        vertexE = edgelistcopy.peekFirst()      #LL
                        vertexW = self.getVertex(vertexE[0]).getValue()      #Vertex
                        # print("DSAGraphVertex", vertexW)
                        if not vertexW.getVisited():         # for each w in L[v] marked new
                            T.enQueue((vertexV, vertexW, vertexE[1]))    # add set {u, w} #Vertex
                            if vertexW.getLabel() != dest:      ####able to make multiple routes to destination airport
                                vertexW.setVisited()             # mark w as old

                            Q.enQueue(vertexW)               #insert (Q, w) #vertex
                        edgelistcopy.removeFirst()               
            else: 
                vertexV = None

        #Create label sets for BFS
        # Labelsets = CircularQueue()
        Labelsets = DoubleLinked()  #Linked List instead of Queue to go both directions if
        for i in range(T.getCount()):
            set_item = T.deQueue()
            # print(set_item)
            label1 = set_item[0].getLabel()
            label2 = set_item[1].getLabel()
            distance = set_item[2]
            # Labelsets.enQueue((label1, label2, distance))
            Labelsets.insertLast((label1, label2, distance)) #Linked List instead os Queue
        # print(Labelsets.printit())
        T.refresh()
        return Labelsets, T.getCount()
    
    
    def routecountnofilter(self, Tcount, Labelsets, dest):

        numberofroutes = 0
        spare = Labelsets.LLcopy()
        # for j in range(Labelsets.getCount()):
        for j in range(Tcount):     #Linked List instead os Queue
            flightedge = Labelsets.peekFirst() #Linked List instead os Queue
            flightdest = flightedge[1]
            if flightdest == dest:
                numberofroutes += 1
            Labelsets.removeFirst()
        Labelsets = spare
        # Labelsets.refresh()

        return Labelsets, numberofroutes


    def DestBFSbylay(self, dest, dep, maxlay):     #BFS but towards a specified Airport - specified max layover
        with open('filteredroutes.csv', 'w') as routeoutput:
            routeoutput.write("")

        Labelsets, Tcount = self.breadthFirstSearch(dest, dep)
        Labelsets, numberofroutes = self.routecountnofilter(Tcount, Labelsets, dest)

        print("\nNumber of unfiltered routes available:", numberofroutes)
        print("Searching Route options (Layover filter on)...")

        Labelcount = Labelsets.getCount()
        # print(Labelcount)
        kk = True

        routeno = 1
        while kk is True: 
            for k in range(numberofroutes):
                skipexport = False
                routestack = DSAStack()
                Labelcount = Labelsets.getCount()           #green fault
                layovercount = -1
                accdistance = 0
                
                #some code to extract routes in order
                tempdest = dest
                tempdep = dep
                pusheddep = "z"

                while pusheddep != tempdep and layovercount <= int(maxlay):
                    # print("\nwhile", pusheddep, "is not", tempdep)
                    flightedge = Labelsets.peekLast() #Linked List instead os Queue?
                    # print("peek last", flightedge)
                    flightL1 = flightedge[1]
                    # print("Label 1 (destination):", flightL1)
                    flightL0 = flightedge[0]
                    # print("Label 0 (departure):", flightL0)
                
                    if flightL1 == tempdest:
                        # print("if", flightL1, "== tempdest:", tempdest)
                        routestack.push(flightedge)
                        pusheddep = flightL0
                        layovercount += 1
                        accdistance += int(flightedge[2])
                        # print("pushed", flightedge)
                        # print("make tempdest", tempdest, "now equal", flightL0)
                        tempdest = flightL0
                        # print("removed", Labelsets.peekLast())
                        Labelsets.removeLast()
                        Labelcount -= 1
                        # print("Safs Label count", Labelcount)
                        # print("Actual Labelcount", Labelsets.getCount())

                    else: 
                        if Labelcount > 0:          #solve dead-end issues
                            # print("Label count is over 0")
                            # print("does", flightL1, "== tempdest:", tempdest)
                            # print(flightL1, "does not equal tempdest:", tempdest)
                            # Labelsets.printit()
                            # print("inserted", Labelsets.peekLast(), "as head node (to move it out of the way)")
                            Labelsets.insertFirst(Labelsets.peekLast())
                            # Labelsets.printit()
                            Labelsets.removeLast()
                            Labelcount -= 1

                        else:                           #issues with infinite loop when route is dead-end - removes dead-end in stack and continues journey
                            # print("INFINITE LOOP AVOIDANCE STRATEGY")

                            if routestack.getCount() > 0:
                                # print("1")
                                routestack.pop()

                                if routestack.getCount() > 0:
                                    # print("2")
                                    toplabel = routestack.top()
                                    # print(toplabel)
                                    pusheddep = toplabel[0]
                                    tempdest = toplabel[0]
                                    Labelcount = Labelsets.getCount()

                                else:
                                    # print("3")
                                    skipexport = True
                                    break           #break out of while loop - alternative?


                            else: 
                                # print("4")
                                pusheddep = "z"
                                tempdest = dest
                                if Labelsets.getCount() > 0:
                                    Labelsets.removeLast()
                                    Labelcount = Labelsets.getCount()
                                else: 
                                    kk = False
                                


                if skipexport == False:
                    if layovercount <= int(maxlay):

                        # print("\nRoute Option:", routeno, " Layovers: ", layovercount, " Distance: ", accdistance)
                        # routestack.printit() #do something with this stack!
                        #Make a queue with this stack

                        routequeue = CircularQueue()
                        while not routestack.isEmpty():
                            routequeue.enQueue(routestack.pop())
                        self.export(routequeue, layovercount, accdistance)
                        routeno +=1

            
            
            print("\nNumber of routes available: ", routeno-1)
            kk = False


    def DestBFSbydist(self, dest, dep, maxdist):     #BFS but towards a specified Airport - specified max distance
        with open('filteredroutes.csv', 'w') as routeoutput:
            routeoutput.write("")

        Labelsets, Tcount = self.breadthFirstSearch(dest, dep)
        Labelsets, numberofroutes = self.routecountnofilter(Tcount, Labelsets, dest)

        print("\nNumber of unfiltered routes available:", numberofroutes)
        print("Searching Route options (Distance filter on)...")

       
        Labelcount = Labelsets.getCount()
        # print(Labelcount)
        kk = True

        routeno = 1
        while kk is True: 
            for k in range(numberofroutes):
                skipexport = False
                routestack = DSAStack()
                Labelcount = Labelsets.getCount()           #green fault
                layovercount = -1
                accdistance = 0
                
                #some code to extract routes in order
                tempdest = dest
                tempdep = dep
                pusheddep = "z"

                while pusheddep != tempdep and layovercount <= int(maxdist):
                    # print("\nwhile", pusheddep, "is not", tempdep)
                    flightedge = Labelsets.peekLast() #Linked List instead os Queue?
                    # print("peek last", flightedge)
                    flightL1 = flightedge[1]
                    # print("Label 1 (destination):", flightL1)
                    flightL0 = flightedge[0]
                    # print("Label 0 (departure):", flightL0)
                
                    if flightL1 == tempdest:
                        # print("if", flightL1, "== tempdest:", tempdest)
                        routestack.push(flightedge)
                        pusheddep = flightL0
                        layovercount += 1
                        accdistance += int(flightedge[2])
                        # print("pushed", flightedge)
                        # print("make tempdest", tempdest, "now equal", flightL0)
                        tempdest = flightL0
                        # print("removed", Labelsets.peekLast())
                        Labelsets.removeLast()
                        Labelcount -= 1
                        # print("Safs Label count", Labelcount)
                        # print("Actual Labelcount", Labelsets.getCount())

                    else: 
                        if Labelcount > 0:          #solve dead-end issues
                            # print("Label count is over 0")
                            # print("does", flightL1, "== tempdest:", tempdest)
                            # print(flightL1, "does not equal tempdest:", tempdest)
                            # Labelsets.printit()
                            # print("inserted", Labelsets.peekLast(), "as head node (to move it out of the way)")
                            Labelsets.insertFirst(Labelsets.peekLast())
                            # Labelsets.printit()
                            Labelsets.removeLast()
                            Labelcount -= 1

                        else:                           #issues with infinite loop when route is dead-end - removes dead-end in stack and continues journey
                            # print("INFINITE LOOP AVOIDANCE STRATEGY")

                            if routestack.getCount() > 0:
                                # print("1")
                                routestack.pop()

                                if routestack.getCount() > 0:
                                    # print("2")
                                    toplabel = routestack.top()
                                    # print(toplabel)
                                    pusheddep = toplabel[0]
                                    tempdest = toplabel[0]
                                    Labelcount = Labelsets.getCount()

                                else:
                                    # print("3")
                                    skipexport = True
                                    break           #break out of while loop - alternative?


                            else: 
                                # print("4")
                                pusheddep = "z"
                                tempdest = dest
                                if Labelsets.getCount() > 0:
                                    Labelsets.removeLast()
                                    Labelcount = Labelsets.getCount()
                                else: 
                                    kk = False
                                


                if skipexport == False:
                    if accdistance <= int(maxdist):
                
                        # print("\nRoute Option:", routeno, " Layovers: ", layovercount, " Distance: ", accdistance)
                        # routestack.printit() #do something with this stack!
                                #Make a queue with this stack

                        routequeue = CircularQueue()
                        while not routestack.isEmpty():
                            routequeue.enQueue(routestack.pop())
                        self.export(routequeue, layovercount, accdistance)
                        routeno +=1

            
            
            print("\nNumber of filtered routes available: ", routeno-1)
            kk = False


    def export(self, routeimport, layovercount, accdistance):

        with open('filteredroutes.csv', 'a', newline="") as routeoutput:
            
            routeoutput.write(str(layovercount) + "," + str(accdistance) + ",")
            while not routeimport.isEmpty(): 
                routetuple = routeimport.Peek()     
                routeoutput.write(routetuple[0] + "," + routetuple[1] + ",")
                routeimport.deQueue()
            routeoutput.write("\n")


    def depthFirstSearch(self):
        T = CircularQueue()
        S = DSAStack()

# make sure all verticies are not visited
        vertex = self.graphLL.returnHead()      #LL
        while vertex is not None: 
            vertex.getValue().clearVisited()    #Vertex
            # print(vertex) #LL
            vertex = vertex.getNext()           #LL

# from the first vertex
        vertexV = self.graphLL.returnHead()     #LL mark any one vertex v to old
        vertexV.getValue().setVisited()     # v = old   #Vertex
        S.push(vertexV.getValue())       # push (S, v) #Vertex
        vertexV = vertexV.getValue()        #make vertex

        while not S.isEmpty():          #while S is nonempty do
            vertexV = S.top()

            edgelistcopy = vertexV.edgelist.LLcopy()

# find the next unvisited vertex (and make it Vertex W) in the Vertex V edge list
            vertexW = None
            neighbour = edgelistcopy.returnHead()
            while neighbour is not None and vertexW is None:
                vertexE = neighbour.getValue()
                if self.getVertex(vertexE).getValue().getVisited() == True: #iterate through edgelist until getvisited = False
                    edgelistcopy.removeFirst()
                    neighbour = edgelistcopy.returnHead()
                else:
                    vertexW = self.getVertex(vertexE).getValue()

#Queue set, make vertex W visited, push onto stack
            if vertexW is not None:
                T.enQueue({vertexV, vertexW}) 
                vertexW.setVisited()
                S.push(vertexW)
#backtrack if Vertex V edgelist has no vertex's that haven't been visited
            else:
                S.pop()

        print("\nDepth First Search:")
        Labelsets = CircularQueue()
        for i in range(T.getCount()):
            set_item = T.deQueue()
            label1 = set_item.pop().getLabel()
            label2 = set_item.pop().getLabel()
            Labelsets.enQueue({label1, label2})
        Labelsets.printit()

   