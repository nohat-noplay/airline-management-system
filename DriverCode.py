# DriverCode.py
#
# Main driver script for the AnywhereButThere Airline Management System.
# Handles user interaction through Login, Admin, and Customer menus.
#
# This system uses custom-built data structures (hash tables, graphs, heaps, linked lists) 
# to simulate airport lookups, route searches, and flight path management.
#
# Author: Saf Flatters
# Year: 2024

# Route search to print screen 

from GraphClass import *
from HashClass import *
from HeapClass import *


OpMenu = [
    "Admin Login",
    "Customer Login",
    "AUTOINSERT Airport LookUp (HashTable), 5 Airports and 7 Flight Paths into a Graph ",
    "AUTOINSERT Airport LookUp (HashTable), 36 Airports and 114 Flight Paths into a Graph ",
    "Performance Testing (Additional Marks)",
    "EXIT\n"
]

CustomerMenu= [
    "Search for a Route within Maximum Distance - sorted Min to Max Layovers or Distance(Q1, Q3)",            #Includes Prompts to determine Destination, Departure, Add Layover or Distance filter, Sort results by Layover/Distance and Print Results using Hashlookup
    "Search for a Route within Maximum Layovers - sorted Min to Max Layovers or Distance(Q1, Q3)",
    "Display Available Locations",
    "EXIT to Login Menu\n"
]

AdminMenu= [
    "AUTOINSERT: Airport Lookup Hash Table in two seperate lots to demonstrate collisions/resize (Q2)", 
    "AUTOINSERT: Add 38 Airports and 114 Flight Paths (Q1)",
    "DISPLAY: Airports (Hash Table)",
    "DISPLAY: Adjacency List (Q1.1)",
    "ADD: Airport (including Hash Lookup) (Q2)",
    "ADD: Flight Path (Q2)",
    "SEARCH: Airport Lookup (Hash Table) by Code (Q2)",
    "DELETE: Airport (Vertex and Hash Tabled item) (Q2)",
    "DELETE: Flight Path (Q2)",
    "EXIT to Login Menu\n"
]

#print menus
def Menu(options):                                      #Reference: TO avoid using dictionaries - enumerate function idea from DSA Tutor
    for number, option in enumerate(options, start=1):
        print(f"{number}: {option}")

hashtable = None
Flightpath = None

#intro
print("\nHello! Welcome to \'AnywhereButThere\' Travel Agency!")


menuop = None
while menuop not in ["1", "2", "3", "4", "5", "6"]:
    print("\n\nLogin Menu: ")
    print("--------------")
    Menu(OpMenu)


    try: 
        menuop = input("\nPlease select from the Menu...")
        if menuop not in ["1", "2", "3", "4", "5", "6", None]:
            raise ValueError("Please select valid number from Menu... ")
    except ValueError as err:
        print("\nInvalid!", err)
    else: 
