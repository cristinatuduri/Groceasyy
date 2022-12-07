
import numpy as np
import pandas as pd
from typing import DefaultDict
import json
from json import JSONEncoder
import numpy


print("WELCOME TO GROC EASY: \nWHERE SHOPPING BECOMES THE EASIEST THING TO DO")
print("Instructions: \n - Grammar Errors will influence the output \n - Type 'section 2', 'section 3' etc... to select the secitions ")
print('\nInformation about the available sections: \nSection 2: Bakery \nSection 3: Meat \nSection 4: Frozen Products \nSection 5: Foods & Vegetables \nSection 6: Drinks \nSection 7: Cleaning Products \nSection 8: Sea Food')

#Numpy matrices with distances between each section
section_names = np.array([[0,10,7,5,7,9,12,10]]) #names of selection, first array already written because its section1 = door

matrix =  np.array([[0,10,7,5,7,9,12,10],
                    [10,0,4,8,12,16,20,10], 
                    [7,4,0,4,8,12,16,6],
                    [5,8,4,0,4,8,12,5],
                    [7,12,8,4,0,4,8,6],
                    [9,16,12,8,4,0,4,8],
                    [12,20,16,12,8,4,0,12],
                    [10,10,6,5,6,8,12,0]])

#Section names for future implementation
sections = ['section 2: Bakery','section 3: Meat','section 4: Frozen Products','section 5: Foods & Vegetables','section 6: Drinks','section 7: Cleaning Products','section 8: Sea Food']
section = ['section 2','section 3','section 4','section 5','section 6','section 7','section 8']
names = ["Door"]



#Two if statemnts, New or Import. Self explanatory


route_import = input("Type import to 'import' saved routes. If not type 'new' to continue and create a new Route: ").lower()
if route_import == "new":
    while True:
        ask = input("Type the desired sections you want to go through. To finish Type 'q' to quit: ").lower()

        if ask in section:
            pos = section.index(ask)
            short = ask[0:9].replace(" ","")
            section_names = np.vstack([section_names,matrix[pos +1]]) #for every section written = appended to the new matrix to calculate distances
            names.append(sections[pos])
        if ask == "q":
            break
        if ask not in section: 
            print("!! Section DOES NOT EXIST. \n 1. Make sure youre grammar is correct \n 2. Only type the section and the desired number ")

    count = 0   
    nm = 1
    
    for i in sections:
        if i in names: 
            nm += 1
        elif i not in names:
            section_names = np.delete(section_names,nm - count, axis = 1) #deletes the distances froms sections that are not selected

            nm +=1
            count +=1     

    class NumpyArrayEncoder(JSONEncoder): #json encoder from a website in order to save and import routes from the user
        def default(self, obj):
            if isinstance(obj, numpy.ndarray):
                return obj.tolist()
            return JSONEncoder.default(self, obj)


    plus = 1
    route_names = {}
    while plus <= len(names):
        for i in names:
            route_names[i] = plus
            plus += 1
    
    #If statment to ask if user wants to save path
    route_json = input("If you want to save the path type 'save' if not type 'next' ").lower()
    if route_json == "save":
        my_route_name = input("type the name to save the path: ")
        numpyData = {my_route_name: section_names, f"route_names_{my_route_name}":route_names}
        encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)
        with  open('json_data.json', 'w') as outfile: 
            outfile.write(encodedNumpyData)

#If user selects to import data 
if route_import == "import":
                name_import = input("Type the name of the route you saved: ")
                with open('json_data.json') as json_file:
                    data = json.load(json_file)
                section_names = data[name_import] 
                route_names = data[f"route_names_{name_import}"]




# Function to find the minimum
# cost path for all the paths
INT_MAX = 2147483647

#Travelling Salesman Problem
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
    try:
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


        print(f"Optimized route is: ")
        
        for num in path: 

            for key in route_names:
                if num in route_names.values():
                    print(f"### Go to {key} ###")
            print(f"Finally pay groceries in cash register ")
            break
        
        print("Total steps through route :", sum)
    except: 
        print("You have typed 'import' or 'new' incorrectly. Make sure youre grammar is correct")
    
 




if __name__ == "__main__":
    findMinRoute(section_names)