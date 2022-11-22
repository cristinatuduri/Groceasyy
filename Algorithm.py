
import numpy as np
import pandas as pd
from typing import DefaultDict
section_names = np.array([[0,10,7,5,7,9,12,10]]) #names of selection, first array already written because its section1 = door
    
section2 = np.array([[10,0,4,8,12,16,20,10]])
section3 = np.array([[7,4,0,4,8,12,16,6]])
section4 = np.array([[5,8,4,0,4,8,12,5]])
section5 = np.array([[7,12,8,4,0,4,8,6]])
section6 = np.array([[9,16,12,8,4,0,4,8]])
section7 = np.array([[12,20,16,12,8,4,0,12]])
section8 = np.array([[10,10,6,5,6,8,12,0]])
names = ["Door"]

while True: 
        
    ask = input("Type the desired sections in order (section 1, section 2), Type q to quit: ").lower()

    if ask == "section 2": 
        #selected.update(s2)
        section_names = np.vstack([section_names,section2])
        names.append('section 2')
    if ask == "section 3": 
        section_names = np.vstack([section_names,section3])
        names.append('section 3')
    if ask == "section 4": 
        section_names = np.vstack([section_names,section4])
        names.append('section 4')
    if ask == "section 5": 
        section_names = np.vstack([section_names,section5])
        names.append('section 5')
    if ask == "section 6": 
        section_names = np.vstack([section_names,section6])
        names.append('section 6')
    if ask == "section 7": 
        section_names = np.vstack([section_names,section7])
        names.append('section 7')
    if ask == "section 8": 
        section_names = np.vstack([section_names,section8])
        names.append('section 8')
    if ask in section_names: 
        pass
    else: 
        if ask == "q":
            break
        


count = 0 
if 'section 2' not in names:
    section_names = np.delete(section_names,1, axis = 1)
    count += 1
if 'section 3' not in names:
    section_names = np.delete(section_names, 2 - count, axis = 1)
    count += 1
if 'section 4' not in names:
    section_names = np.delete(section_names,3 - count, axis = 1)  
    count += 1     
if 'section 5' not in names:
    section_names = np.delete(section_names,4 - count, axis = 1)    
    count += 1    
if 'section 6' not in names:
    section_names = np.delete(section_names,5 - count, axis = 1)
    count += 1
if 'section 7' not in names:
    section_names = np.delete(section_names,6 - count , axis = 1)
    count += 1
if 'section 8' not in names:
    section_names = np.delete(section_names,7 - count, axis = 1)
    count += 1


plus = 1
route_names = {}
while plus <= len(names):
    for i in names:
        route_names[i] = plus
        plus += 1



 
# Function to find the minimum
# cost path for all the paths

INT_MAX = 2147483647

def findMinRoute(section_names):
    sum = 0
    counter = 0
    j = 0
    i = 0
    min = INT_MAX
    visitedRouteList = DefaultDict(int)
 
 
    # Starting from the 0th indexed
    # city i.e., the first city
    visitedRouteList[0] = 1
    route = [0] * len(section_names)

    # Traverse the adjacency
    # matrix tsp[][]
    while i < len(section_names) and j < len(section_names[i]):

  
        # Corner of the Matrix
        if counter >= len(section_names[i]) - 1:
            break

        # If this path is unvisited then
        # and if the cost is less then
        # update the cost
        if j != i and (visitedRouteList[j] == 0):
            if section_names[i][j] < min:
                min = section_names[i][j]
                route[counter] = j + 1

        j += 1

        # Check all paths from the
        # ith indexed city
        if j == len(section_names[i]):
            sum += min
            min = INT_MAX
            visitedRouteList[route[counter] - 1] = 1
            j = 0
            i = route[counter] - 1
            counter += 1

    # Update the ending city in array
    # from city which was last visited
    i = route[counter - 1] - 1

    for j in range(len(section_names)):

        if (i != j) and section_names[i][j] < min:
            min = section_names[i][j]
            route[counter] = j + 1

            
    sum += min


    # Started from the node where
    # we finished as well.


    path = []
    path_start = [1]
    for i in route:
        path.append(i)

    path = path_start + path[0:-1] + path_start

    
                
    print("WELCOME TO GROC EASY: \nWHERE SHOPPING BECOMES THE EASIEST THING TO DO")
    print("Instructions: \n - Type the sections in order of number. \n - Type quit to finish the route")
    
    print(f"Optimized route is: ")
    for num in path: 
        for key in route_names:
            if num in route_names.values():
                print(f"Go to {key}")
        print(f"Finally pay groceries in cash register ")
        break
    
    print("Total steps through route :", sum)
 







# Driver Code
if __name__ == "__main__":
    findMinRoute(section_names)