##################################################################################################################            
        if menuop == "1":
            adminop = None
            
            while adminop not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
                print("\n\nAdmin Login Menu: ")
                print("--------------")
                Menu(AdminMenu)

                try: 
                    adminop = input("\nPlease select from the Menu...")
                    if adminop not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", None]:
                        raise ValueError("Please select valid number from Menu... ")
                except ValueError as err:
                        print("\nInvalid!", err)
                else: 
                    
                    if adminop == "1":
                        print("Inserting Airport Lookup (Hash Table) for 38 Airports in 2 lots to demonstrate collisions/resize...")
                        try: 
                            with open('AirportLookup.csv', 'r') as database:

                                data = database.readlines()
                                databasecount = 0
                                for line in data:
                                    databasecount +=1

                        except FileNotFoundError():
                            print("File can not be found. Please check the file path")

                        if hashtable is None:
                            hashtable = DSAHashTable(int(databasecount * 1.5))

                        for line in data: 
                            splitline = line.split(',')   
                            hashtable.put(splitline[0], ', '.join(splitline[1:4]))
                        

                        print("\n\n\nCOMPLETED Inserting Airport Lookup 1 into HashTable")

                        try: 
                            with open('AirportLookup2.csv', 'r') as database:

                                data = database.readlines()
                                databasecount = 0
                                for line in data:
                                    databasecount +=1

                        except FileNotFoundError():
                            print("File can not be found. Please check the file path")

                        for line in data: 
                            splitline = line.split(',')   
                            hashtable.put(splitline[0], ', '.join(splitline[1:4]))
                        

                        print("\n\n\nCOMPLETED Inserting Airport Lookup 2 into HashTable")

                        printlookup = input("Do you want to see print Airport Lookup (combined) Hash Table? Type \'Y\' or AnyKey to Return to Admin Menu... ").upper()
                        if printlookup == "Y":
                            hashtable.printHashTable()
                            adminop = None
                        else: 
                            adminop = None

                    elif adminop == "2":
                        try: 
                            with open('AirportDataTest.csv', 'r') as database:            #AirportDataTest.csv for 38 Airports (Verticies) and 114 Routes (Edges)
                                                                                                #SIMPLEAirportTestData.csv for 5 Airports (Verticies) and 7 Routes (Edges)
                                data = database.readlines()
                                databasecount = 0
                                for line in data:
                                    databasecount +=1

                        except FileNotFoundError():
                            print("File can not be found. Please check the file path")

                        if Flightpath is None:    
                            Flightpath = DSAGraph(True)

                        for line in data: 
                            splitline = line.split(',')   
                            Flightpath.addVertex(splitline[0])
                            Flightpath.addVertex(splitline[1])
                            Flightpath.addEdge(splitline[0], splitline[1], splitline[2])

                        print("....")
                        print(Flightpath.getVertexCount(), "Airports (verticies) added")     
                        print(Flightpath.getEdgeCount(), "Flight Paths (edges) and their distances added") 
                        adminreturn = input("\n\nReturn to Admin Menu? (press anykey)")
                        if adminreturn is not None:
                             adminop = None

                    elif adminop == "3":
                        print("Displaying Airport Lookup")

                        try:
                            if hashtable is None:
                                raise ValueError("HashTable does not exist - Please insert Airport Look up")
                        except ValueError as err:
                            print("\nInvalid!", err)
                            adminop = None
                        else:
                            hashtable.printHashTable()

                        adminreturn = input("\n\nReturn to Admin Menu? (press anykey)")
                        if adminreturn is not None:
                            adminop = None

                    elif adminop == "4":
                        print("Displaying Adjaceny List")
                        try:
                            if Flightpath is None:
                                raise ValueError("Graph does not exist - Please insert Airports")
                        except ValueError as err:
                            print("\nInvalid!", err)
                            adminop = None
                        else:
                            Flightpath.adjacencyList()
                            adminop = None

                    elif adminop == "5":
                        print("You selected input a new location into our database")

                        newcountry = input("Country: ")
                        newcity = input("City: ")
                        newairport = input("Airport: ")
                        newcode = input("Airport code: ").upper()

                        newlocation = str(newairport + "," + newcity + "," + newcountry)

                        #SVO,Sheremetyevo International Airport,Moscow,Russia
                        if hashtable is None:
                            hashtable = DSAHashTable(int(5))

                        hashtable.put(newcode, newlocation[0:])

                        if Flightpath is None:
                            Flightpath = DSAGraph(True)
 
                        Flightpath.addVertex(newcode)
                        adminop = None

                    elif adminop == "6":
                        print("You selected input a new flight path into our database")

                        insertpath1 = input("Type First Airport Code: ").upper()
                        insertpath2 = input("Type Second Airport Code: ").upper()

                        try:
                            pathdistance = int(input("ENTER distance in Kilometres between Locations "))
                        except ValueError:
                            print("Invalid! Please enter an integer")



                        if Flightpath is None:
                            Flightpath = DSAGraph(True)

                        Flightpath.addEdge(insertpath1, insertpath2, pathdistance)  #exception handling inside class
                        adminreturn = input("Return to Admin Menu? (press anykey) ")
                        if adminreturn is not None:
                            adminop = None

                    elif adminop == "7":
                        print("You selected Airport Lookup (Hash Table) by Code")
                        try:
                            if hashtable is None:
                                raise ValueError("HashTable does not exist - Please insert Airport Look up")
                        except ValueError as err:
                            print("\nInvalid!", err)
                            adminop = None
                        else:
                            retrieve = input("Type Airport Code you want to retrieve from Airport Lookup: \n").upper()
                            hashtable.get(retrieve)
                            adminop = None
                         
                    elif adminop == "8":
                        print("You selected Delete Airport (Vertex and Hash Tabled item)")
                        try:
                            if hashtable is None or Flightpath is None:
                                raise ValueError("HashTable or Graph does not exist - Please insert before delete")
                        except ValueError as err:
                            print("\nInvalid!", err)
                            adminop = None
                        else:
                            delete = input("Type Airport Code you want to delete from Graph and Airport Lookup: ").upper()
                            hashtable.remove(delete)
                            Flightpath.delVertex(delete)
                            adminop = None

                    elif adminop == "9":
                        print("You selected Delete Flight Path")
                        try:
                            if Flightpath is None:
                                raise ValueError("Graph does not exist - Please insert before delete")
                        except ValueError as err:
                            print("\nInvalid!", err)
                            adminop = None
                        else:
                            delete1 = input("Type First Airport Code you want to delete an Flight Path from: ").upper()
                            delete2 = input("Type Second Airport Code you want to delete the connecting Flight Path from: ").upper()
                            Flightpath.delEdge(delete1, delete2)
                            adminop = None

                    elif adminop == "10":
                        menuop = None

