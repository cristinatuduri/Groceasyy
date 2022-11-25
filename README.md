# Project name - Groceasy
Groceasy is an application that maps out the shortest route to get all your desired items at the supermarket

Our platform's main purpose is:
* optimizing the time you spend shopping at the supermarket

# Installation 
To run our program, we have installed and imported the following packages:
* Python programming language (version 3.11.0, although it will work with other versions)
* NumpPy library --> ```pip install numpy```
* Pandas library --> ```pip install pandas```
* json library --> ```pip install json```
 * JSONEncoder --> ```from json import JSONEncoder```
* DefaultDict (from the typing library) ```pip install typing``` --> ```from typing import DefaultDict```

Once you have the libraries installed and set up, you can open the file named Algorithm.py and run the program.

# Usage
After the user has oppened the app, it will display the available sections to choose from and what they each contain.
The sections are the following:
* Section 2: Bakery
* Section 3: Meat
* Section 4: Frozen products
* Section 5: Fruits and vegetables
* Section 6: Drinks
* Section 7: Cleaning Products
* Sectiojn 8: Seafood

The user will get asked if he/she would like to import a shopping list from another usage or to start a new one.
* User chooses to start a new shopping list:
  1. He/she will get the option to type in a shopping list one by one which sections he/she would like to go through 
  2. When the user is finished typing the sections, he/she will type 'q'
  3. The user will get asked if he/she would like to save the typed in shopping list ('save' if they want to save it or 'next' if they don't)
   * If typed in 'save' the program will ask the user to give the shopping list a name

* User chooses to import an already used shopping list:
  1. Program asks the user the name of the previously saved list
  
Then the program will print the user's optimized route starting at the door and finishing at the chashier
And lastly it will print the number of steps the route will take
  
# Some extra information about the code
The main algorithm we used for the code is:
* the greedy approach 
  * from it we mainly used the traveling salesman problem

Some data structures that we used in the algorithm are:
* arrays
* matrices
* dicitonaries and lists
* many functions in the imported libraries



# Credits
The authors for this project are:
* Anita Rull 
* Nora Rosa
* Sebastian Llobet 
* Alberto Padilla
* Ramon Zubiaga
* Cristina Tuduri