############################################################################################################################
        elif menuop == "2":

            custop = None
            print("\nCustomer Login Menu: ")
            while custop not in ["1", "2", "3", "4"]:
                print("--------------")
                Menu(CustomerMenu)

                try: 
                    custop = input("\nPlease select from the Menu...")
                    if custop not in ["1", "2", "3", "4", None]:
                        raise ValueError("Please select valid number from Menu... ")
                except ValueError as err:
                        print("\nInvalid!", err)
                else: 

                    ########################
                    if custop in ["1", "2"]:
                        if custop == "1":
                            specifiedmax = "D"
                        elif custop == "2":
                            specifiedmax = "L"
                    ###########################

                        print("SEARCH FOR A ROUTE BETWEEN TWO LOCATIONS...")

                        try:
                            if Flightpath is None:
                                raise ValueError("Airports and Flights do not exist - Please insert before Searching for Route")
                        except ValueError as err:
                            print("\nInvalid!", err)
                            menuop = None
                        else:

                    ####Clarify Departure and Destination 
                            print("\n Locations Available:")
                            AdjQueue = Flightpath.adjacencyList(False)

                            airportcount = AdjQueue.getCount()
                            for i in range(airportcount): 
                                    checknode = AdjQueue.deQueue()
                                    hashtable.get(checknode)
                                    
                            try:
                                if hashtable is None:
                                    raise ValueError("HashTable does not exist - Please insert Airport Look up")
                            except ValueError as err:
                                print("\nInvalid!", err)
                                menuop = None
                            else:
                            # #Testing purposes only - no user input
                            # destination = "MEL"
                            # departure = "LHR"

                                try:
                                    destination = input("\nType in Airport code for desired DESTINATION city: ").upper()
                                    if Flightpath.hasVertex(destination) is False:
                                        raise ValueError("Airport code does not exist")
                                except ValueError as err:
                                    print("\nInvalid!", err)
                                else:
                                    hashtable.get(destination)

                                try:
                                    departure = input("\nType in Airport code for desired DEPARTURE city: ").upper()
                                    if Flightpath.hasVertex(departure) is False:
                                        raise ValueError("Airport code does not exist")
                                except ValueError as err:
                                    print("\nInvalid!", err)
                                else:
                                    hashtable.get(departure)

                        ####Specified Maximum Distance or Layover when Customer selected Custop "1" or "2"

                                if specifiedmax == "L":
                                    Layovermax = True
                                    Distancemax = False
                                elif specifiedmax == "D":
                                    Layovermax = False
                                    Distancemax = True

                                if Layovermax == True:
                                    laymax1 = input("ENTER Maximum Layovers allowed: ")
                                    try:
                                        laymax = int(laymax1)
                                    except ValueError:
                                        print("Invalid! Please enter an integer")

                                elif Distancemax == True:
                                    distmax1 = input("ENTER Maximum Accumalative Distance allowed: ")
                                    try:
                                        distmax = int(distmax1)
                                    except ValueError:
                                        print("Invalid! Please enter an integer")

                                #Testing purposes only - no user input
                                # distmax = int("100")
                                # laymax = int("10")

                                # Complete a BFS with Departure and Destination, specifying max layover
                                if Layovermax == True:
                                    Flightpath.DestBFSbylay(destination, departure, laymax) 

                                elif Distancemax == True:
                                # Complete a BFS with Departure and Destination, specifying max distance
                                    Flightpath.DestBFSbydist(destination, departure, distmax) 

                                # print("Exported Flight Path options (with maximum filtered) to filteredroutes.csv...")


                        #### HeapSort filtered routes by either Layovers or Distance
                        #####################################
                        #take csv file from filtered routes and sort routes available either by distance or layover amount - export into another csv

                                #Testing purposes only - no user input
                                # sortedby = "L"

                                #Stop it going further if no results
                                try: 
                                    with open('filteredroutes.csv', 'r') as database:

                                        data = database.readlines()
                                        databasecount = 0
                                        for line in data:
                                            databasecount +=1

                                except FileNotFoundError():
                                    print("File can not be found. Please check the file path")

                                if databasecount == 0:
                                    print("There are no results for routes between", destination, "and", departure)
                                    if Layovermax == True:
                                        print("within", laymax, "layovers")
                                    else:
                                        print("within", distmax, "accumalated distance")
                                        
                                    custreturn = input("\n\nReturn to Customer Menu? (press anykey) ")
                                    if custreturn is not None:
                                        custop = None
                                else:


                                
                                    ###User input whether they would like Layover or Distance Filter
                                    sortedby = input("SORT DISPLAY RESULTS BY... \nENTER \"L\" to SORT by amount of Layovers    OR     ENTER \"D\" to SORT by Accumalative Distance: ").upper()
                                    
                                    try:
                                        if sortedby not in ["L", "D"]:
                                            raise ValueError("You must select \"L\" OR \"D\"...")
                                    except ValueError as err:
                                        print("\nInvalid!", err)
                                    else:
                                        if sortedby == "L":
                                            Layoversort = True
                                            Distancesort = False
                                        elif sortedby == "D":
                                            Layoversort = False
                                            Distancesort = True

                                    print("\nFlight Route Options for:")
                                    print("___________________________")
                                    hashtable.get(departure)
                                    print("      to")
                                    hashtable.get(destination)
                                    print("___________________________")
                                    #from opened filteredroutes.csv
                                                                
                                    routeheap = DSAHeap(int(databasecount +1))

                                    for line in data:           #avoid list by making string
                                        splitline = line.split(',')
                                        if Layoversort == True: 
                                            heapdata = splitline[1] 
                                            for item in splitline[2:-1]:
                                                heapdata += "," + item  
                                            routeheap.add(splitline[0], heapdata) #sort by layover (2nd item in distance)
                                        else:
                                            heapdata = splitline[0] + "," + splitline[2]
                                            for item in splitline[3:-1]:
                                                heapdata += "," + item
                                            routeheap.add(splitline[1], heapdata) # sort by distance (1st item is layover)
                                        

                                    routeheap.heapSort()
                                    routeheap.export()

                                    # print("Exported Heap Sorted routes (by Distance or Layover (Min-Max)) to heaproutes.csv...")

                
                            #### Display route information by importing heaproutes.csv and hash.get() all codes to display Option[1]: Layover [], Distance [], City>City>City..

                                    try: 
                                        with open('heaproutes.csv', 'r') as database:

                                            data = database.readlines()
                                            databasecount = 0
                                            for line in data:
                                                databasecount +=1

                                    except FileNotFoundError():
                                        print("File can not be found. Please check the file path")

                                    if Layoversort == True:
                                        print("\n >>>    Sorted by Layover amount (Minimum to Maximum)")
                                    else:
                                        print("\n >>>   Sorted by Accumalated Distance (Minimum to Maximum)")

                                    for line in data:           
                                        splitline = line.split(',')
                                        optionno = splitline[0]

                                        if Layoversort == True: 
                                            layno = splitline[1] 
                                            distno = splitline[2]

                                        else:
                                            layno = splitline[2] 
                                            distno = splitline[1]

                                        flightcount = 0
                                        print("\n\nOPTION", optionno, ": LAYOVERS:", layno, " DISTANCE:", distno)
                                        for item in splitline[3:-1]:
                                                
                                                if flightcount % 2 == 0:
                                                    print("\n        ----Flight: ", int(flightcount/2 + 1), "-----")
                                                hashtable.get(item)
                                                flightcount += 1
                                    
                                    print("_________________________________________________________")
                                    custreturn = input("\n\nReturn to Customer Menu? (press anykey) ")
                                    if custreturn is not None:
                                        custop = None

                    elif custop == "3":
                        print("\n Locations Available:")
                        try:
                            if Flightpath == None:
                                raise ValueError("Locations do not exist. Try inserting airports")
                        except ValueError as err:
                                print("\nInvalid!", err)
                        else: 
                            AdjQueue = Flightpath.adjacencyList(False)

                            airportcount = AdjQueue.getCount()
                            for i in range(airportcount): 
                                    checknode = AdjQueue.deQueue()
                                    hashtable.get(checknode)


                        custreturn = input("\n\nReturn to Customer Menu? (press anykey) ")
                        if custreturn is not None:
                            custop = None       

                    else: 
                        menuop = None

##############################################################################################################################################################

        elif menuop in ["3", "4"]:
            
            #AirportDataTest.csv for 38 Airports (Verticies) and 114 Routes (Edges)
            #SIMPLEAirportTestData.csv for 5 Airports (Verticies) and 7 Routes (Edges)

            if menuop == "3":
                print("AUTOINSERT Airport LookUp (HashTable), 5 Airports and 7 Flight Paths into a Graph")
                VEinsert = "SIMPLEAirportTestData.csv"

            elif menuop == "4":
                print("AUTOINSERT Airport LookUp (HashTable), 38 Airports and 114 Flight Paths into a Graph")
                VEinsert = "AirportDataTest.csv"


            print("Inserting Airport Lookup (Hash Table) for 38 Airports in 2 lots to demonstrate collisions/resize...")
            try: 
                with open('AirportLookup.csv', 'r') as database:

                    data = database.readlines()
                    databasecount = 0
                    for line in data:
                        databasecount +=1

            except FileNotFoundError():
                print("File can not be found. Please check the file path")

            if hashtable is None:
                hashtable = DSAHashTable(int(databasecount * 1.5))

            for line in data: 
                splitline = line.split(',')   
                hashtable.put(splitline[0], ', '.join(splitline[1:4]))
            

            print("\n\n\nCOMPLETED Inserting Airport Lookup 1 into HashTable")

            try: 
                with open('AirportLookup2.csv', 'r') as database:

                    data = database.readlines()
                    databasecount = 0
                    for line in data:
                        databasecount +=1

            except FileNotFoundError():
                print("File can not be found. Please check the file path")

            for line in data: 
                splitline = line.split(',')   
                hashtable.put(splitline[0], ', '.join(splitline[1:4]))
            

            print("\n\n\nCOMPLETED Inserting Airport Lookup 2 into HashTable")

            print("Displaying Airport Lookup")
            hashtable.printHashTable()

            try: 
                print("AUTOINSERT Specified amount of Airports and Flight Paths")
                with open(VEinsert, 'r') as database:            #AirportDataTest.csv for 38 Airports (Verticies) and 114 Routes (Edges)
                                                                #SIMPLEAirportTestData.csv for 5 Airports (Verticies) and 7 Routes (Edges)
                    data = database.readlines()
                    databasecount = 0
                    for line in data:
                        databasecount +=1

            except FileNotFoundError():
                print("File can not be found. Please check the file path")

            if Flightpath is None:    
                Flightpath = DSAGraph(True)

            for line in data: 
                splitline = line.split(',')   
                Flightpath.addVertex(splitline[0])
                Flightpath.addVertex(splitline[1])
                Flightpath.addEdge(splitline[0], splitline[1], splitline[2])

            print("....")
            print(Flightpath.getVertexCount(), "Airports (verticies) added")     
            print(Flightpath.getEdgeCount(), "Flight Paths (edges) and their distances added") 

            
            print("Displaying Adjaceny List")
            try:
                if Flightpath is None:
                    raise ValueError("Graph does not exist - Please insert Airports")
            except ValueError as err:
                print("\nInvalid!", err)
                menuop = None
            else:
                Flightpath.adjacencyList()
                menuop = None


###################################################################################################################
        elif menuop == "5":
            print("Performance Testing...\n")       #ADDITIONAL MARKS - RUN BY BASH SHELL & DISCUSSION IN REPORT
            
            print("Open \'AdditionalMarks\' subfolder in commandline and type \'./input.sh'\'\n\n")

            menuop = "6"

####################################################################################################################
        elif menuop == "6":
            print("You chose EXIT. Goodbye!\n")
            
        
              